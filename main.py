from google import genai
client = genai.Client()
response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain what an API is in one simple paragraph."
)

print(response.output_text)