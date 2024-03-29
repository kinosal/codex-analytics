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
    print(prompt)
    kwargs = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    if stop:
        kwargs["stop"] = stop
    response = openai.ChatCompletion.create(**kwargs)
    print(response)
    return response["choices"][0]["message"]["content"]


####

# Page start

st.set_page_config(page_title="English to Code", page_icon="🤖")

st.title(
    "English to Code w/ [OpenAI Codex](https://openai.com/blog/openai-codex/)"
)

st.write(
    """This mini-app translates a statement in plain English into
    [SQL](https://en.wikipedia.org/wiki/SQL) or
    [Python](https://www.python.org) [Pandas](https://pandas.pydata.org)
    using OpenAI's GPT-3.5 model, allowing anyone
    not familiar with those languages/libraries to perform simple data
    analysis tasks with SQL databases or Pandas DataFrames."""
)

st.write(
    """The following inputs will generate a text prompt describing the table or
    DataFrame and adding a comment with the provided query statement. The
    prompt is then sent to the OpenAI API which - using the GPT-3.5 Turbo (Chat)
    model that has been trained on a lot of publicly available text content
    including open-source code - predicts and returns the likely to be used tokens for a
    possible answer and thus generates the translated statement."""
)

st.write(
    """I hope this will be of value to people learning, wanting or needing
    to use SQL and/or Pandas for data analytics as well as for people trying
    to understand the capabilities of GPT models in this field.
    Please reach out to me at nikolas@schriefer.me with any feedback -
    especially suggestions to improve - or questions you might
    have. You can find the code for this app on
    [GitHub](https://github.com/kinosal/codex-analytics).
    """
)

st.markdown("""---""")

selectbox = st.selectbox(
    "Select the type of translation you would like to perform",
    ("English to SQL", "English to Pandas")
)

if selectbox == "English to SQL":
    table_name_label = "Table name"
elif selectbox == "English to Pandas":
    table_name_label = "DataFrame name"

table_name = st.text_input(label=table_name_label, value="traffic")
column_names = st.text_area(
    label="Column names (comma-separated; optionally specify data types in parentheses)",
    value="url (string), event (string), country (string)",
)
statement = st.text_area(
    label="English text prompt/query statement",
    value="Count the number of pageview events by url for urls with at least 10 pageviews"
)

if statement:
    if selectbox == "English to SQL":
        prompt = textwrap.dedent(
            f'''
            """
            The database table "{table_name}" contains the following colums: {column_names}
            """

            # {statement}
            sql = """
            '''
        )
        stop = '"""'
        result_prefix = ""
        language = "sql"

    elif selectbox == "English to Pandas":
        prompt = textwrap.dedent(
            f'''
            """
            The Pandas DataFrame "{table_name}" contains the following colums: {column_names}
            """

            # {statement}
            {table_name}.'''
        )
        stop = None
        result_prefix = table_name + "."
        language = "python"

    st.markdown("""---""")
    st.header("Result")
    st.code(result_prefix + openai_call(prompt, stop), language=language)

    st.markdown("""---""")
    st.header("Prompt sent to Codex")
    st.text(prompt)
