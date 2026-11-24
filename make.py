import os

LINE = (
    "Sorry I missed the deadline \u2014 I hallucinated finishing it with 97% "
    "confidence, then hallucinated this apology with the same confidence. "
    "Both felt great."
)

assert len(LINE) <= 200, f"line exceeds 200-char gate limit: {len(LINE)}"

os.makedirs("output", exist_ok=True)
with open("output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"wrote output/entry.txt ({len(LINE)} chars)")