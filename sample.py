from openai import OpenAI

client = OpenAI(api_key='')

response = client.completions.create(model="davinci-002",
prompt="You are a fake news generator for experiential activities. Use a colloquial tone similar to actual news, and avoid using formal language. Use primarily for references to specific dates or institutions. When entering a specific keyword, please write a Korean news title and text summary that fits the topic.: 경제, 불황, 고금리, 대출",
max_tokens=64)

print(response.choices[0].text.strip())

