-- Hospital DataBase Queries --

CREATE TABLE users (
    user_id BIGSERIAL PRIMARY KEY,
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
    -- OR: create role table
);

CREATE TABLE admins (
    admin_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users (user_id) UNIQUE,
    position VARCHAR (100) NOT NULL
    -- permission, group, etc ...
);

CREATE TABLE doctors (
    doctor_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users (user_id) UNIQUE,
    specialization VARCHAR (100) NOT NULL,
    medical_license_number BIGINT UNIQUE NOT NULL
    -- education, university, etc ...
);

CREATE TABLE patients (
    patient_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users (user_id),
    medical_record_number BIGINT UNIQUE NOT NULL
    -- blood type, allergy, etc ...
);

CREATE TABLE appointments (
    appointment_id BIGSERIAL PRIMARY KEY,
    doctor_id BIGINT REFERENCES doctors (doctor_id),
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    available BOOLEAN DEFAULT TRUE NOT NULL
    -- room number, cancel bool, etc ...
);

CREATE TABLE visits (
    visit_id BIGSERIAL PRIMARY KEY,
    appointment_id BIGINT REFERENCES appointments (appointment_id),
    patient_id BIGINT REFERENCES patients (patient_id),
    paid BOOLEAN DEFAULT FALSE NOT NULL
    -- payment methods, bank number, etc ...
    -- OR: create payment table
);


-- Initial Queries For Testing --

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('ali aryu', 'aliaryu@yahoo.com', '1997-4-22', 'male', 'aliaryu', '1', 'admin', TRUE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (1, 'super user operator');

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('rostam dastan', 'rostam@dastan.com', '1980-08-17', 'male', 'rostam', '1', 'admin', FALSE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (2, 'security');

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('artmis daryasalar', 'artmis@daryasalar.com', '1996-04-03', 'female', 'artmis', '1', 'admin', FALSE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (3, 'financial');











