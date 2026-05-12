{
  description = "terraform + yc dev shell";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          terraform
          yandex-cloud
        ];

        shellHook = ''
          echo "Dev shell activated"
          YC_TOKEN=$(yc iam create-token)
          YC_CLOUD_ID=$(yc config get cloud-id)
          YC_FOLDER_ID=$(yc config get folder-id)

          cat > terraform.tfvars << EOF
          token       = "$YC_TOKEN"
          cloud_id    = "$YC_CLOUD_ID"
          folder_id   = "$YC_FOLDER_ID"
          EOF

          terraform version
          trap 'deactivate > /dev/null; echo "Nix dev shell deactivated"' EXIT
        '';
      };
    };
}
