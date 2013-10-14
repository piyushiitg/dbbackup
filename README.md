dbbackup
========

Automated databases backup using S3 Api


We need to take database(postgresql) backup from production and store into Amazon S3.
While prod pull remove database from staging and restore database from S3.


This way we can synchronize prod and staging databases.
