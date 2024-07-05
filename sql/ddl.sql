CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    project TEXT
);

CREATE TABLE work_hours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue TEXT NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP
);
