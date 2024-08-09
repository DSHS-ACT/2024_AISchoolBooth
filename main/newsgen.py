from openai import OpenAI

client = OpenAI(api_key='THERE_IS_NO_API_KEY')

user_input = input('Type a news:')

response = client.chat.completions.create(model="gpt-4o",
messages=[
  {"role": "system", "content": "You are a fake news generator for experiential activities. Use a colloquial tone similar to actual news, and using formal language. Use primarily for references to specific dates or institutions. When entering a specific keyword, please write a Korean news title and use a formal text that fits the topic."},
  {"role": "user", "content": user_input}
])

print(response.choices[0].message.content.strip())
