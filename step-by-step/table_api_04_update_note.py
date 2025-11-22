"""So how do we get full CRUD?"""
# pylint: disable=invalid-name

from uuid import uuid4
from luminadb import SKIP
from table_api_01_create_db import notes_table

# Previously, we have 2 notes.
# And updating one of them is easy.

notes_table.update({'title': "My title"}, # We checked if a row has title of "My Title"
                   {"title": "Some random title"}) # And then we provide our changes

# Oh, when updating/inserting data, from version v0.6.5,
# you can now use pre-defined SKIP sentinel. What does it do?
# Suppose we have this:

an_id = str(uuid4())
notes_table.insert({'title': "Hey, this is a title",
                    "content": "wahdgjasdgjas",
                    'id': an_id})

title = SKIP
content = "This is a content"

notes_table.update({'id': an_id}, {"title": title, "content": content})

# The data title will be discarded right away before it reached database
# It's going to safe your life from having to create a dictionary
# And then updating it like:
# if title:
#     new['title'] = title
# None is still translate to NULL in SQL, that's why I created SKIP so it's better
# of creating a Sentinel value

# Oh, and I remind you that using this SKIP sentinel value is required.
