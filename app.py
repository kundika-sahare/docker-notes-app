from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)

NOTES_FILE = "notes.json"

# Load notes from file
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

# Save notes to file
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

notes = load_notes()

@app.route('/')
def index():
    return render_template("index.html", notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    notes.append({"title": title, "content": content})
    save_notes(notes)
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
        save_notes(notes)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
