terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = "ru-central1-a"
  token     = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

variable "token" { type = string }
variable "cloud_id" { type = string }
variable "folder_id" { type = string }
variable "ssh_key_path" {
  type    = string
  default = "~/.ssh/id_rsa.pub"
}

data "yandex_compute_image" "ubuntu" {
  family = "ubuntu-2204-lts"
}

# Network
resource "yandex_vpc_network" "lab-net" {
  name = "lab-network"
}

resource "yandex_vpc_subnet" "lab-subnet" {
  name           = "lab-subnet"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.lab-net.id
  v4_cidr_blocks = ["10.0.1.0/24"]
}

# Security Group
resource "yandex_vpc_security_group" "lab-sg" {
  name       = "lab-sg"
  network_id = yandex_vpc_network.lab-net.id

  ingress {
    protocol       = "TCP"
    port           = 80
    v4_cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    protocol       = "TCP"
    port           = 443
    v4_cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    protocol       = "TCP"
    port           = 22
    v4_cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol       = "ANY"
    v4_cidr_blocks = ["0.0.0.0/0"]
  }
}

# GitLab Instance
resource "yandex_compute_instance" "gitlab" {
  name = "gitlab-server"
  zone = "ru-central1-a"

  resources {
    cores  = 4
    memory = 8
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.ubuntu.id
      size     = 30
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.lab-subnet.id
    nat       = true
    security_group_ids = [yandex_vpc_security_group.lab-sg.id]
  }

  metadata = {
    ssh-keys  = "ubuntu:${file(var.ssh_key_path)}"
    user-data = <<-EOF
      #cloud-config
      package_update: true
      packages:
        - docker.io
        - docker-compose
      runcmd:
        - systemctl enable docker
        - systemctl start docker
        - mkdir -p /home/ubuntu/gitlab
        - |
          cat > /home/ubuntu/gitlab/docker-compose.yml <<EOL
          version: '3.6'
          services:
            gitlab:
              image: gitlab/gitlab-ce:latest
              container_name: gitlab
              restart: unless-stopped
              hostname: 'gitlab.local'
              ports:
                - "80:80"
                - "443:443"
                - "2222:22"
              volumes:
                - ./config:/etc/gitlab
                - ./logs:/var/log/gitlab
                - ./data:/var/opt/gitlab
          EOL
        - cd /home/ubuntu/gitlab && docker-compose up -d
    EOF
  }
}

# GitLab Runner Instance
resource "yandex_compute_instance" "runner" {
  name = "gitlab-runner"
  zone = "ru-central1-a"

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.ubuntu.id
      size     = 20
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.lab-subnet.id
    nat       = true
    security_group_ids = [yandex_vpc_security_group.lab-sg.id]
  }

  metadata = {
    ssh-keys  = "ubuntu:${file(var.ssh_key_path)}"
    user-data = <<-EOF
      #cloud-config
      package_update: true
      packages:
        - docker.io
      runcmd:
        - systemctl enable docker
        - systemctl start docker
        - curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | bash
        - apt-get install -y gitlab-runner
    EOF
  }
}

output "gitlab_public_ip" {
  value = yandex_compute_instance.gitlab.network_interface.0.nat_ip_address
}

output "runner_public_ip" {
  value = yandex_compute_instance.runner.network_interface.0.nat_ip_address
}
