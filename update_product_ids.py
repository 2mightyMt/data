# import json
# import random

# # 카테고리별 ID 시작 번호
# CATEGORY_START_ID = {
#     "body": 100,
#     "candle": 300,
#     "diffuser": 500,
#     "perfume": 700
# }

# def update_json(file_path, category):
#     """ JSON 파일을 업데이트하여 새로운 ID 규칙, 판매량, 재고 상태를 추가 """
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = json.load(f)
    
#     # ID 시작 값 설정
#     current_id = CATEGORY_START_ID[category]
    
#     for product in data:
#         product["id"] = current_id  # 새로운 ID 할당
#         product["sales"] = random.randint(0, 500)  # 판매량 랜덤 설정
#         product["inStock"] = random.choice([True, False])  # 재고 여부 랜덤 설정
        
#         # ID 증가
#         current_id += 1
    
#     # 업데이트된 JSON 저장
#     updated_file_path = file_path.replace(".json", "_updated.json")
#     with open(updated_file_path, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
    
#     print(f"✅ {updated_file_path} 업데이트 완료!")

# # 처리할 파일 목록
# files = {
#     "body": "productData/body/body_updated.json",
#     "candle": "productData/candle/candle_updated.json",
#     "diffuser": "productData/diffuser/diffuser_updated.json",
#     "perfume": "productData/perfume/perfume_updated.json"
# }

# # 각 파일 업데이트 실행
# for category, file_path in files.items():
#     update_json(file_path, category)
