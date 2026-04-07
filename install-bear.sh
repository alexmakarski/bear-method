#!/bin/bash
# BEAR Method Installer
# Copies the BEAR skill into your Claude Code directories.
# Run from the folder containing this script.

set -e

SKILLS_DIR="$HOME/.claude/skills"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_SKILLS="$SCRIPT_DIR/skills"

# Check source exists
if [ ! -d "$SOURCE_SKILLS" ]; then
    echo "ERROR: No 'skills/' folder found next to this script."
    echo "Expected: $SOURCE_SKILLS"
    echo "Make sure you're running this from the BEAR distribution folder."
    exit 1
fi

# Create directories if they don't exist
mkdir -p "$SKILLS_DIR"

# Install skill
echo "Installing BEAR skill..."
cp -R "$SOURCE_SKILLS/bear" "$SKILLS_DIR/"
echo "  Installed: bear"

echo ""
echo "BEAR installed successfully."
echo ""
echo "Quick start:"
echo "  /bear diagnose {client-name}"
echo "  /bear snapshot {client-name}"
echo "  /bear compare {client-name}"
