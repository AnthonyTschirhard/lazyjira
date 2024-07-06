CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    project TEXT
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE work_hours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    issue TEXT NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP
);

CREATE TABLE time_allocation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project TEXT NOT NULL,
    period TIMESTAMP NOT NULL,
    allocated_time INTEGER NOT NULL
);

INSERT INTO tasks (name, project) VALUES ('GTMP-1', 'Project A');
INSERT INTO tasks (name, project) VALUES ('GTMP-2', 'Project B');
INSERT INTO tasks (name, project) VALUES ('GTMP-3', 'Project C');

INSERT INTO work_hours (issue, start_time, end_time)
VALUES ('GTMP-1', '2024-07-01 09:00:00', '2024-07-01 17:00:00');

INSERT INTO work_hours (issue, start_time, end_time)
VALUES ('GTMP-1', '2024-07-02 10:00:00', '2024-07-02 18:00:00');

INSERT INTO work_hours (issue, start_time, end_time)
VALUES ('GTMP-2', '2024-07-03 08:00:00', '2024-07-03 16:00:00');
