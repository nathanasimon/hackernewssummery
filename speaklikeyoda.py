import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

# Use .env to load the API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
  api_key=api_key  # Use the API key loaded from the .env file
)

def yoda_speak(text):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "Answer questions like Yoda would. If it isnt a question just say: Is that so, young padawan?"},
      {"role": "user", "content": question},
    ],
    max_tokens=100,  
    n=1,
    stop=None,
    temperature=0.8,  
  )
  yoda_answer = str(response.choices[0].message.content)
  return yoda_answer

# Get user input and continue asking until they say "exit"
print("Ask Jedi Master Yoda anything. Type 'exit' to quit.")
while True:
    question = input("You:")
    if question.lower() == "exit":
        break

    yoda_answer = yoda_speak(question)
    print("Yoda says: " + yoda_answer)
