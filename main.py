import openai
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

# Define request model
class TextRequest(BaseModel):
    text: str

# Function to summarize text using OpenAI API
def doc_summarize(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the text in few sentences"},
            {"role": "user", "content": text},
        ],
        max_tokens=350,
        temperature=0.7,
        n=1,
        stop=None
    )
    return response.choices[0].message["content"]

# Define endpoint for summarizing text
@app.post("/summarize/")
async def summarize(request: TextRequest):
    summary = doc_summarize(request.text)
    return {"summary": summary}
