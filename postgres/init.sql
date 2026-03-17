-- we separate the db for 2 reasons: 1) if the superset db gets corrupted, 
-- we can easily drop it and recreate it without affecting the telephony_db.
-- 2) it allows us to have different users with different permissions for each database, which can enhance security and data management.

-- superset is a BI we will use to build graphs. this tool needs its own db to store its metadata,
-- such as dashboards, charts, and user information. By having a separate database for superset,
-- we can ensure that the data is organized and managed efficiently without interfering with the telephony data.
CREATE DATABASE superset_db;

-- that's the heart db. here we will store all the data we get from the Cisco servers.
-- This database will be used to store the telephony data, such as call logs, performance metrics, and other relevant information.
-- By keeping this data in a separate database, we can optimize it for the specific needs of our telephony application and ensure that it is secure and well-managed.
CREATE DATABASE telephony_db;