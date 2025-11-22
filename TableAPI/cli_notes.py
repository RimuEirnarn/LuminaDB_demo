"""How to create a simple CRUD app with sqlite-database Table API"""

from uuid import uuid4
from argh import dispatch_commands, arg
from luminadb import Database, text, SKIP

def generate_id():
    """Generate an ID"""
    return str(uuid4())

db = Database("notes.db", forgive=True)

notes = db.create_table('notes', [
    text('id').primary(),
    text('title'),
    text('content')
])

def render_note(note_id: str, title: str, content: str):
    """Render a note"""
    print(f"""\
{'='*8}
Note ID: {note_id}
Title: {title}
Content: {content}
{'='*8}""")

@arg("title", help="Title of this note")
@arg("content", help='Content of this note')
def add_note(title: str, content: str):
    """Add a note to the database"""
    note_id = generate_id()
    notes.insert({
        "id": note_id,
        'title': title,
        "content": content
    })
    print(f"Added successfully: {note_id}")

@arg('note_id', help="The note ID to be changed")
@arg('--title', '-t', help="New title")
@arg("--content", '-c', help="New content")
def update_note(note_id: str, title: str = '', content: str = ""):
    """Change/update a note based on Note ID"""
    updates = {
        "title": title or SKIP,
        "content": content or SKIP
    }

    notes.update({'id': note_id}, updates) # Don't blindly update stuff!

@arg('note_id', help="The note ID to be changed")
def delete(note_id: str):
    """Deleta a note based on ID"""
    notes.delete({'id': note_id})

@arg('note_id', help="The note ID to be changed")
def get(note_id: str):
    """Get a note based on ID"""
    note = notes.select_one({"id": note_id})

    if not note:
        print(f"There's no note of {note}")

    render_note(note.id, note.title, note.content)

def get_all():
    """Return all notes"""
    for note in notes.select():
        render_note(note.id, note.title, note.content)

if __name__ == '__main__':
    dispatch_commands([add_note, update_note, delete, get, get_all])
