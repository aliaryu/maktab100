-- Hospital DataBase Queries --

CREATE TABLE users (
    user_id BIGSERIAL PRIMARY KEY,
    fullname VARCHAR (100) NOT NULL,
    email VARCHAR (100) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    gender VARCHAR (10) NOT NULL,
    username VARCHAR (100) UNIQUE NOT NULL,
    password BYTEA NOT NULL,
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
    appointment_id BIGINT REFERENCES appointments (appointment_id) UNIQUE,
    patient_id BIGINT REFERENCES patients (patient_id),
    paid BOOLEAN DEFAULT FALSE NOT NULL,
    paid_date DATE NOT NULL
    -- payment methods, bank number, etc ...
    -- OR: create payment table
);

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('ali aryu', 'aliaryu@yahoo.com', '1997-4-22', 'male', 'aliaryu', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'admin', TRUE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (1, 'super user operator'); -- This superuser is necessary


-- Initial Queries For Testing --

INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('rostam dastan', 'rostam@gmail.com', '1980-08-17', 'male', 'rostam', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'admin', FALSE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (2, 'security');
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('artmis daryasalar', 'artmis@gmail.com', '1996-04-03', 'female', 'artmis', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'admin', FALSE, TRUE, FALSE);
INSERT INTO admins (user_id, position) VALUES (3, 'financial');


INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('hasti mehraban', 'hasti@gmail.com', '2003-02-28', 'female', 'hasti', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'doctor', FALSE, TRUE, FALSE);
INSERT INTO doctors (user_id, specialization, medical_license_number) VALUES (4, 'beauty', 1111111111);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('majid samii', 'majid@gmail.com', '1965-05-15', 'male', 'majid', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'doctor', FALSE, TRUE, FALSE);
INSERT INTO doctors (user_id, specialization, medical_license_number) VALUES (5, 'cardiovascular', 2222222222);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('nikan hadadi', 'nikan@gmail.com', '1991-10-11', 'male', 'nikan', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'doctor', FALSE, TRUE, FALSE);
INSERT INTO doctors (user_id, specialization, medical_license_number) VALUES (6, 'otorhinolaryngology', 3333333333);


INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '09:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '09:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '10:0:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '10:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '11:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '11:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '14:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '14:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '15:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '15:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '16:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '1 day', '16:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '09:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '09:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '10:0:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '10:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '11:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '11:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '14:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '14:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '15:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '15:30:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '16:00:00', 100.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (1, CURRENT_DATE + INTERVAL '2 day', '16:30:00', 100.00);

INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '1 day', '09:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '1 day', '10:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '1 day', '11:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '1 day', '14:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '1 day', '15:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '1 day', '16:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '2 day', '09:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '2 day', '10:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '2 day', '11:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '2 day', '14:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '2 day', '15:00:00', 70.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (2, CURRENT_DATE + INTERVAL '2 day', '16:00:00', 70.00);

INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '09:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '09:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '09:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '09:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '10:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '10:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '10:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '10:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '11:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '11:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '11:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '11:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '14:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '14:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '14:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '14:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '15:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '15:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '15:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '15:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '16:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '16:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '16:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '1 day', '16:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '09:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '09:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '09:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '09:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '10:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '10:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '10:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '10:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '11:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '11:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '11:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '11:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '14:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '14:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '14:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '14:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '15:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '15:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '15:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '15:45:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '16:00:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '16:15:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '16:30:00', 30.00);
INSERT INTO appointments (doctor_id, appointment_date, appointment_time, cost)
VALUES (3, CURRENT_DATE + INTERVAL '2 day', '16:45:00', 30.00);


INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('arvin kamari', 'b1@gmail.com', '2001-01-01', 'male', 'bimar1', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (7, 1111110);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('mahsa fadakar', 'b2@gmail.com', '2002-02-02', 'female', 'bimar2', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (8, 2222220);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('amin baqeri', 'b3@gmail.com', '2003-03-03', 'male', 'bimar3', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (9, 3333330);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('zoha rashti', 'b4@gmail.com', '2004-04-04', 'female', 'bimar4', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (10, 4444440);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('ali musa zade', 'b5@gmail.com', '2005-05-05', 'male', 'bimar5', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (11, 5555550);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('poneh karimlar', 'b6@gmail.com', '2006-06-06', 'female', 'bimar6', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (12, 6666660);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('nima niazi', 'b7@gmail.com', '2007-07-07', 'male', 'bimar7', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (13, 7777770);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('maryam khalaj', 'b8@gmail.com', '2008-08-08', 'female', 'bimar8', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (14, 8888880);
INSERT INTO users (fullname, email, date_of_birth, gender, username, password, role, superuser, active, delete)
VALUES ('sajad rostam zadi', 'b9@gmail.com', '2009-09-09', 'male', 'bimar9', '$2b$12$0KdMmFngvGhqBI0CMM/Lp.Mjudl1ncglUgFaTH88TCV6aqYbUrpYq', 'patient', FALSE, TRUE, FALSE);
INSERT INTO patients (user_id, medical_record_number) VALUES (15, 9999990);


INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (1,  1, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 1;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (25, 2, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 25;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (27, 3, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 27;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (37, 4, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 37;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (38, 5, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 38;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (40, 6, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 40;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (54, 7, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 54;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (55, 8, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 55;
INSERT INTO visits (appointment_id, patient_id, paid, paid_date) VALUES (56, 9, true, CURRENT_DATE);
UPDATE appointments SET available = false WHERE appointment_id = 56;
