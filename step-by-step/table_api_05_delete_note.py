"""Finally, delete in CRUD"""

from uuid import UUID
from table_api_01_create_db import notes_table

# Uncomment this line if you want to delete ALL rows
# notes_table.delete()

# And, as expected, to delete a row is frankly easy. If you follow previous showcase, it's easy
notes_table.delete({
    'id': str(UUID(int=-0)) # We delete a note with UUID of 0
})
