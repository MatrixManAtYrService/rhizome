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
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            # Override ALL Python packages to redirect PyPI URLs to Artifactory
            (final: prev: {
              python312Packages = prev.python312Packages.overrideScope (pyFinal: pyPrev:
                pkgs.lib.mapAttrs (name: pkg: 
                  if pkg ? overrideAttrs && pkg ? src then
                    pkg.overrideAttrs (old: 
                      if old ? src && old.src ? overrideAttrs then {
                        src = old.src.overrideAttrs (srcAttrs: 
                          if srcAttrs ? url then {
                            url = builtins.replaceStrings 
                              ["https://files.pythonhosted.org/packages"] 
                              ["https://artifactory.corp.clover.com/artifactory/api/pypi/libs-python/packages/packages"] 
                              srcAttrs.url;
                          } else if srcAttrs ? urls then {
                            urls = map (url: builtins.replaceStrings 
                              ["https://files.pythonhosted.org/packages"] 
                              ["https://artifactory.corp.clover.com/artifactory/api/pypi/libs-python/packages/packages"] 
                              url
                            ) srcAttrs.urls;
                          } else srcAttrs
                        );
                      } else old
                    )
                  else pkg
                ) pyPrev
              );
            })
          ];
        };

        # Import project constants
        constants = import ./nix/constants.nix { };

        python = pkgs.python312;
        workspace = uv2nix.lib.workspace.loadWorkspace {
          workspaceRoot = ./.;
        };

        overlay = workspace.mkPyprojectOverlay {
          sourcePreference = "wheel";
        };

        pythonSet = (pkgs.callPackage pyproject-nix.build.packages {
          inherit python;
        }).overrideScope (
          nixpkgs.lib.composeManyExtensions [
            pyproject-build-systems.overlays.default
            overlay
            # Apply Artifactory URL redirection to build system packages too
            (final: prev: 
              pkgs.lib.mapAttrs (name: pkg: 
                if pkg ? overrideAttrs && pkg ? src then
                  pkg.overrideAttrs (old: 
                    if old ? src && old.src ? overrideAttrs then {
                      src = old.src.overrideAttrs (srcAttrs: 
                        if srcAttrs ? url then {
                          url = builtins.replaceStrings 
                            ["https://files.pythonhosted.org/packages"] 
                            ["https://artifactory.corp.clover.com/artifactory/api/pypi/libs-python/packages/packages"] 
                            srcAttrs.url;
                        } else if srcAttrs ? urls then {
                          urls = map (url: builtins.replaceStrings 
                            ["https://files.pythonhosted.org/packages"] 
                            ["https://artifactory.corp.clover.com/artifactory/api/pypi/libs-python/packages/packages"] 
                            url
                          ) srcAttrs.urls;
                        } else srcAttrs
                      );
                    } else old
                  )
                else pkg
              ) prev
            )
          ]
        );

        editableOverlay = workspace.mkEditablePyprojectOverlay {
          root = "$REPO_ROOT";
        };

        editableHatchling = (final: prev: {
              ${constants.name} = prev.${constants.name}.overrideAttrs (old: {
                nativeBuildInputs =
                  old.nativeBuildInputs
                  ++ final.resolveBuildSystem {
                    editables = [ ];
                  };
              });
            });



        editablePythonSet = pythonSet.overrideScope (
          nixpkgs.lib.composeManyExtensions [
            editableOverlay
            editableHatchling
          ]
        );

        pythonEnv = pythonSet.mkVirtualEnv constants.name workspace.deps.default;
      in
      rec {
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
