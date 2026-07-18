CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    text TEXT,
    owner_id INTEGER,
    FOREIGN KEY (owner_id) REFERENCES users (id)
);
