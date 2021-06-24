from db import Database


class SQL(Database):
    def __init__(self):
        super().__init__("posts_db")

        if not self._table_exists("posts_table"):
            self._make_table("posts_table", [
                ("id", "INTEGER PRIMARY KEY"),
                ("title", "TEXT"),
                ("content", "TEXT")
            ])

    def _quotify(self, string: str):
        return "'" + string + "'"

    def load(self, post_id: int):
        record = self._lookup_record("posts_table", f"id={post_id}")
        if record:
            return {"id": record[0][0], "title": record[0][1], "content": record[0][2]}
        return False

    def save(self, title: str, content: str):
        self._add_record("posts_table", [
            ("title", self._quotify(title)),
            ("content", self._quotify(content))
        ])
        return self._lookup_record("posts_table", f"content='{content}'")[-1][0]
