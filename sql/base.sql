CREATE TABLE IF NOT EXISTS Post(
    Post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Post_Name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Services(
    Service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Service_Name VARCHAR(255) NOT NULL,
    Service_Price INTEGER NOT NULL,
    Description_Service VARCHAR(255)NOT NULL
);

CREATE TABLE IF NOT EXISTS Client(
    Client_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Client_Name VARCHAR(255)NOT NULL,
    Client_Address VARCHAR(255) NOT NULL,
    Client_Telephone_Number VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS User(
    User_id INTEGER PRIMARY KEY AUTOINCREMENT,
    User_Name VARCHAR(255)NOT NULL,
    User_Password VARCHAR(255) NOT NULL,
    User_Telephone_Number VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Workers(
    Workers_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Post_id INTEGER NOT NULL,
    Worker_Name VARCHAR(255) NOT NULL,
    Worker_Surname VARCHAR(255)NOT NULL,
    Worker_Telephone_Number VARCHAR(100) NOT NULL,
    FOREIGN KEY(Post_id) REFERENCES Post(Post_id)
);

CREATE TABLE IF NOT EXISTS Visits(
    Visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Client_id INTEGER NOT NULL,
    Service_id INTEGER NOT NULL,
    Worker_id INTEGER NOT NULL,
    DateTime DateTime NOT NULL,
    FOREIGN KEY(Client_id) REFERENCES Client(Client_Id),
    FOREIGN KEY(Service_id) REFERENCES Services(Service_id),
    FOREIGN KEY(Worker_id) REFERENCES  Workers(Workers_id)
);

CREATE TABLE IF NOT EXISTS The_day_of_the_visit(
    The_day_of_the_visit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Visit_id INTEGER NOT NULL,
    Client_id INTEGER NOT NULL,
    Service_id INTEGER NOT NULL,
    Workers_id INTEGER NOT NULL,
    Performing_the_service INTEGER NOT NULL,
    FOREIGN KEY(Visit_id)REFERENCES Visits(Visit_id),
    FOREIGN KEY(Client_id)REFERENCES Client(Client_id),
    FOREIGN KEY (Service_id) REFERENCES Services(Service_id),
    FOREIGN KEY (Workers_id) REFERENCES Workers(Workers_id)
);