-- Display the column information for the table first_table in the specified database
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.columns
WHERE table_name = 'first_table' AND table_schema = DATABASE();
