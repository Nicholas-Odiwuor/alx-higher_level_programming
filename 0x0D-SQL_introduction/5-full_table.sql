-- Script to print the full description of the table first_table

USE hbtn_0c_0; -- mysql

SELECT CONCAT('Table   Create Table                                                                         
first_table     ', CREATE_TABLE) AS 'Create Table'
FROM information_schema.TABLES
WHERE TABLE_NAME = 'first_table';
i
