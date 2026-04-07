#!/bin/bash
# BEAR Method Installer
# Copies the BEAR skill and SerpAPI tool into your Claude Code directories.
# Run from the folder containing this script.

set -e

SKILLS_DIR="$HOME/.claude/skills"
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

# Install skill
echo "Installing BEAR skill..."
cp -R "$SOURCE_SKILLS/bear" "$SKILLS_DIR/"
echo "  Installed: bear"

# Install shared tools (into project, not global)
if [ -d "$SOURCE_TOOLS" ]; then
    echo ""
    echo "SerpAPI tool available in tools/serpapi.sh"
    echo "  Copy to your project's .claude/tools/ directory if needed."
    echo "  Requires SERPAPI_KEY in a .env file (see .env.example)."
fi

echo ""
echo "BEAR installed successfully."
echo ""
echo "Quick start:"
echo "  /bear diagnose {client-name}"
echo "  /bear snapshot {client-name}"
echo "  /bear compare {client-name}"
echo ""
echo "Optional: Set up SerpAPI for Google Trends integration."
echo "  1. Sign up at https://serpapi.com"
echo "  2. Copy .env.example to .env in your project root"
echo "  3. Add your API key"
echo "  BEAR works without SerpAPI (uses WebFetch fallback) but structured data is better."
