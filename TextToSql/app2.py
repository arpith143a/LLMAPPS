import streamlit as st
import os

from dotenv import load_dotenv
load_dotenv() #load environment variables


import sqlite3

import google.generativeai as genai

#configure AI key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load google gemini model and provide query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# function to retrieve query from sql db
def sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows 

# Function to list files in a folder
def list_files(folder_path):
    files = os.listdir(folder_path)
    return files

# Function to read the content of a text file
def read_text_file(file_path):
    f = open(file_path, "r")
    content=f.read()
    return content

def save_uploaded_file(uploaded_file, save_folder):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    file_path = os.path.join(save_folder, uploaded_file.name)
    with open(file_path, 'wb') as file:
        file.write(uploaded_file.getvalue())

    return file_path

# Streamlit app

st.set_page_config(page_title="I can retrieve any sql query")
st.header("Text to Sql Generator")
upload_document = st.checkbox("Upload a Document")

if upload_document:
    # If checkbox is selected, allow the user to upload a document
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])

    if uploaded_file:
        st.success("File uploaded successfully!")
        # Process the uploaded file as needed
        # For example, you can save it to a folder or perform further analysis
        save_folder = r"C:\Users\Arpith Paida\Documents\Projects\TextToSql\templates" 
        saved_file_path = save_uploaded_file(uploaded_file, save_folder)

        st.write(f"File saved to: {saved_file_path}")

folder_path = r"C:\Users\Arpith Paida\Documents\Projects\TextToSql\templates"  # Replace with the actual path to your documents folder
existing_files = list_files(folder_path)
print(existing_files)

selected_file = st.selectbox("Choose an existing document", existing_files, index=0)
# print(s)

st.write(f"You selected: {selected_file}")
print(folder_path+"/"+selected_file)
# Process the selected existing file as needed
# For example, you can read its content or display it
prompt_content = read_text_file(folder_path+"/"+selected_file)
print(prompt_content)
prompt=[]
prompt.append(prompt_content)

question=st.text_input("Input: ",key="input")
submit=st.button("Query result")

from tabulate import tabulate
import sqlparse

def extract_column_names(sql_query):
    parsed = sqlparse.parse(sql_query)[0]

    columns = []

    # Find the SELECT statement and extract column names
    for token in parsed.tokens:
        if isinstance(token, sqlparse.sql.IdentifierList):
            columns.extend([str(identifier).strip() for identifier in token.get_identifiers()])
        elif isinstance(token, sqlparse.sql.Identifier):
            columns.append(str(token).strip())

    return columns


if submit:
    # prompt=main()
    response=get_gemini_response(question,prompt)
    print(response)
    column_names = extract_column_names(response)
    data = sql_query(response,"university.db")
    # data = sql_query(response,"student.db")
    table = tabulate(data, column_names, tablefmt='grid')
    print(table)
    st.subheader("the response is: ")
    st.text(table)
