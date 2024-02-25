import requests
import os
from openai import OpenAI
from dotenv import load_dotenv
from transformers import BertTokenizer
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4")

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

client = OpenAI(
  api_key="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"  # Use the API key loaded from the .env file
)

# Ask the user to input the topic of their haiku
topic = input("Enter the topic of your haiku: ")


completion = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "user", "content": "Write a haiku based off this topic: " + topic},
        ]
)

haiku = completion.choices[0].message.content

# Tokenize the haiku
tokenized_haiku = enc.encode(haiku)

# Multiply all the tokens by ten
multiplied_tokens = [token + 2 for token in tokenized_haiku]

# Convert the multiplied tokens back to text
detokenized_haiku = tokenizer.decode(multiplied_tokens)




print("Your haiku: ", detokenized_haiku)
