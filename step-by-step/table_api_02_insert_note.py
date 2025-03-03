"""This showcase you how to insert a data into a table with Table API"""

from uuid import UUID, uuid4
from table_api_01_create_db import notes_table

# Let's define our mock data
my_note = {
    "id": str(uuid4()),
    "title": "My note",
    "content": "I don't know what to write"
}

# .insert() only requires mapping/dictionary. So make sure you give the correct data.
notes_table.insert(my_note)

notes_table.insert({
    'id': str(UUID(int=0)),
    'title': 'My title',
    "content": "Some random data"
})
