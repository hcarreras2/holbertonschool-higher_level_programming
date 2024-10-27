-- List all privileges for the users user_0d_1 and user_0d_2
SELECT * 
FROM information_schema.USER_PRIVILEGES 
WHERE GRANTEE IN ('user_0d_1', 'user_0d_2');
