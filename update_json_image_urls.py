# import json
# import os

# # GitHub 정적 파일 레포지토리 URL
# GITHUB_IMAGE_BASE_URL = "https://raw.githubusercontent.com/2mightyMt/diptyqueStatic/main/images"

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

# def update_image_urls(json_path, updated_json_path, category):
#     """
#     JSON 파일을 읽고 이미지 경로를 GitHub 정적 파일 URL로 업데이트한 후 새로운 JSON 파일로 저장.
#     """
#     try:
#         with open(json_path, "r", encoding="utf-8") as f:
#             data = json.load(f)
        
#         for product in data:
#             product_name = product["name"].replace(" ", "_").replace("/", "_")
            
#             for option in product.get("options", []):
#                 images = option.get("images", {})
                
#                 if "thumbnail" in images:
#                     images["thumbnail"]["default"] = f"{GITHUB_IMAGE_BASE_URL}/{category}/{product_name}/{product_name}_default.jpg"
#                     images["thumbnail"]["hover"] = f"{GITHUB_IMAGE_BASE_URL}/{category}/{product_name}/{product_name}_hover.jpg"
                
#                 if "detail" in images:
#                     images["detail"] = [
#                         f"{GITHUB_IMAGE_BASE_URL}/{category}/{product_name}/{product_name}_detail_{idx+1}.jpg"
#                         for idx in range(len(images["detail"]))
#                     ]
        
#         # 업데이트된 JSON 파일 저장
#         with open(updated_json_path, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=4, ensure_ascii=False)
        
#         print(f"✅ {updated_json_path} 파일 업데이트 완료!")
#     except Exception as e:
#         print(f"❌ 오류 발생 ({json_path}): {e}")

# # 모든 JSON 파일 업데이트 실행
# for category, json_path in json_files.items():
#     update_image_urls(json_path, updated_json_files[category], category)

# print("🎉 모든 JSON 파일 업데이트 완료!")