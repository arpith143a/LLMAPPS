# LLMAPPS
Hands on projects related to LLM
1. TextToSql
Functionality:
Use the template provided to include details of database,tables and relation between tables.
After running the application using streamlit run app.py.
Upload option is available to upload your custom prompt template
Select the templated available
Provide the text which you need query for.
Query is formulated.
Modify the code in app3.py to connect to the db which you have mentioned in the Prompt template.
Along with the query generated output from db will also be printed for validating your requirement

Files:
app.py = has the code for calling gemini model and generate output, has the code for UI using streamlit
Templates = This directory has the format of the Prompt Template that needs to be put into the app.py
requirements.txt= This file has the libraries required for this app
sql.py and sql2.py= These are python files for creating sample student and university databases, their tables and inserting sample data
student.db and university.db= database files created

2. TripAdvisor
Functionality:
To generate trip itenary based on user choices like budget type, number of days planned, food choices,activity choices,local transportation choice, stay type etc.
After running the application using streamlit run app.py
Fill out the fields.
After submitting, you will get detailed formatted itenary for your Trip.

Files:
app.py = has the prompt that takes the input field requied for generating itenary, code for calling gemnini model and generate output, has the code for UI using streamlit
requirements.txt= This file has the libraries required for this app
PromptTemplate= Prompt used in the code

