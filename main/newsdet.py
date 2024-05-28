from openai import OpenAI

client = OpenAI(api_key='sk-proj-8CoRJ86LEzsOAyywmLkdT3BlbkFJwthj3qyRj5OGcH1r3a10')

user_input = input('Type a news:')

response = client.chat.completions.create(model="gpt-4o",
messages=[
  {"role": "system", "content": "You are a fake news detector. Given the title and summary text of the news, determine whether the text is real news or fake news based on specific evidence and answer in Korean. Find all the evidence in the text without asking for additional information. Finally, determine whether this news is more likely to be real or fake news"},
  {"role": "user", "content": user_input}
])

print(response.choices[0].message.content.strip())
