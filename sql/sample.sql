INSERT INTO task (
    summary,
    jira_id,
    description,
    complexity,
    is_in_sprint,
) VALUES (
    "Sample Summary",
    "GTMP-6164",
    "simple description",
    10,
    1,
), (
    "Second task",
    "GTMP-7174",
    "simple description",
    20,
    0
);

INSERT INTO work_hour (task, start_time, end_time)
VALUES (1, '2024-07-01 09:00:00', '2024-07-01 17:00:00');

INSERT INTO work_hour (task, start_time, end_time)
VALUES (1, '2024-07-02 10:00:00', '2024-07-02 18:00:00');

INSERT INTO work_hour (task, start_time, end_time)
VALUES (1, '2024-07-03 08:00:00', null);


 -- rm brother.db && sqlite3 brother.db < sql/ddl.sql && sqlite3 brother.db < sql/sample.sql
