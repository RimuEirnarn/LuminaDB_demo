"""Main entry"""

from uuid import uuid4

from luminadb import Null
from flask import Flask, redirect, render_template, request, flash
from model.notes import Notes  # pylint: disable=import-error

app = Flask(__name__)
app.secret_key = "some random key"


@app.post("/note")
def push_note():
    """Push a note"""
    title = request.form.get("title", Null)
    content = request.form.get("content", Null)

    if Null in (title, content):
        flash("Cannot create: Either title/content is undefined", "danger")
    else:
        flash("Note created", "success")

    Notes.create(id=str(uuid4()), title=title, content=content)
    return redirect("/")


@app.patch("/note/<note_id>/patch")
@app.post("/note/<note_id>")
def note_patch(note_id):
    """Patch a note"""
    title = request.form.get("title", Null)
    content = request.form.get("content", Null)

    note = Notes.first(id=note_id)
    if not note:
        flash(f"There is no note of {note}", "danger")
        return redirect("/")

    note.update(title=title, content=content)
    flash("Updated")
    return redirect("/")


@app.delete("/note/<note_id>")
@app.get("/note/<note_id>/delete")
def delete_note(note_id):
    """Delete a note"""

    note = Notes.first(id=note_id)
    if not note:
        flash(f"There's no note of {note}", "warning")
        return redirect("/")

    note.delete()
    flash("Deleted", 'success')
    return redirect("/")


@app.get("/note/<note_id>")
def single_note(note_id):
    """Get a single note"""

    note = Notes.first(id=note_id)
    if not note:
        return redirect("/"), 404

    return render_template("single_note.html", note=note.to_dict())

@app.get("/note/<note_id>/edit")
def edit_form(note_id):
    """Get a single note, and push out edit form"""

    note = Notes.first(id=note_id)
    if not note:
        return redirect("/"), 404

    return render_template("change.html", note=note)

@app.get("/note")
def get_all():
    """Get all notes"""

    notes = Notes.where().fetch()

    return render_template("all_notes.html", notes=[note.to_dict() for note in notes])

@app.get('/')
def index():
    """Index"""
    notes = Notes.where().fetch()

    return render_template("index.html", notes=[note.to_dict() for note in notes])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, threaded=True)
