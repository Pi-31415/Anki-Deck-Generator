import tkinter as tk
from tkinter import scrolledtext, filedialog, Label
import genanki
import hashlib

def generate_deck():
    word_definitions_text = text_area.get("1.0", tk.END)
    deck_name = deck_name_entry.get()

    # Convert deck name to a unique integer using a hash function
    hash_object = hashlib.md5(deck_name.encode())
    deck_id = int(hash_object.hexdigest(), 16) % (1 << 31)
    model_id = deck_id + 1  # Ensure model_id is different but related

    # Parse input text to dictionary
    word_definitions = {}
    for line in word_definitions_text.strip().split('\n'):
        if ':' in line:
            word, definition = line.split(':', 1)
            word_definitions[word.strip()] = definition.strip()

    # Create the Anki deck
    model = genanki.Model(
        model_id,
        'Simple Model',
        fields=[
            {'name': 'Word'},
            {'name': 'Definition'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Word}}',
                'afmt': '{{Definition}}',
            },
            {
                'name': 'Card 2',
                'qfmt': '{{Definition}}',
                'afmt': '{{Word}}',
            },
        ])

    deck = genanki.Deck(deck_id, deck_name)

    for word, definition in word_definitions.items():
        note = genanki.Note(model=model, fields=[word, definition])
        deck.add_note(note)

    # Ask the user to choose a save location
    filename = filedialog.asksaveasfilename(
        initialdir="/",
        initialfile=deck_name.replace(" ", "_").lower() + '.apkg',
        title="Save deck",
        filetypes=(("Anki Deck Package", "*.apkg"), ("All Files", "*.*")),
        defaultextension=".apkg"
    )

    if filename:  # Check if a filename was selected
        genanki.Package(deck).write_to_file(filename)

# Create the main window
root = tk.Tk()
root.title("Anki Deck Generator by Pi")

# Instruction label
instruction_label = Label(root, text="Enter word definitions in the format 'word: definition'.\nEnter a deck name and click 'Generate Deck'.")
instruction_label.pack(pady=10)

# Label and scrolled text area for input
input_label = Label(root, text="Word Definitions:")
input_label.pack()
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# Label and entry for deck name
deck_name_label = Label(root, text="Deck Name:")
deck_name_label.pack()
deck_name_entry = tk.Entry(root, width=30)
deck_name_entry.pack(pady=5)

# Button to generate the deck
generate_button = tk.Button(root, text="Generate Deck", command=generate_deck)
generate_button.pack(pady=10)

# Run the application
root.mainloop()
