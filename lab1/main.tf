terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}
provider "yandex" {
  zone     = "ru-central1-a"
  token    = var.token
  cloud_id = var.cloud_id
  folder_id = var.folder_id
}

variable "token" { type = string }
variable "cloud_id" { type = string }
variable "folder_id" { type = string }

data "yandex_compute_image" "ubuntu" {
  family = "ubuntu-2204-lts"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = data.yandex_compute_image.ubuntu.id
}

resource "yandex_compute_instance" "lab-gitlab" {
  name = "lab-gitlab"

  labels = {
   environment = "network-1"
   owner       = "tihdizer"
   task        = "block-2"
  }

  resources {
    cores  = 4
    memory = 8
  }

  allow_stopping_for_update = true

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
    security_group_ids = [yandex_vpc_security_group.web_sg.id]
  }

  metadata = {
    ssh-keys  = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
    user-data = <<-EOF
      #cloud-config
      package_update: true
      packages:
        - docker.io
        - docker-compose
      runcmd:
        - systemctl enable docker
        - systemctl start docker
        - usermod -aG docker ubuntu

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
              - ./gitlab/config:/etc/gitlab
              - ./gitlab/logs:/var/log/gitlab
              - ./gitlab/data:/var/opt/gitlab
            environment:
              GITLAB_OMNIBUS_CONFIG: |
                nginx['listen_addresses'] = ['0.0.0.0']
          EOL

        - cd /home/ubuntu/gitlab && docker-compose up -d
    EOF
  }

  lifecycle {
    create_before_destroy = true

    prevent_destroy = false

    ignore_changes = [labels, metadata]
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["10.0.1.0/24"]
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.lab-gitlab.network_interface.0.nat_ip_address
}

output "ssh_command" {
  value = "ssh ubuntu@${yandex_compute_instance.lab-gitlab.network_interface.0.nat_ip_address}"
}

resource "yandex_vpc_security_group" "web_sg" {
  network_id = yandex_vpc_network.network-1.id

  ingress {
    protocol       = "TCP"
    port           = 80
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
