{
  description = "Postman Nix dev shell";

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
        packages = with pkgs; [
          postman
          insomnia
        ];

        shellHook = ''
          echo "Nix dev shell activated"

          mkdir -p .logs

          postman > .logs/postman.log 2>&1 &
          POSTMAN_PID=$!

          insomnia > .logs/insomnia.log 2>&1 &
          INSOMNIA_PID=$!

          cleanup() {
            if kill -0 "$POSTMAN_PID" 2>/dev/null; then
              kill "$POSTMAN_PID" 2>/dev/null || true
              wait "$POSTMAN_PID" 2>/dev/null || true
            fi

            if kill -0 "$INSOMNIA_PID" 2>/dev/null; then
              kill "$INSOMNIA_PID" 2>/dev/null || true
              wait "$INSOMNIA_PID" 2>/dev/null || true
            fi

            echo "Nix dev shell deactivated"
          }

          trap cleanup EXIT INT TERM
        '';
      };
    };
}
