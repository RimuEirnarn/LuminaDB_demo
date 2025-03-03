"""So how do we fetch a data?"""

from table_api_01_create_db import notes_table

# By default, using empty .select() returns ALL values inside the table, this returns list of Rows
all_notes = notes_table.select()

# Specific one? If we follow previous case where we insert a note with "Hello, World!"
# We can fetch that specific data like this:
first_note = notes_table.select_one({'title': "Hello, World!"})

# You can replace it with .select(), it'll work well.
print(all_notes)
print(first_note)
