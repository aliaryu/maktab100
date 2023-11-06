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
VALUES ('rostam dastan', 'rostam@gmail.com', '1980-08-17', 'male', 'rostam', '1', 'admin', FALSE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (2, 'security');

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('artmis daryasalar', 'artmis@gmail.com', '1996-04-03', 'female', 'artmis', '1', 'admin', FALSE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (3, 'financial');


INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('hasti mehraban', 'hasti@gmail.com', '2003-02-28', 'female', 'hasti', '1', 'doctor', FALSE, TRUE, FALSE);
INSERT INTO doctors (user_id, specialization, medical_license_number) VALUES (4, 'beauty', 1111111111);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('majid samii', 'majid@gmail.com', '1965-05-15', 'male', 'majid', '1', 'doctor', FALSE, TRUE, FALSE);
INSERT INTO doctors (user_id, specialization, medical_license_number) VALUES (5, 'cardiovascular', 2222222222);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('nikan hadadi', 'nikan@gmail.com', '1991-10-11', 'male', 'nikan', '1', 'doctor', FALSE, TRUE, FALSE);
INSERT INTO doctors (user_id, specialization, medical_license_number) VALUES (6, 'otorhinolaryngology', 3333333333);


INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 1', 'b1@gmail.com', '2001-01-01', 'male', 'bimar1', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (7, 1111110);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 2', 'b2@gmail.com', '2002-02-02', 'female', 'bimar2', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (8, 2222220);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 3', 'b3@gmail.com', '2003-03-03', 'male', 'bimar3', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (9, 3333330);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 4', 'b4@gmail.com', '2004-04-04', 'female', 'bimar4', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (10, 4444440);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 5', 'b5@gmail.com', '2005-05-05', 'male', 'bimar5', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (11, 5555550);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 6', 'b6@gmail.com', '2006-06-06', 'female', 'bimar6', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (12, 6666660);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 7', 'b7@gmail.com', '2007-07-07', 'male', 'bimar7', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (13, 7777770);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 8', 'b8@gmail.com', '2008-08-08', 'female', 'bimar8', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (14, 8888880);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('bimar 9', 'b9@gmail.com', '2009-09-09', 'male', 'bimar9', '1', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (15, 9999990);









