CREATE TABLE restaurant (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(15),
    opening_hours VARCHAR(255),
    owner_id INT
);

CREATE TABLE menu (
    menu_id INT PRIMARY KEY,
    restaurant_id INT,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2)
);

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    name VARCHAR(255),
    contact_name VARCHAR(255),
    contact_email VARCHAR(255),
    phone_number VARCHAR(15)
);

CREATE TABLE restaurant_table (
    table_id INT PRIMARY KEY,
    restaurant_id INT,
    table_number INT,
    capacity INT
);

CREATE TABLE workers (
    worker_id INT PRIMARY KEY,
    restaurant_id INT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender_id INT,
    position VARCHAR(255),
    salary DECIMAL(10, 2)
);

CREATE TABLE gender (
    gender_id INT PRIMARY KEY,
    name VARCHAR(10)
);

CREATE TABLE administrator (
    admin_id INT PRIMARY KEY,
    worker_id INT,
    hire_date DATE,
    admin_level VARCHAR(255)
);

CREATE TABLE waiter (
    waiter_id INT PRIMARY KEY,
    worker_id INT,
    hire_date DATE
);

CREATE TABLE janitor (
    janitor_id INT PRIMARY KEY,
    worker_id INT,
    hire_date DATE
);

CREATE TABLE bartender (
    bartender_id INT PRIMARY KEY,
    worker_id INT,
    hire_date DATE
);

CREATE TABLE chef (
    chef_id INT PRIMARY KEY,
    worker_id INT,
    hire_date DATE
);

CREATE TABLE dish (
    dish_id INT PRIMARY KEY,
    menu_id INT,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    chef_id INT
);

CREATE TABLE drinks (
    drink_id INT PRIMARY KEY,
    menu_id INT,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    supplier_id INT,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    quantity_available INT
);


-- Add foreign key to Restaurant table
ALTER TABLE Restaurant
ADD CONSTRAINT fk_owner_id
FOREIGN KEY (owner_id)
REFERENCES Administrator(admin_id);

-- Add foreign key to Menu table
ALTER TABLE Menu
ADD CONSTRAINT fk_restaurant_id
FOREIGN KEY (restaurant_id)
REFERENCES Restaurant(restaurant_id);

-- Add foreign key to Restaurant_Table table
ALTER TABLE Restaurant_Table
ADD CONSTRAINT fk_restaurant_id
FOREIGN KEY (restaurant_id)
REFERENCES Restaurant(restaurant_id);

-- Add foreign key to Workers table
ALTER TABLE Workers
ADD CONSTRAINT fk_restaurant_id
FOREIGN KEY (restaurant_id)
REFERENCES Restaurant(restaurant_id);

ALTER TABLE Workers
ADD CONSTRAINT fk_gender_id
FOREIGN KEY (gender_id)
REFERENCES Gender(gender_id);

-- Add foreign key to Administrator table
ALTER TABLE Administrator
ADD CONSTRAINT fk_worker_id
FOREIGN KEY (worker_id)
REFERENCES Workers(worker_id);

-- Add foreign key to Waiter table
ALTER TABLE Waiter
ADD CONSTRAINT fk_worker_id
FOREIGN KEY (worker_id)
REFERENCES Workers(worker_id);

-- Add foreign key to Janitor table
ALTER TABLE Janitor
ADD CONSTRAINT fk_worker_id
FOREIGN KEY (worker_id)
REFERENCES Workers(worker_id);

-- Add foreign key to Bartender table
ALTER TABLE Bartender
ADD CONSTRAINT fk_worker_id
FOREIGN KEY (worker_id)
REFERENCES Workers(worker_id);

-- Add foreign key to Chef table
ALTER TABLE Chef
ADD CONSTRAINT fk_worker_id
FOREIGN KEY (worker_id)
REFERENCES Workers(worker_id);

-- Add foreign key to Dish table
ALTER TABLE Dish
ADD CONSTRAINT fk_menu_id
FOREIGN KEY (menu_id)
REFERENCES Menu(menu_id);

ALTER TABLE Dish
ADD CONSTRAINT fk_chef_id
FOREIGN KEY (chef_id)
REFERENCES Chef(chef_id);

-- Add foreign key to Drinks table
ALTER TABLE Drinks
ADD CONSTRAINT fk_menu_id
FOREIGN KEY (menu_id)
REFERENCES Menu(menu_id);

-- Add foreign key to Products table
ALTER TABLE Products
ADD CONSTRAINT fk_supplier_id
FOREIGN KEY (supplier_id)
REFERENCES Suppliers(supplier_id);
