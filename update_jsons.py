# import json
# import os
# import random

# # GitHub 정적 파일 레포지토리 URL
# GITHUB_IMAGE_BASE_URL = "https://raw.githubusercontent.com/2mightyMt/diptyqueStatic/main/images"

# # 카테고리별 ID 시작 번호
# CATEGORY_START_ID = {
#     "body": 100,
#     "candle": 300,
#     "diffuser": 500,
#     "perfume": 700
# }

# # JSON 파일 경로 설정
# json_files = {
#     "body": "productData/body/body_updated.json",
#     "candle": "productData/candle/candle_updated.json",
#     "diffuser": "productData/diffuser/diffuser_updated.json",
#     "perfume": "productData/perfume/perfume_updated.json"
# }

# # JSON 파일 업데이트 경로 설정
# updated_json_files = {
#     "body": "productData/body/body_updated_updated.json",
#     "candle": "productData/candle/candle_updated_updated.json",
#     "diffuser": "productData/diffuser/diffuser_updated_updated.json",
#     "perfume": "productData/perfume/perfume_updated_updated.json"
# }

# def update_json(json_path, updated_json_path, category):
#     """ JSON 파일을 업데이트하여 ID 규칙 적용, 판매량/재고 추가, 이미지 URL 변경, URL 필드 삭제 """
#     try:
#         with open(json_path, "r", encoding="utf-8") as f:
#             data = json.load(f)

#         # ID 시작 값 설정
#         current_id = CATEGORY_START_ID[category]

#         for product in data:
#             # ID 업데이트
#             product["id"] = current_id

#             # 판매량 및 재고 여부 추가
#             product["sales"] = random.randint(0, 500)
#             product["inStock"] = random.choice([True, False])

#             # 제품명 가공 (파일명으로 사용)
#             product_name = product["name"].replace(" ", "_").replace("/", "_")

#             # 옵션 ID 설정 (상품 ID + 옵션 순번)
#             for idx, option in enumerate(product.get("options", []), start=1):
#                 option["optionId"] = int(f"{current_id}{idx}") # 예: 1001, 1002, 1011, 1012 ...
#                 images = option.get("images", {})

#                 if "thumbnail" in images:
#                     images["thumbnail"]["default"] = f"{GITHUB_IMAGE_BASE_URL}/{category}/{product_name}/{product_name}_default.jpg"
#                     images["thumbnail"]["hover"] = f"{GITHUB_IMAGE_BASE_URL}/{category}/{product_name}/{product_name}_hover.jpg"

#                 if "detail" in images:
#                     images["detail"] = [
#                         f"{GITHUB_IMAGE_BASE_URL}/{category}/{product_name}/{product_name}_detail_{idx+1}.jpg"
#                         for idx in range(len(images["detail"]))
#                     ]

#                 # 불필요한 `url` 필드 제거
#                 if "url" in option:
#                     del option["url"]

#             # ID 증가
#             current_id += 1

#         # 업데이트된 JSON 저장
#         with open(updated_json_path, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=4, ensure_ascii=False)

#         print(f"✅ {updated_json_path} 업데이트 완료!")

#     except Exception as e:
#         print(f"❌ 오류 발생 ({json_path}): {e}")

# # 모든 JSON 파일 업데이트 실행
# for category, json_path in json_files.items():
#     update_json(json_path, updated_json_files[category], category)

# print("🎉 모든 JSON 파일 업데이트 완료!")
