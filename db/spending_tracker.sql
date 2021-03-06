DROP TABLE transactions;
DROP TABLE users;
DROP TABLE tags;
DROP TABLE merchants; 

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    wallet FLOAT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    tag_type VARCHAR(255)
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    date DATE,
    time TIME,
    merchant_id INT REFERENCES merchants(id),
    amount FLOAT,
    tag_id INT REFERENCES tags(id)
);