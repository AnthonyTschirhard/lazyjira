CREATE TABLE project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary TEXT NOT NULL,
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
