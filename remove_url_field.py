# import json
# import os

# # 업데이트할 JSON 파일 목록
# json_files = [
#     "body_updated_updated.json",
#     "candle_updated_updated.json",
#     "diffuser_updated_updated.json",
#     "perfume_updated_updated.json"
# ]

# # JSON 파일에서 'url' 필드 제거

# def remove_url_field(json_path):
#     with open(json_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
    
#     for product in data:
#         if "options" in product:
#             for option in product["options"]:
#                 if "url" in option:
#                     del option["url"]
    
#     # 변경된 데이터 저장
#     with open(json_path, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
    
#     print(f"✅ {json_path}에서 'url' 필드 제거 완료!")

# # 모든 JSON 파일 처리
# for json_file in json_files:
#     if os.path.exists(json_file):
#         remove_url_field(json_file)
#     else:
#         print(f"⚠️ {json_file} 파일을 찾을 수 없습니다.")
