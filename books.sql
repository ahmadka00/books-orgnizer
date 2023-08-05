CREATE TABLE books (
    id INTEGER NOT NULL PRIMARY KEY,
    book TEXT NOT NULL,
    year INTEGER
);
CREATE TABLE writers (
    id INTEGER NOT NULL PRIMARY KEY,
    book_id  INTEGER NOT NULL,
    writer TEXT NOT NULL,
    FOREIGN KEY(book_id) REFERENCES books(id)
);
CREATE TABLE categories (
    book_id INTEGER NOT NULL,
    writer_id INTEGER NOT NULL,
    category TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(writer_id) REFERENCES writers(id)
);
CREATE TABLE shelves (
    shelff TEXT NOT NULL,
    book_id INTEGER NOT NULL,
    writer_id INTEGER NOT NULL,
    categories TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(writer_id) REFERENCES writers(id)
);