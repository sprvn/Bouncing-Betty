DROP TABLE IF EXISTS programs;
DROP TABLE IF EXISTS targets;
DROP TABLE IF EXISTS domains;


CREATE TABLE programs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);