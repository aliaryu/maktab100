-- Hospital DataBase Queries

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    fullname VARCHAR (100) NOT NULL,
    email VARCHAR (100) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR (10) NOT NULL,
    username VARCHAR (100) UNIQUE NOT NULL,
    password VARCHAR (255) NOT NULL,
    role VARCHAR (50) NOT NULL,
    superuser BOOLEAN DEFAULT FALSE NOT NULL,
    active BOOLEAN DEFAULT FALSE NOT NULL,
    delete BOOLEAN DEFAULT FALSE NOT NULL
    -- phone, address, etc ...
);

CREATE TABLE admins (
    admin_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users (user_id),
    position VARCHAR (100) NOT NULL
    -- permission, group, etc ...
);

CREATE TABLE doctors (
    doctor_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users (user_id),
    specialization VARCHAR (100) NOT NULL,
    medical_license_number INT UNIQUE NOT NULL
    -- education, university, etc ...
);

CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users (user_id),
    medical_record_number INT UNIQUE NOT NULL
    -- blood type, allergy, etc ...
);