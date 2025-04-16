CREATE DATABASE IF NOT EXISTS unap;
USE unap;

CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    grado VARCHAR(20) NOT NULL,
    seccion VARCHAR(10) NOT NULL,
    edad INT NOT NULL
);

INSERT INTO estudiantes (nombre, grado, seccion, edad) VALUES
('Ana López', '1°', 'A', 6),
('Carlos Pérez', '2°', 'B', 7),
('María García', '3°', 'A', 8),
('José Ramírez', '4°', 'C', 9),
('Lucía Torres', '5°', 'B', 10),
('Pedro Quispe', '6°', 'A', 11),
('Diana Huamán', '1°', 'C', 6),
('Luis Salas', '2°', 'A', 7),
('Valeria Cruz', '3°', 'B', 8),
('Diego Medina', '4°', 'A', 9);
