DROP TABLE if EXISTS entries;
CREATE TABLE entries (
  id INTEGER PRIMARY KEY autoincrement,
  title text NOT NULL,
  content text NOT NULL,
  audiofile_cust NOT NULL,
  audiofile text NOT NULL,
  imagefile text NOT NULL
);
