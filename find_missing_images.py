import os
import json

# JSON 파일 경로 설정
json_files = {
    "body": "productData/body/body.json",
    "candle": "productData/candle/candle.json",
    "diffuser": "productData/diffuser/diffuser.json",
    "perfume": "productData/perfume/perfume.json"
}

# 이미지 폴더 경로 설정
images_dir = "images"

# 실제 저장된 상품 폴더 리스트 가져오기
existing_folders = set(os.listdir(images_dir))

# 누락된 이미지가 있는 상품 찾기
missing_images = []

for category, json_path in json_files.items():
    if not os.path.exists(json_path):
        print(f"⚠ JSON 파일이 존재하지 않음: {json_path}")
        continue
    
    with open(json_path, "r", encoding="utf-8") as f:
        products = json.load(f)
    
    for product in products:
        product_name = product["name"].replace(" ", "_").replace("/", "_")
        expected_folder = os.path.join(category, product_name)
        
        if expected_folder not in existing_folders:
            missing_images.append(f"{product['name']} ({category}.json)")

# 결과 출력
if missing_images:
    print("🚨 누락된 이미지가 있는 상품 목록:")
    for item in missing_images:
        print(f"- {item}")
else:
    print("✅ 모든 상품 이미지가 정상적으로 저장됨.")