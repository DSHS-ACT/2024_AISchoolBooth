import json

# 파일 경로
file_path = 'datas/news.jsonl'
output_path = 'datas/processed_news_turbo.jsonl'

# 데이터 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    processed_data = [json.loads(line) for line in file]

# 데이터 변환
turbo_data = []
for item in processed_data:
  turbo_data.append({
    "messages": [
      {"role": "system", "content": "You are a fake news generator for experiential activities. Use a colloquial tone similar to actual news, and avoid using formal language. Use primarily for references to specific dates or institutions. When entering a specific keyword, please write a Korean news title and text summary that fits the topic."},
      {"role": "user", "content": item['text']},
      {"role": "assistant", "content": item['label']}
    ]
  })

# 변환된 데이터를 JSONL 형식으로 저장
with open(output_path, 'w', encoding='utf-8') as file:
  for entry in turbo_data:
    json.dump(entry, file, ensure_ascii=False)
    file.write('\n')

print(f"Processed data saved to {output_path}")
