INSERT INTO task (
    summary,
    jira_id,
    description,
    complexity
) VALUES (
    "Sample Summary",
    "GTMP-6164",
    "simple description",
    10
);

INSERT INTO work_hour (issue, start_time, end_time)
VALUES ('GTMP-6164', '2024-07-01 09:00:00', '2024-07-01 17:00:00');

INSERT INTO work_hour (issue, start_time, end_time)
VALUES ('GTMP-6164', '2024-07-02 10:00:00', '2024-07-02 18:00:00');

INSERT INTO work_hour (issue, start_time, end_time)
VALUES ('GTMP-6164', '2024-07-03 08:00:00', '2024-07-03 16:00:00');

 -- rm brother.db && sqlite3 brother.db < sql/ddl.sql && sqlite3 brother.db < sql/sample.sql
