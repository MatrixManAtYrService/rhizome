{
  description = "A project template";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs = {
        pyproject-nix.follows = "pyproject-nix";
        uv2nix.follows = "uv2nix";
        nixpkgs.follows = "nixpkgs";
      };
    };
  };

  outputs = { self, nixpkgs, flake-utils, uv2nix, pyproject-nix, pyproject-build-systems }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # Import Artifactory overlay functions
        artifactoryLib = import ./nix/artifactory.nix { inherit (nixpkgs) lib; };


        # Override Python packages in nixpkgs to redirect PyPI URLs to Artifactory
        nixpkgsArtifactoryOverlay = final: prev:
          let
            overlayFuncs = artifactoryLib.mkNixpkgsOverlay {
              inherit (final) cacert;
              inherit (nixpkgs) lib;
            };
          in
          {
            python312Packages = overlayFuncs.python312Packages prev.python312Packages;
            python313Packages = overlayFuncs.python313Packages prev.python313Packages;
            python311Packages = overlayFuncs.python311Packages prev.python311Packages;
          };

        # Override Python packages fetched via pypkg to redirect PyPI URLs to Artifactory
        pyprojectArtifactoryOverlay = final: prev:
          artifactoryLib.mkPyprojectOverlay
            {
              inherit (pkgs) cacert lib;
            }
            prev;

        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            nixpkgsArtifactoryOverlay
          ];
          config.allowUnfree = true;
        };

        # Import project constants
        constants = import ./nix/constants.nix { };

        python = pkgs.python312;
        workspace = uv2nix.lib.workspace.loadWorkspace {
          workspaceRoot = ./.;
        };

        pyprojectOverlay = workspace.mkPyprojectOverlay {
          sourcePreference = "wheel";
        };


        pythonSet = (pkgs.callPackage pyproject-nix.build.packages {
          inherit python;
        }).overrideScope (
          nixpkgs.lib.composeManyExtensions [
            pyproject-build-systems.overlays.default
            pyprojectOverlay
            pyprojectArtifactoryOverlay
          ]
        );

        editableOverlay = workspace.mkEditablePyprojectOverlay {
          root = "$REPO_ROOT";
        };

        editableHatchling = final: prev: {
          ${constants.name} = prev.${constants.name}.overrideAttrs (old: {
            nativeBuildInputs =
              old.nativeBuildInputs
              ++ final.resolveBuildSystem {
                editables = [ ];
              };
          });
        };



        editablePythonSet = pythonSet.overrideScope (
          nixpkgs.lib.composeManyExtensions [
            editableOverlay
            editableHatchling
          ]
        );

        pythonEnv = pythonSet.mkVirtualEnv constants.name workspace.deps.default;
      in
      {
        packages = {
          default = pythonEnv;
          nix-analysis = pkgs.callPackage ./nix/nix-analysis.nix { };
          python-analysis = pkgs.callPackage ./nix/python-analysis.nix { };
          docs = pkgs.callPackage ./nix/docs.nix { inherit constants; };
          codegen = pkgs.callPackage ./nix/codegen.nix { inherit constants; };
          version-bump = pkgs.callPackage ./nix/version-bump.nix { };
        };

        apps = rec {
          default = {
            type = "app";
            program = "${pythonEnv}/bin/${constants.name}";
          };
          hello = default;
        };

        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            (editablePythonSet.mkVirtualEnv constants.name workspace.deps.all)
            uv
            ruff
            python312Packages.python-lsp-ruff
            python312Packages.cogapp
            pyright
            nixpkgs-fmt
            nix-output-monitor
            kind
            gnumake
            tilt
            kubernetes-helm
            (google-cloud-sdk.withExtraComponents [
              google-cloud-sdk.components.gke-gcloud-auth-plugin
              google-cloud-sdk.components.kubectl
            ])
            _1password-cli
            yq
            k9s
            mariadb_114
          ];
          env = {
            UV_NO_SYNC = "1";
            UV_PYTHON = python.interpreter;
            UV_PYTHON_DOWNLOADS = "never";
          };
          shellHook = ''
            export REPO_ROOT=$(pwd)
          '';
        };
      });
}
