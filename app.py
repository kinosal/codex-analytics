"""Streamlit app to analyze data with English language commands."""

# Import from standard library
import os
import textwrap

# Import from 3rd party libraries
import streamlit as st
import openai

# Assign OpenAI API key from environment variable or streamlit secrets dict
openai.api_key = os.getenv("OPENAI_API_KEY") or st.secrets["OPENAI_API_KEY"]


def openai_call(prompt: str, stop: str = None) -> str:
    """Call OpenAI Codex with text prompt.
    Args:
        prompt: text prompt
        stop: stop sequence to interrupt further token generation
    Return: predicted response text
    """
    kwargs = {
        "engine": "davinci-codex",
        "prompt": prompt,
        "max_tokens": 64,
        "temperature": 0,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "best_of": 1
    }
    if stop:
        kwargs["stop"] = stop
    response = openai.Completion.create(**kwargs)
    print(response)
    return response["choices"][0]["text"]


####

# Page start

# Sidebar select
selectbox = st.sidebar.selectbox(
    "Select the type of translation",
    ("English to SQL", "English to Pandas")
)

st.title(selectbox)

# Placeholders
if selectbox == "English to SQL":
    table_name_label = "Table name"
elif selectbox == "English to Pandas":
    table_name_label = "DataFrame name"
table_name = st.text_input(label=table_name_label, value="traffic")
column_names = st.text_input(
    label="Column names (comma-separated; optionally specify data types in parentheses)",
    value="url (string), event (string), country (string)",
)
statement = st.text_input(
    label="English text prompt/query statement",
    value="Count the number of pageview events by url for urls with at least 10 pageviews"
)

if statement:
    if selectbox == "English to SQL":
        prompt = f'''
        """
        The table "{table_name}" contains the following colums: {column_names}
        """

        # {statement}
        sql = """

        '''

        st.header("SQL statement")
        st.text(openai_call(textwrap.dedent(prompt), '"""'))

    elif selectbox == "English to Pandas":
        prompt = f'''
        """
        The Pandas DataFrame "{table_name}" contains the following colums: {column_names}
        """

        # {statement}
        {table_name}.'''

        st.header("Pandas method")
        st.text(
            table_name + "." + openai_call(textwrap.dedent(prompt), "\n")
        )
