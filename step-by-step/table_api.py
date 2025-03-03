# pylint: disable=all

import table_api_01_create_db
import table_api_02_insert_note
import table_api_03_fetch_note
import table_api_04_update_note
import table_api_05_delete_note

print(table_api_01_create_db.notes_table.select())
