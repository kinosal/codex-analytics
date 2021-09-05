import streamlit as st
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

base_prompt = '''
"""
The table "traffic" contains the following colums: "event", "linkid", "country"
"""

'''

st.title("English to SQL")

table_name = st.text_input(label="Table name", value="traffic")
column_names = st.text_input(
    label="Column names (comma-separated)", value="linkid,event,country"
).split(",")
statement = st.text_input(
    label="English text prompt/query statement",
    value="Count the number of pageview events by linkid for linkids with at least 10 pageviews"
)

if statement:
    prompt = f'''
    """
    The table "{table_name}" contains the following colums: {str(column_names)}
    """

    # {statement}
    sql = """

    '''

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=64,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=['"""'],
    )
    print(response)

    st.header("SQL statement")
    st.text(response["choices"][0]["text"])
