# Anki Deck Generator

Generate Anki flashcard decks (`.apkg`) from simple TSV files.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Generate a specific deck
python generate_deck.py computer-science/data-structures.tsv

# Specify a custom deck name
python generate_deck.py computer-science/algorithms.tsv "Algo Fundamentals"

# Default (generates data-structures deck)
python generate_deck.py
```

The deck name is derived from the filename by default (`data-structures.tsv` becomes "Data Structures"). The output `.apkg` file can be double-clicked or imported into Anki.

## Adding Cards

Cards are stored as TSV files — one card per line, front and back separated by a tab:

```text
What is a stack?	A LIFO data structure. Elements are added and removed from the top.
```

HTML is supported in answers for formatting (e.g., `<br>` for line breaks).

## Available Decks

### Computer Science

| File | Cards | Topics |
| ------ | ------- | -------- |
| `computer-science/data-structures.tsv` | 20 | Arrays, linked lists, stacks, queues, hash tables, trees, heaps, tries, graphs, B-trees |
| `computer-science/algorithms.tsv` | 20 | Sorting, searching, BFS/DFS, Dijkstra's, dynamic programming, greedy algorithms, Big O |
| `computer-science/networking.tsv` | 20 | OSI/TCP-IP models, TCP/UDP, DNS, HTTP/HTTPS, subnets, NAT, TLS, load balancers |

## Adding a New Deck

1. Create a new `.tsv` file in the appropriate directory
2. Add cards as `front[TAB]back` pairs, one per line
3. Run `python generate_deck.py path/to/your-file.tsv`
4. Import the generated `.apkg` into Anki
