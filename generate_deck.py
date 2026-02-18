"""
Generate an Anki .apkg file from a TSV file.

Install: pip install genanki
Usage:   python generate_deck.py                                        (reads computer-science/data-structures.tsv)
         python generate_deck.py computer-science/data-structures.tsv   (same, explicit)
         python generate_deck.py my_cards.tsv "My Deck Name"            (custom file and deck name)
Output:  decks/<deck-name>.apkg (double-click to import into Anki)

Card format in TSV: one card per line, front and back separated by a tab.
"""

import csv
import os
import sys
import genanki

# Unique IDs (random but stable — don't change these once cards exist)
MODEL_ID = 1607392319
DECK_ID = 2059400110

model = genanki.Model(
    MODEL_ID,
    "Basic CS Card",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Front}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        },
    ],
    css="""
    .card {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 20px;
        text-align: center;
        color: #333;
        background-color: #fff;
        padding: 20px;
    }
    """,
)

tsv_file = sys.argv[1] if len(sys.argv) > 1 else "computer-science/data-structures.tsv"

# Derive deck name from filename if not provided
if len(sys.argv) > 2:
    deck_name = sys.argv[2]
else:
    basename = os.path.splitext(os.path.basename(tsv_file))[0]
    deck_name = basename.replace("-", " ").title()

deck = genanki.Deck(DECK_ID, deck_name)

with open(tsv_file, newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    count = 0
    for row in reader:
        if len(row) >= 2:
            note = genanki.Note(model=model, fields=[row[0], row[1]])
            deck.add_note(note)
            count += 1

os.makedirs("decks", exist_ok=True)
output_file = os.path.join("decks", f"{deck_name.lower().replace(' ', '_')}.apkg")
genanki.Package(deck).write_to_file(output_file)
print(f"Created {output_file} with {count} cards from {tsv_file}")
