"""
Deck generator - simple markdown slides for leadership
"""

import os
from datetime import datetime

def generate_deck_md(output_path=os.path.join("..","notebook","spdis_leadership_deck.md"), insights=None, recommendations=None):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    date = datetime.utcnow().strftime("%Y-%m-%d")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# SPDIS Leadership Brief — {date}\n\n")
        f.write("## Key Insights\n\n")
        if not insights:
            f.write("- Insight generation is pending. Run SPDIS analysis to populate.\n")
        else:
            for i,ins in enumerate(insights,1):
                f.write(f"{i}. {ins}\n")
        f.write("\n## Recommendations\n\n")
        if not recommendations:
            f.write("- Recommendations pending. Run SPDIS scenario engine and review results.\n")
        else:
            for i,rec in enumerate(recommendations,1):
                f.write(f"{i}. {rec}\n")
    return output_path
