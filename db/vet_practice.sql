DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE pets(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    photo VARCHAR(255),
    dob VARCHAR(255),
    type VARCHAR(255),
    owner VARCHAR(255),
    owner_tel VARCHAR(255),
    owner_email VARCHAR(255),
    notes TEXT,
    vet_id INT REFERENCES vets(id)
);
    
