#!/usr/bin/env python3
"""
BEAR Chart Generator
Produces publication-ready PNG charts for BEAR diagnoses and pulses.

Usage:
  python3 bear-charts.py timeline <json_file> <output_png>
  python3 bear-charts.py search-lead-gap <json_file> <output_png>
  python3 bear-charts.py convergence <json_file> <output_png>
  python3 bear-charts.py cost-pressure <json_file> <output_png>
  python3 bear-charts.py sparkline <json_file> <output_png>

Each chart type reads a simple JSON input file. See examples below.
"""

import sys
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

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

def apply_style(fig, ax):
    """Apply consistent BEAR styling to any chart."""
    fig.patch.set_facecolor(COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COLORS['grid'])
    ax.spines['bottom'].set_color(COLORS['grid'])
    ax.tick_params(colors=COLORS['text'], labelsize=9)
    ax.grid(axis='y', color=COLORS['grid'], linewidth=0.5, alpha=0.7)


def chart_timeline(data, output):
    """
    Indicator timeline with event annotations.

    JSON input:
    {
      "title": "Consumer Confidence Index",
      "subtitle": "ANZ-Roy Morgan Weekly, Feb-Apr 2026",
      "y_label": "Index",
      "dates": ["2026-02-24", "2026-03-03", ...],
      "values": [80.2, 77.1, ...],
      "events": [
        {"date": "2026-02-28", "label": "Iran strikes begin"},
        {"date": "2026-03-17", "label": "RBA hikes to 4.10%"}
      ],
      "reference_lines": [
        {"value": 65.3, "label": "COVID low (Mar 2020)"}
      ]
    }
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    apply_style(fig, ax)

    dates = [datetime.strptime(d, '%Y-%m-%d') for d in data['dates']]
    values = data['values']

    ax.plot(dates, values, color=COLORS['accent'], linewidth=2.5, marker='o',
            markersize=6, markerfacecolor=COLORS['accent'], markeredgecolor='white',
            markeredgewidth=1.5, zorder=5)

    # Fill below line
    ax.fill_between(dates, values, min(values) * 0.95, alpha=0.08, color=COLORS['accent'])

    # Event annotations
    for event in data.get('events', []):
        edate = datetime.strptime(event['date'], '%Y-%m-%d')
        # Find closest y value
        closest_idx = min(range(len(dates)), key=lambda i: abs(dates[i] - edate))
        y_val = values[closest_idx]
        ax.axvline(x=edate, color=COLORS['annotation'], linewidth=1, linestyle='--', alpha=0.6)
        ax.annotate(event['label'], xy=(edate, y_val),
                    xytext=(10, 20), textcoords='offset points',
                    fontsize=8, color=COLORS['text'],
                    arrowprops=dict(arrowstyle='->', color=COLORS['annotation'], lw=0.8),
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=COLORS['grid'], alpha=0.9))

    # Reference lines
    for ref in data.get('reference_lines', []):
        ax.axhline(y=ref['value'], color=COLORS['neutral'], linewidth=1, linestyle=':', alpha=0.8)
        ax.text(dates[-1], ref['value'] + 0.5, ref['label'],
                fontsize=8, color=COLORS['neutral'], ha='right', va='bottom')

    ax.set_title(data['title'], fontsize=14, fontweight='bold', color=COLORS['primary'], pad=15)
    if data.get('subtitle'):
        ax.text(0.5, 1.02, data['subtitle'], transform=ax.transAxes,
                fontsize=9, color=COLORS['annotation'], ha='center')
    ax.set_ylabel(data.get('y_label', ''), fontsize=10, color=COLORS['text'])
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    fig.autofmt_xdate(rotation=30)

    plt.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close(fig)
    print(f"Saved: {output}")


def chart_search_lead_gap(data, output):
    """
    Dual-axis chart: search interest vs lead volume.

    JSON input:
    {
      "title": "Search Interest vs Lead Volume",
      "subtitle": "Victoria 'roller shutters' vs Titan leads, Feb-Apr 2026",
      "periods": ["Feb", "Mar 1-14", "Mar 15-28", "Mar 29-Apr"],
      "search_values": [100, 83, 72, 60],
      "search_label": "Google Trends (VIC)",
      "lead_values": [50, 38, 25, 20],
      "lead_label": "Titan Leads/Month",
      "gap_annotation": "The gap = conversion collapse"
    }
    """
    fig, ax1 = plt.subplots(figsize=(10, 5))
    apply_style(fig, ax1)

    x = range(len(data['periods']))

    # Search interest (left axis)
    line1 = ax1.plot(x, data['search_values'], color=COLORS['secondary'], linewidth=2.5,
                     marker='o', markersize=7, markerfacecolor=COLORS['secondary'],
                     markeredgecolor='white', markeredgewidth=1.5, label=data.get('search_label', 'Search Interest'))
    ax1.set_ylabel(data.get('search_label', 'Search Interest'), fontsize=10, color=COLORS['secondary'])
    ax1.tick_params(axis='y', labelcolor=COLORS['secondary'])

    # Lead volume (right axis)
    ax2 = ax1.twinx()
    line2 = ax2.plot(x, data['lead_values'], color=COLORS['accent'], linewidth=2.5,
                     marker='s', markersize=7, markerfacecolor=COLORS['accent'],
                     markeredgecolor='white', markeredgewidth=1.5, label=data.get('lead_label', 'Leads'))
    ax2.set_ylabel(data.get('lead_label', 'Leads'), fontsize=10, color=COLORS['accent'])
    ax2.tick_params(axis='y', labelcolor=COLORS['accent'])
    ax2.spines['right'].set_color(COLORS['grid'])
    ax2.spines['top'].set_visible(False)

    # Fill the gap between normalized lines
    ax1.fill_between(x, data['search_values'],
                     [s * (data['lead_values'][0] / data['search_values'][0]) for s in data['search_values']],
                     alpha=0.06, color=COLORS['accent'])

    ax1.set_xticks(x)
    ax1.set_xticklabels(data['periods'], fontsize=9)

    # Combined legend
    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc='upper right', fontsize=9, framealpha=0.9)

    # Gap annotation
    if data.get('gap_annotation'):
        mid = len(x) // 2
        ax1.annotate(data['gap_annotation'],
                     xy=(mid, (data['search_values'][mid] + data['lead_values'][mid]) / 2),
                     fontsize=9, color=COLORS['annotation'], ha='center',
                     bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=COLORS['grid']))

    ax1.set_title(data['title'], fontsize=14, fontweight='bold', color=COLORS['primary'], pad=15)
    if data.get('subtitle'):
        ax1.text(0.5, 1.02, data['subtitle'], transform=ax1.transAxes,
                 fontsize=9, color=COLORS['annotation'], ha='center')

    plt.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close(fig)
    print(f"Saved: {output}")


def chart_convergence(data, output):
    """
    Competitive convergence map: competitors plotted by angle clustering.

    JSON input:
    {
      "title": "Competitive Convergence Map",
      "subtitle": "Melbourne Roller Shutters, 12 competitors",
      "competitors": [
        {"name": "Titan", "angle": "Design", "proof_density": 453, "is_client": true},
        {"name": "Ultimate", "angle": "Trust", "proof_density": 200, "is_client": false},
        {"name": "Security Plus", "angle": "Security", "proof_density": 150, "is_client": false, "price_play": true}
      ]
    }
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    apply_style(fig, ax)

    # Group by angle
    angles = {}
    for c in data['competitors']:
        angle = c['angle']
        if angle not in angles:
            angles[angle] = []
        angles[angle].append(c)

    # Assign x positions by angle, y by proof density
    angle_list = sorted(angles.keys())
    angle_x = {a: i for i, a in enumerate(angle_list)}

    for comp in data['competitors']:
        x = angle_x[comp['angle']]
        y = comp.get('proof_density', 50)
        # Jitter x slightly to avoid overlap
        import random
        random.seed(hash(comp['name']))
        x_jitter = x + random.uniform(-0.15, 0.15)

        is_client = comp.get('is_client', False)
        has_price_play = comp.get('price_play', False)

        color = COLORS['accent'] if is_client else (COLORS['negative'] if has_price_play else COLORS['secondary'])
        size = max(40, min(300, y * 0.6))
        edge = 'white' if is_client else 'none'
        linewidth = 2 if is_client else 0

        ax.scatter(x_jitter, y, s=size, c=color, alpha=0.7, edgecolors=edge, linewidths=linewidth, zorder=5)
        ax.annotate(comp['name'], (x_jitter, y), textcoords='offset points',
                    xytext=(0, 8), ha='center', fontsize=7.5,
                    fontweight='bold' if is_client else 'normal',
                    color=COLORS['primary'] if is_client else COLORS['text'])

    # Highlight crowded angles
    for angle, comps in angles.items():
        if len(comps) >= 3:
            x = angle_x[angle]
            ax.axvspan(x - 0.4, x + 0.4, alpha=0.06, color=COLORS['negative'])
            ax.text(x, ax.get_ylim()[1] * 0.95, f"CROWDED ({len(comps)})",
                    ha='center', fontsize=7, color=COLORS['negative'], fontweight='bold')

    ax.set_xticks(range(len(angle_list)))
    ax.set_xticklabels(angle_list, fontsize=9, rotation=30, ha='right')
    ax.set_ylabel('Proof Density (reviews/testimonials)', fontsize=10, color=COLORS['text'])
    ax.set_title(data['title'], fontsize=14, fontweight='bold', color=COLORS['primary'], pad=15)
    if data.get('subtitle'):
        ax.text(0.5, 1.02, data['subtitle'], transform=ax.transAxes,
                fontsize=9, color=COLORS['annotation'], ha='center')

    plt.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close(fig)
    print(f"Saved: {output}")


