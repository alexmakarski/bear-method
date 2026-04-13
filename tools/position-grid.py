#!/usr/bin/env python3
"""
BEAR Position Grid Chart Generator
Produces publication-ready PNG of the BEAR Position Grid (2x2 quadrant chart).

Usage:
  python3 position-grid.py <json_file> <output_png>

JSON input:
{
  "title": "BEAR Position Grid",
  "subtitle": "Acme Roofing, April 2026",
  "client_name": "Acme Roofing",
  "performance_gap": -30,
  "positioning_overlap": 75,
  "quadrant": "Bear Trap"
}
"""

import sys
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# -- Style constants --
COLORS = {
    'primary': '#1a1a2e',
    'accent': '#e94560',
    'secondary': '#0f3460',
    'positive': '#2ecc71',
    'negative': '#e74c3c',
    'neutral': '#95a5a6',
    'background': '#fafafa',
    'grid': '#e0e0e0',
    'text': '#2c3e50',
    'annotation': '#7f8c8d',
}

QUADRANT_COLORS = {
    'Grizzly':    '#2ecc71',  # green
    'Salmon Run': '#f39c12',  # amber
    'Den':        '#3498db',  # blue
    'Bear Trap':  '#e74c3c',  # red
}

# Aliases for the open-source quadrant names
QUADRANT_ALIASES = {
    'Roaming': 'Salmon Run',
    'Hibernating': 'Den',
}


def chart_position_grid(data, output):
    """Generate the BEAR Position Grid 2x2 chart."""
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor(COLORS['background'])
    ax.set_facecolor(COLORS['background'])

    x_min, x_max = -60, 60
    y_min, y_max = 0, 100

    # Draw quadrant fills
    # Top-left: Den / Hibernating (negative gap, low overlap)
    ax.axvspan(x_min, 0, ymin=0.5, ymax=1.0, alpha=0.08, color=QUADRANT_COLORS['Den'])
    # Top-right: Grizzly (positive gap, low overlap)
    ax.axvspan(0, x_max, ymin=0.5, ymax=1.0, alpha=0.08, color=QUADRANT_COLORS['Grizzly'])
    # Bottom-left: Bear Trap (negative gap, high overlap)
    ax.axvspan(x_min, 0, ymin=0.0, ymax=0.5, alpha=0.08, color=QUADRANT_COLORS['Bear Trap'])
    # Bottom-right: Salmon Run / Roaming (positive gap, high overlap)
    ax.axvspan(0, x_max, ymin=0.0, ymax=0.5, alpha=0.08, color=QUADRANT_COLORS['Salmon Run'])

    # Midpoint lines
    ax.axhline(y=50, color=COLORS['grid'], linewidth=1.5, linestyle='-', alpha=0.6)
    ax.axvline(x=0, color=COLORS['grid'], linewidth=1.5, linestyle='-', alpha=0.6)

    # Quadrant labels
    label_style = dict(fontsize=16, fontweight='bold', ha='center', va='center', alpha=0.25)
    ax.text(x_max * 0.5, 25, 'GRIZZLY', color=QUADRANT_COLORS['Grizzly'], **label_style)
    ax.text(x_min * 0.5, 25, 'HIBERNATING', color=QUADRANT_COLORS['Den'], **label_style)
    ax.text(x_max * 0.5, 75, 'ROAMING', color=QUADRANT_COLORS['Salmon Run'], **label_style)
    ax.text(x_min * 0.5, 75, 'BEAR TRAP', color=QUADRANT_COLORS['Bear Trap'], **label_style)

    # Plot client dot (Y inverted: low overlap at bottom of data = top of chart)
    x = data['performance_gap']
    y = data['positioning_overlap']

    quadrant = data.get('quadrant', '')
    # Resolve aliases
    resolved = QUADRANT_ALIASES.get(quadrant, quadrant)
    dot_color = QUADRANT_COLORS.get(resolved, COLORS['accent'])

    ax.scatter(x, y, s=250, c=dot_color, edgecolors='white', linewidths=3, zorder=10)

    # Combined label: name + values
    gap_sign = '+' if x > 0 else ''
    label_text = f"{data.get('client_name', '')}\nGap: {gap_sign}{x}%  |  Overlap: {y}%"
    ax.annotate(label_text,
                xy=(x, y), xytext=(14, -16), textcoords='offset points',
                fontsize=9, fontweight='bold', color=COLORS['primary'],
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                          edgecolor=dot_color, alpha=0.95))

    # Axis labels
    ax.set_xlabel('Performance Gap (%)\nUnderperforming market \u2190    \u2192 Beating market',
                  fontsize=10, color=COLORS['text'], labelpad=10)
    ax.set_ylabel('Positioning Overlap (%)\nDifferentiated \u2190    \u2192 Converged',
                  fontsize=10, color=COLORS['text'], labelpad=10)

    # Invert Y so low overlap (differentiated) is at top, high overlap (converged) at bottom
    ax.invert_yaxis()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(100, 0)

    # Clean up spines
    for spine in ax.spines.values():
        spine.set_color(COLORS['grid'])

    ax.set_title(data.get('title', 'BEAR Position Grid'),
                 fontsize=14, fontweight='bold', color=COLORS['primary'], pad=15)
    if data.get('subtitle'):
        ax.text(0.5, 1.02, data['subtitle'], transform=ax.transAxes,
                fontsize=9, color=COLORS['annotation'], ha='center')

    plt.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close(fig)
    print(f"Saved: {output}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    json_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(json_file) as f:
        data = json.load(f)

    chart_position_grid(data, output_file)
