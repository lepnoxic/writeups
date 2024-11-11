-- Create a table for spaceship equipment
CREATE TABLE spaceship_equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_name VARCHAR(255) NOT NULL
);

-- Insert equipment names into the table
INSERT INTO spaceship_equipment (equipment_name)
VALUES
    ('Engine'),
    ('Navigation System'),
    ('Life Support'),
    ('Weapons System'),
    ('Communication System'),
    ('Shields'),
    ('Fuel Tanks');

-- Create a table for critical information
CREATE TABLE critical_information (
    info_id INT AUTO_INCREMENT PRIMARY KEY,
    info_text TEXT NOT NULL
);

-- Insert critical information into the table
INSERT INTO critical_information (info_text)
VALUES 
    ('sctf{passw0rd_cr4ck}'),
    ('sctf{p@ssw0rd_cr4ck}'),
    ('sctf{password_cr4ck}'),
    ('sctf{p@ssw0rd_h@ck}'),
    ('sctf{p@ssw0rd_hack}'),
    ('sctf{Pa$$w0rd_Cr4ck}'),
    ('sctf{P@$$W0rd_Cr4ck}'),
    ('sctf{P@ssw0rd_H@ck}'),
    ('sctf{p@ssW0rd_Cr4ck}'),
    ('sctf{P@ssw0rd_Hack}');

-- Retrieve equipment names
SELECT * FROM spaceship_equipment;

-- Retrieve critical information
SELECT info_text FROM critical_information;