def chart_cost_pressure(data, output):
    """
    Cost pressure bar chart showing input cost changes.

    JSON input:
    {
      "title": "Cost Pressure Summary",
      "subtitle": "Pre-crisis vs Current, as of April 2026",
      "items": [
        {"label": "Petrol", "before": 1.71, "after": 2.53, "unit": "$/L"},
        {"label": "Aluminium (LME)", "before": 2300, "after": 3585, "unit": "$/t"},
        {"label": "RBA Cash Rate", "before": 3.85, "after": 4.10, "unit": "%"}
      ]
    }
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    apply_style(fig, ax)

    labels = [item['label'] for item in data['items']]
    pct_changes = [((item['after'] - item['before']) / item['before']) * 100 for item in data['items']]

    colors = [COLORS['negative'] if p > 0 else COLORS['positive'] for p in pct_changes]

    bars = ax.barh(labels, pct_changes, color=colors, height=0.5, alpha=0.85, edgecolor='white', linewidth=1)

    # Add value labels
    for bar, item, pct in zip(bars, data['items'], pct_changes):
        unit = item.get('unit', '')
        label = f"+{pct:.1f}%  ({item['before']}{unit} \u2192 {item['after']}{unit})"
        x_pos = bar.get_width() + 1
        ax.text(x_pos, bar.get_y() + bar.get_height() / 2,
                label, va='center', fontsize=9, color=COLORS['text'])

    ax.set_xlabel('Change (%)', fontsize=10, color=COLORS['text'])
    ax.set_title(data['title'], fontsize=14, fontweight='bold', color=COLORS['primary'], pad=15)
    if data.get('subtitle'):
        ax.text(0.5, 1.02, data['subtitle'], transform=ax.transAxes,
                fontsize=9, color=COLORS['annotation'], ha='center')

    ax.axvline(x=0, color=COLORS['grid'], linewidth=1)

    plt.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close(fig)
    print(f"Saved: {output}")


def chart_sparkline(data, output):
    """
    Compact sparkline panel for pulse reports.

    JSON input:
    {
      "title": "BEAR Pulse: Titan Shutters",
      "date": "2026-04-14",
      "keywords": [
        {"keyword": "roller shutters", "values": [65, 62, 58, 55, 53], "direction": "declining"},
        {"keyword": "security shutters", "values": [45, 48, 41, 50, 47], "direction": "stable"},
        {"keyword": "electric shutters", "values": [30, 28, 25, 22, 20], "direction": "declining"}
      ],
      "indicators": [
        {"label": "Consumer Confidence", "value": 61.2, "prev": 58.8, "direction": "recovering"},
        {"label": "Aluminium (LME)", "value": 3420, "prev": 3585, "direction": "easing"}
      ]
    }
    """
    n_keywords = len(data.get('keywords', []))
    n_indicators = len(data.get('indicators', []))
    n_rows = n_keywords + n_indicators

    fig, axes = plt.subplots(n_rows, 1, figsize=(8, n_rows * 1.2))
    fig.patch.set_facecolor(COLORS['background'])

    if n_rows == 1:
        axes = [axes]

    row = 0

    # Keyword sparklines
    for kw in data.get('keywords', []):
        ax = axes[row]
        vals = kw['values']
        direction = kw.get('direction', 'stable')

        color = COLORS['negative'] if direction == 'declining' else (
            COLORS['positive'] if direction == 'rising' else COLORS['neutral'])

        ax.plot(vals, color=color, linewidth=2)
        ax.fill_between(range(len(vals)), vals, min(vals) * 0.95, alpha=0.1, color=color)
        ax.set_xlim(0, len(vals) - 1)

        # Remove all decorations
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

        # Label
        arrow = {'declining': '\u2198', 'rising': '\u2197', 'stable': '\u2192'}.get(direction, '')
        change = vals[-1] - vals[0]
        sign = '+' if change > 0 else ''
        ax.text(-0.02, 0.5, f"{kw['keyword']}", transform=ax.transAxes,
                fontsize=10, fontweight='bold', color=COLORS['text'], ha='right', va='center')
        ax.text(1.02, 0.5, f"{vals[-1]}  {arrow}  ({sign}{change})", transform=ax.transAxes,
                fontsize=10, color=color, ha='left', va='center')

        row += 1

    # Indicator rows (no sparkline, just value + direction)
    for ind in data.get('indicators', []):
        ax = axes[row]
        direction = ind.get('direction', 'stable')
        color = COLORS['positive'] if direction in ('recovering', 'easing') else (
            COLORS['negative'] if direction in ('worsening', 'rising') else COLORS['neutral'])

        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

        prev = ind.get('prev', 0)
        curr = ind.get('value', 0)
        if prev != 0:
            pct = ((curr - prev) / prev) * 100
            sign = '+' if pct > 0 else ''
            change_str = f"{sign}{pct:.1f}%"
        else:
            change_str = ''

        ax.text(-0.02, 0.5, ind['label'], transform=ax.transAxes,
                fontsize=10, fontweight='bold', color=COLORS['text'], ha='right', va='center')
        ax.text(1.02, 0.5, f"{curr}  ({change_str})  {direction}", transform=ax.transAxes,
                fontsize=10, color=color, ha='left', va='center')

        row += 1

    fig.suptitle(data.get('title', 'BEAR Pulse'), fontsize=13, fontweight='bold',
                 color=COLORS['primary'], y=1.02)

    plt.tight_layout()
    fig.savefig(output, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close(fig)
    print(f"Saved: {output}")


# -- CLI dispatcher --
CHARTS = {
    'timeline': chart_timeline,
    'search-lead-gap': chart_search_lead_gap,
    'convergence': chart_convergence,
    'cost-pressure': chart_cost_pressure,
    'sparkline': chart_sparkline,
}

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    chart_type = sys.argv[1]
    json_file = sys.argv[2]
    output_file = sys.argv[3]

    if chart_type not in CHARTS:
        print(f"Unknown chart type: {chart_type}")
        print(f"Available: {', '.join(CHARTS.keys())}")
        sys.exit(1)

    with open(json_file) as f:
        data = json.load(f)

    CHARTS[chart_type](data, output_file)
