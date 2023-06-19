cat create-sql-entries.sql | docker exec -i $(docker ps -q) mysql -popenai
