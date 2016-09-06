from blog_flask.blog.database.db import WorkWithDatabase

class EntryViewModel():

    def get_entries_from_database(self):
        db = WorkWithDatabase()
        entries = db.execute_get_query('select title, content from entries order by id desc')
        db.close_connection()
        return entries