#!/usr/bin/env bash
set -euo pipefail

if nix_path="$(type -p nix)" ; then
  echo "Aborting: Nix is already installed at ${nix_path}"
  exit
fi

echo "::group::Installing nix-portable"

# Download nix-portable
arch=$(uname -m)
echo "Downloading nix-portable for architecture: $arch"

curl_retries=5
while ! curl -sS -o "$HOME/nix-portable" --fail -L "https://github.com/DavHau/nix-portable/releases/latest/download/nix-portable-${arch}"
do
  sleep 1
  ((curl_retries--))
  if [[ $curl_retries -le 0 ]]; then
    echo "curl retries failed" >&2
    exit 1
  fi
done

chmod +x "$HOME/nix-portable"

# Create a symlink so scripts can call 'nix' directly
mkdir -p "$HOME/.local/bin"
ln -s "$HOME/nix-portable" "$HOME/.local/bin/nix"

# Add to PATH so scripts can find 'nix'
echo "$HOME/.local/bin" >> "$GITHUB_PATH"

# Build nix configuration and set as environment variable
nix_config="experimental-features = nix-command flakes"$'\n'
nix_config+="show-trace = true"$'\n'
nix_config+="max-jobs = auto"$'\n'

# Add GitHub access token if available
if [[ -n "${INPUT_GITHUB_ACCESS_TOKEN:-}" ]]; then
  echo "::debug::Using provided GitHub access token"
  nix_config+="access-tokens = github.com=$INPUT_GITHUB_ACCESS_TOKEN"$'\n'
elif [[ -n "${GITHUB_TOKEN:-}" && $GITHUB_SERVER_URL == "https://github.com" ]]; then
  echo "::debug::Using default GITHUB_TOKEN"
  nix_config+="access-tokens = github.com=$GITHUB_TOKEN"$'\n'
fi

# Add extra nix configuration if provided
if [[ -n "${INPUT_EXTRA_NIX_CONFIG:-}" ]]; then
  nix_config+="$INPUT_EXTRA_NIX_CONFIG"$'\n'
fi

# Set environment variables for subsequent steps
echo "NIX_CONFIG<<EOF" >> "$GITHUB_ENV"
echo "$nix_config" >> "$GITHUB_ENV"
echo "EOF" >> "$GITHUB_ENV"

echo "NIX_PORTABLE_PATH=$HOME/nix-portable" >> "$GITHUB_ENV"
echo "NP_RUNTIME=proot" >> "$GITHUB_ENV"

# Set NIX_PATH if requested
if [[ -n "${INPUT_NIX_PATH:-}" ]]; then
  echo "NIX_PATH=${INPUT_NIX_PATH}" >> "$GITHUB_ENV"
fi

# Set temporary directory for better performance
if [[ -z "${TMPDIR:-}" ]]; then
  echo "TMPDIR=${RUNNER_TEMP}" >> "$GITHUB_ENV"
fi

echo "nix-portable installed successfully at $HOME/nix-portable"
echo "Testing installation..."
"$HOME/nix-portable" nix --version

echo "::endgroup::"
