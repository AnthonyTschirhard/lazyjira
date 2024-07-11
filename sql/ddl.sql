CREATE TABLE project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    project TEXT NOT NULL,
    status TEXT CHECK( status IN ('ToDo','InProgress','Done') ) NOT NULL DEFAULT 'ToDo',
    jira_id TEXT,
    description TEXT,
    complexity INTEGER,
    parent INTEGER,
    created_date TIMESTAMP,
    updated_date TIMESTAMP,
    due_date TIMESTAMP,
    priority TEXT CHECK( priority IN ('Low','Medium','High') ) NOT NULL DEFAULT 'Medium'
);

CREATE TABLE work_hour (
    issue TEXT NOT NULL,
    start_time TIMESTAMP,
    end_time TIMESTAMP,

    PRIMARY KEY(issue, start_time, end_time)
);

CREATE TABLE time_allocation (
    project TEXT NOT NULL,
    period TIMESTAMP NOT NULL,
    allocated_time INTEGER NOT NULL,

    PRIMARY KEY(project, period)
);

INSERT INTO task (name, project) VALUES ('GTMP-1', 'Project A');
INSERT INTO task (name, project) VALUES ('GTMP-2', 'Project B');
INSERT INTO task (name, project) VALUES ('GTMP-3', 'Project C');

INSERT INTO work_hour (issue, start_time, end_time)
VALUES ('GTMP-1', '2024-07-01 09:00:00', '2024-07-01 17:00:00');

INSERT INTO work_hour (issue, start_time, end_time)
VALUES ('GTMP-1', '2024-07-02 10:00:00', '2024-07-02 18:00:00');

INSERT INTO work_hour (issue, start_time, end_time)
VALUES ('GTMP-2', '2024-07-03 08:00:00', '2024-07-03 16:00:00');
