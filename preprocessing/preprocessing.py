import json

# 파일 경로
file_path = 'datas/news.jsonl'

# 데이터 읽기
with open(file_path, 'r', encoding='utf-8') as file:
  data = [json.loads(line) for line in file]

# 예시 데이터 전처리 (가정: 데이터에 'text'와 'label' 필드가 있음)
processed_data = []
for item in data:
  prompt = f"Generate fake news based on: {item['text']}\n"
  completion = f"{item['label']}\n"
  processed_data.append({"prompt": prompt, "completion": completion})

# 전처리된 데이터를 JSONL 형식으로 저장
with open('datas/processed_news.jsonl', 'w', encoding='utf-8') as file:
  for entry in processed_data:
    json.dump(entry, file, ensure_ascii=False)
    file.write('\n')