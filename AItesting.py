from openai import OpenAI
import os
import requests
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with your API key
OpenAI.api_key = api_key

# Use the updated API method
response = OpenAI.completions.create(
model="gpt-4.0-turbo",  # Ensure this is the latest model
prompt="You are a helpful assistant. tell me about MindX bloodtests",
max_tokens=150  # Adjust as needed
)

print(response.choices[0].text.strip())
