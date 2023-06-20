# GPT-3 SQL Query Example

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

# How to run this on [Google Cloud Shell](https://shell.cloud.google.com/)

## 1: Set OpenAI environment variable with your API Key

`export OPENAI_API_KEY=sk-XXXXXXXXXX`

## 2: Run MySQL Container

`01-run-mysql.sh`

## 3: Populate MySQL with Data

`02-add-data.sh`

## 4: Install Python dependencies

`pip3 install -r requirements.txt`

## 5: Run Python Script

`python3 03-query.py`

## To Do

* better error handling
* move to GPT 3.5/4 to reduce hallucinations