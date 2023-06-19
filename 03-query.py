import pymysql
import os
import openai
import sys

mysql_host="127.0.0.1"
mysql_port=3306
mysql_password="openai"


openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(user_question):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="This MySQL table holds the following employee data:\n\n1: Employee Name\n2: Birthday (year)\n3: Employee Grade (1 to 10)\n4: Phone number\n5: Job Title\n\n CREATE TABLE Employees (\n  EmployeeName VARCHAR(255),\n  Birthday YEAR,\n  EmployeeGrade INTEGER UNSIGNED,\n  PhoneNumber VARCHAR(14),\n  JobTitle VARCHAR(255) \n );\n\ndata looks like this:\n\n  ('John Smith', 1985, 8, '123-456-7890', 'Software Engineer'),\n  ('Allison Jones', 1987, 7, '123-456-7891', 'Product Manager'),\n  ('Tyler Williams', 1982, 9, '123-456-7892', 'Software Architect'),\n  ('Emma Brown', 1981, 6, '123-456-7893', 'Software Developer'),\n  ('Michael Davis', 1990, 8, '123-456-7894', 'Software Test Engineer'),\n  ('Emily Miller', 1980, 7, '123-456-7895', 'Business Analyst'),\n\n---\n\nWrite SQL query statements based on natural language from user input. If the question does not make any sense, please output UNKNOWN. Make sure the SQL statement ends with a semicolon.\n\nUser: What is David Brown's email address?\nSELECT Email FROM Employees WHERE EmployeeName='David Brown';\n\nUser: How many employees do we have at the company?\nSELECT COUNT(*) FROM Employees;\n\nUser: What is the average age of our employees?\nSELECT AVG(YEAR(CURDATE()-Birthday)) FROM Employees;\n\nUser: How many unique job titles do we have?\nSQL: SELECT COUNT(DISTINCT(JobTitle)) FROM Employees;\n\nUser: " + user_question,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return(response["choices"][0]["text"])

def execute_mysql_query(query):
    try:
        # Create a connection to the MySQL database
        connection = pymysql.connect(
            host=mysql_host,
            port=mysql_port,
            user='root',  # Replace with your MySQL username if necessary
            password=mysql_password,
            database='empdata'  # Replace with your database name
        )

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Fetch all the rows returned by the query
        result = cursor.fetchall()

        # Commit the transaction
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Return the result
        return result

    except pymysql.Error as error:
        print(f"Error connecting to MySQL database: {error}")
        return None

# print(execute_mysql_query("select * from Employees;"))

def craft_response(uquery, sqlstatement, sqlres):

    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt="A MySQL table holds the following employee data:\n\n1: Employee Name\n2: Birthday (year)\n3: Employee Grade (1 to 10)\n4: Phone number\n5: Job Title\n\n the user has asked the following question: " + uquery + "\n\nthe corresponding SQL query is: " + sqlstatement + "\nthe SQL database response is " + str(sqlres) + "\nplease respond to the users query using natural language.\n\nHere is the response to your question:",
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return(response["choices"][0]["text"])


question = input("What would you like to know? ")

sqlquery = ask_openai(question)

if sqlquery.replace("UNKNOWN", "") != sqlquery:
    print("Sorry no clue.")
    sys.exit(1)

print("SQL Query: " + sqlquery);

answer = execute_mysql_query(sqlquery);

print("Answer from database:" + str(answer));

resp = craft_response(question, sqlquery, answer);

print("Response: " + str(resp))
