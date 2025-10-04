"""This module showcase you how to create a Database instance with Table API"""

from luminadb import Database, text

db = Database("database.db", forgive=True) # You can pass a filename like "my_db.db" or ":memory:"

# We create a table named "notes" and then we define the scheme with text()
notes_table = db.create_table("notes", [
    # Id is your column, it has text as type
    text('id').primary(), # Make sure this ID is primary key
    text('title'),
    text('content')
])
