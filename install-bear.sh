#!/bin/bash
# BEAR Method Installer v3.12.0
# Copies the BEAR skill and tools into your Claude Code directories.
# Run from the folder containing this script.

set -e

SKILLS_DIR="$HOME/.claude/skills"
TOOLS_DIR="$HOME/.claude/tools"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_SKILLS="$SCRIPT_DIR/skills"
SOURCE_TOOLS="$SCRIPT_DIR/tools"

# Check source exists
if [ ! -d "$SOURCE_SKILLS" ]; then
    echo "ERROR: No 'skills/' folder found next to this script."
    echo "Expected: $SOURCE_SKILLS"
    echo "Make sure you're running this from the BEAR distribution folder."
    exit 1
fi

# Create directories if they don't exist
mkdir -p "$SKILLS_DIR"
mkdir -p "$TOOLS_DIR"

# Install skill
echo "Installing BEAR skill..."
cp -R "$SOURCE_SKILLS/bear" "$SKILLS_DIR/"
echo "  Installed: ~/.claude/skills/bear/SKILL.md"

# Install chart tool
if [ -f "$SOURCE_TOOLS/bear-charts.py" ]; then
    echo "Installing chart generator..."
    cp "$SOURCE_TOOLS/bear-charts.py" "$TOOLS_DIR/"
    echo "  Installed: ~/.claude/tools/bear-charts.py"
fi

echo ""
echo "BEAR v3.12.0 installed successfully."
echo ""
echo "Quick start:"
echo "  /bear diagnose {client-name}    # Full market shift diagnosis"
echo "  /bear pulse {client-name}       # Weekly monitoring check"
echo ""
echo "Optional: install matplotlib for chart generation:"
echo "  pip install matplotlib"
