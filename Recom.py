# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os

import streamlit as st
#from components.sidebar import sidebar

#openai.api_key = os.environ["OPENAI_API_KEY"] = "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"
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai_api_key = st.secrets["OPENAI_API_KEY"]

st.header("RecomGPT - Generate Recommendation Letters with ChatGPT")

st.subheader("Your name and title")
st.markdown(
    """
    e.g., I am Dr. Vahid Behzadan, assistant professor of computer science and data science, and director of the Secure and Assured Intelligent Learning (SAIL) lab at the University of New Haven
   
    """
)
System_Content = st.text_area("Enter your name and title", max_chars=500)

st.subheader("Student/Colleague")
st.markdown(
    """
    Name of the referee, and their title/position
    e.g., Stan Smith, a student in our MS Data Science program
   
    """
)
Referee_Name = st.text_area("Name and title of the referee", max_chars=500)

st.subheader("Application or program")
st.markdown(
    """
    What is your letter for?
    e.g., for his application to the Computer Science PhD program at Yale.
   
    """
)
Referee_Target = st.text_area("Target", max_chars=500)

st.subheader("Relationship")
st.markdown(
    """
    How do you know the referee?
    e.g., Stan was a student in my Artificial Intelligence class
   
    """
)
Referee_Relationship = st.text_area("Relationship", max_chars=500)

st.subheader("Special Notes")
st.markdown(
    """
    Is there a special quality or event that you would like to note about the referee?
    e.g., Stan did well in my class.
   
    """
)
Referee_Special = st.text_area("Special Notes", max_chars=500)

query = "Write a recommendation letter for " + Referee_Name + " for " + Referee_Target + ". " + Referee_Relationship + ". " + Referee_Special + "."

if st.button("Ask"):
  if query == "":
      st.error("Please enter a question")
  with st.spinner("Generating letter..."):
      # res = query_gpt_memory(chosen_class, chosen_pdf, query)
      response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
              {"role": "system", "content": System_Content},#"You are writing a recommendation letter on behalf of Dr. Vahid Behzadan, an assistant professor of computer science and data science, and director of the Secure and Assured Intelligent Learning (SAIL) lab at the University of New Haven."},
              {"role": "user", "content": query}#"Write a recommendation letter for Stan Smith, a student in our MS Data Science program, for his application to the Computer Science PhD program at Yale. Stan was a student in my Artificial Intelligence class, and performed well."}
              #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
              #{"role": "user", "content": "Where was it played?"}
          ]
        )
  result = ''
  for choice in response.choices:
    result += choice.message.content
    
  st.markdown(result)

# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#         {"role": "system", "content": System_Content},#"You are writing a recommendation letter on behalf of Dr. Vahid Behzadan, an assistant professor of computer science and data science, and director of the Secure and Assured Intelligent Learning (SAIL) lab at the University of New Haven."},
#         {"role": "user", "content": query}#"Write a recommendation letter for Stan Smith, a student in our MS Data Science program, for his application to the Computer Science PhD program at Yale. Stan was a student in my Artificial Intelligence class, and performed well."}
#         #{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#         #{"role": "user", "content": "Where was it played?"}
#     ]
# )
# result = ''
# for choice in response.choices:
#     result += choice.message.content
# print (result)