# GPT3 SQL Query Example

## Example 1

What would you like to know? how many people do we have?

SQL Query: SELECT COUNT(*) FROM Employees;

Answer from database:((84,),)

Response:  We have 84 employees.

## Example 2

What would you like to know? how many people have HR in their job title?

SQL Query: SELECT COUNT(*) FROM Employees WHERE JobTitle LIKE '%HR%';

Answer from database:((2,),)

Response:  We found 2 employees with HR in their job title.