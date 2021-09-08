# Data Analytics with OpenAI GPT-3 Codex

Live version of this app at
https://share.streamlit.io/kinosal/codex-analytics/app.py

## Description

This [Streamlit](https://streamlit.io) mini-app translates a statement in plain
English into [SQL](https://en.wikipedia.org/wiki/SQL) or
[Python](https://www.python.org) [Pandas](https://pandas.pydata.org)
using OpenAI's GPT-3 based [Codex](https://openai.com/blog/openai-codex/) model,
allowing anyone not familiar with those languages/libraries to perform simple data
analysis tasks with SQL databases or Pandas DataFrames.

The app generates a text prompt describing the table or DataFrame and
adding a comment with the provided query statement from a few user inputs. The
prompt is then sent to the OpenAI API which - using the GPT-3 davinci-codex
engine that has been trained on a lot of publicly available text content
including open-source code - predicts the next likely to be used tokens
and thus generates the translated statement.

This is not perfect and does occasionally result in false statements with
a wrong syntax (less frequent as far as I could observe)
and/or unexpected behavior (more frequent). In my experiments the
translation to SQL also yielded better results than Pandas.

## Contribution

I hope this will be of value to people learning, wanting or needing
to use SQL and/or Pandas for data analytics as well as for people trying
to understand GPT-3's and specifically Codex's capabilities in this field.

Please reach out to me at nikolas@schriefer.me with any feedback -
especially suggestions to improve this - or questions you might have.
