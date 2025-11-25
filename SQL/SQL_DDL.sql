-- CREATE DATABASE CompanyDB;

-- Let's create a database to represent a company.


-- Schema are like folders or objects within the database to organize tables and other database objects.
-- CREATE SCHEMA IF NOT EXISTS hr;
-- CREATE SCHEMA IF NOT EXISTS audit;

-- DDL commands allow us to define the structure of our database objects.
-- CREATE, ALTER, DROP, TRUNCATE, RENAME are all DDL commands.

-- Let's create a table with some constraints.

CREATE TABLE IF NOT EXISTS hr.departments ( -- Column name and data type
    -- column_name data_type constraints
    department_id SERIAL PRIMARY KEY, -- auto-incrementing unique identifier
    department_name VARCHAR(100) NOT NULL UNIQUE,
    budget NUMERIC(10, 2) DEFAULT 10000.00, -- setting default value
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- set time of creation
);

CREATE TABLE IF NOT EXISTS hr.employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary NUMERIC(10, 2) CHECK (salary >= 30000), -- salary must be positive
    department_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_employee_department
    FOREIGN KEY (department_id) REFERENCES hr.departments(department_id)

    -- We can tell the database how to handle deletions or updates in the referenced table {FK}

    ON DELETE SET NULL -- If a department is deleted, set the department_id {FK} to NULL, preserving referential integrity
    ON UPDATE CASCADE -- If a department_id {FK} is updated, update it in employees table as well.

);

CREATE TABLE IF NOT EXISTS audit.employee_log (
    log_id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    ACTION VARCHAR(10) NOT NULL CHECK (ACTION IN ('INSERT', 'UPDATE', 'DELETE')), -- ACTION must be one of these three
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT -- TEXT is like a larger VARCHAR, can technically hold a 1GB string
);

-- DML - Data Manipulation Language commands allow us to manipulate the data within our tables.
-- INSERT, UPDATE, DELETE, SELECT are all DML commands.

-- Inserting data into departments table
-- INSERT INTO hr.departments (department_name) VALUES ('Sales');

--INSERT INTO hr.employees (name, salary, department_id) VALUES 
--('Alice Johnson', 60000, 1),
--('Bob Smith', 55000, 1),
--('Charlie Brown', 70000, NULL); -- department_id is NULL

SELECT e.employee_id, e.name, d.department_name, d.department_id
FROM hr.employees e
JOIN hr.departments d ON e.department_id = d.department_id;


-- Update department id for an employee
UPDATE hr.departments
SET department_id = 10 -- New department ID
WHERE department_id = 1; -- Some contraint to identify which rows/columns to update
-- This can be done because of the ON UPDATE CASCADE constraint on the foreign key in employees table


-- Deleting a department
DELETE FROM hr.departments
WHERE department_id = 10; -- Deleting department with ID 10
-- This will set the department_id in employees table to NULL for employees in that department because of the ON DELETE SET NULL constraint

SELECT * FROM hr.employees;

-- Let's create a trigger. They are user-defined functions that return a trigger type.

CREATE OR REPLACE FUNCTION hr.log_employee_insert()
RETURNS TRIGGER 
LANGUAGE plpgsql
AS $$
BEGIN

    INSERT INTO audit.employee_log (employee_id, ACTION, details)
    VALUES (NEW.employee_id, 'INSERT', format('New employee: %%', NEW.name));
    RETURN NEW; -- For INSERT triggers, we return the new row

END;
$$;

-- Now we create the trigger that will call this function after an INSERT on employees table
CREATE OR REPLACE TRIGGER employee_insert_audit_trigger
AFTER INSERT ON hr.employees -- when and where the trigger fires
FOR EACH ROW -- frequency of trigger execution
EXECUTE FUNCTION hr.log_employee_insert(); -- function to execute

-- Testing the trigger by inserting a new employee
INSERT INTO hr.employees (name, salary, department_id) VALUES ('Diana Prince', 80000, NULL);

SELECT * FROM audit.employee_log;