import pymysql
mysql_host="127.0.0.1"
mysql_port=3306
mysql_password="openai"

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

print(execute_mysql_query("select * from Employees;"))