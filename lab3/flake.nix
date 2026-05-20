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
          python312
          stdenv.cc.cc.lib
        ];
        shellHook = ''
          export LD_LIBRARY_PATH="${pkgs.stdenv.cc.cc.lib}/lib:\$LD_LIBRARY_PATH"

          if [ ! -d ".venv" ]; then
            python -m venv .venv
          fi
          source .venv/bin/activate
          pip install --upgrade pip > /dev/null
          if [ -f "requirements.txt" ]; then
            pip install -r requirements.txt > /dev/null
          fi
          echo "Nix dev shell activated (venv ready)"
          trap 'deactivate > /dev/null; echo "Nix dev shell deactivated"' EXIT
        '';
      };
    };
}
