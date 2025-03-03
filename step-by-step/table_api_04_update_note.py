"""So how do we get full CRUD?"""

from table_api_01_create_db import notes_table

# Previously, we have 2 notes.
# And updating one of them is easy.

notes_table.update({'title': "My title"}, # We checked if a row has title of "My Title"
                   {"title": "Some random title"}) # And then we provide our changes
