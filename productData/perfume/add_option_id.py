import json

# 원본 JSON 파일 경로
input_file = "C:/Users/EZEN/Documents/data/productData/diffuser/diffuser.json"
# 수정된 JSON 저장 경로
output_file = "C:/Users/EZEN/Documents/data/productData/diffuser/diffuser_updated.json"

# JSON 파일 읽기
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# 데이터 수정 (optionId 추가)
for product in data:
    # 리스트로 중첩된 경우 처리
    if isinstance(product, list):
        product = product[0]

    product_id = product["id"]

    # 옵션이 존재하는 경우만 처리
    if "options" in product:
        for idx, option in enumerate(product["options"], start=1):
            option["optionId"] = int(f"{product_id}{idx}")  # 상품 ID + 옵션 순번

# 수정된 JSON 저장
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ 옵션 ID 추가 완료! 결과는 '{output_file}'에 저장됨.")
