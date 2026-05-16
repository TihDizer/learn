{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          python313
          python313Packages.playwright
          stdenv.cc.cc.lib
          chromium
          chromedriver
        ];

        shellHook = ''
          echo "Nix dev shell activated"
          trap 'deactivate > /dev/null; echo "Nix dev shell deactivated"' EXIT
        '';
      };
    };
}
