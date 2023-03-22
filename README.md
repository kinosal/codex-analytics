# Data Analytics with OpenAI GPT-3 Codex

Live version of this app at
https://share.streamlit.io/kinosal/codex-analytics/app.py

## Description

This [Streamlit](https://streamlit.io) mini-app translates a statement in plain
English into [SQL](https://en.wikipedia.org/wiki/SQL) or
[Python](https://www.python.org) [Pandas](https://pandas.pydata.org)
using OpenAI's [GPT-3.5](https://platform.openai.com/docs/models/gpt-3-5) Turbo (Chat) model,
allowing anyone not familiar with those languages/libraries to perform simple data
analysis tasks with SQL databases or Pandas DataFrames.

The app generates a text prompt describing the table or DataFrame and
adding a comment with the provided query statement from a few user inputs. The
prompt is then sent to the OpenAI API which returns the next likely to be used tokens
for a possible answer and thus generates the translated statement.

## Contribution

I hope this will be of value to people learning, wanting or needing
to use SQL and/or Pandas for data analytics as well as for people trying
to understand the capabilities of GPT models in this field.

Please reach out to me at nikolas@schriefer.me with any feedback -
especially suggestions to improve this - or questions you might have.
