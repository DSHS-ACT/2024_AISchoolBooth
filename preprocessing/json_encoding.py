import json

# 파일 경로
file_path = 'processed_news.jsonl'
output_path = 'processed_news_turbo_encoded.jsonl'

# 데이터 읽기 및 디코딩
with open(file_path, 'r', encoding='utf-8') as file:
    processed_data = [json.loads(line) for line in file]

# 데이터 변환 및 유니코드 디코딩
turbo_data = []
for item in processed_data:
    prompt = item['prompt'].encode().decode('unicode_escape')
    completion = item['completion'].encode().decode('unicode_escape')
    turbo_data.append({
        "messages": [
            {"role": "system", "content": "You are a news generator."},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": completion}
        ]
    })

# 변환된 데이터를 JSONL 형식으로 저장
with open(output_path, 'w', encoding='utf-8') as file:
    for entry in turbo_data:
        json.dump(entry, file, ensure_ascii=False)
        file.write('\n')

print(f"Processed data saved to {output_path}")
