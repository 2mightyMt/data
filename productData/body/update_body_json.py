import json
import os

# GitHub 정적 파일 레포지토리 URL
GITHUB_IMAGE_BASE_URL = "https://raw.githubusercontent.com/2mightyMt/diptyqueStatic1/main/images/product/body"

# JSON 파일 경로 설정
JSON_PATH = "C:\\Users\\EZEN\\Documents\\data\\productData\\body\\body_updated_updated.json"
UPDATED_JSON_PATH = "C:\\Users\\EZEN\\Documents\\data\\productData\\body\\body_final.json"

def format_name(name):
    """폴더 및 파일명을 위한 문자열 포맷팅 (공백, 특수문자 제거)"""
    return name.replace(" ", "_").replace("/", "_")

def update_image_urls(json_path, updated_json_path):
    """JSON 파일을 읽고 이미지 경로를 GitHub 정적 파일 URL로 업데이트한 후 새로운 JSON 파일로 저장"""
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        for product in data:
            product_type = format_name(product["type"])
            product_name = format_name(product["name"])
            
            for option in product.get("options", []):
                images = option.get("images", {})
                
                if "thumbnail" in images:
                    images["thumbnail"]["default"] = f"{GITHUB_IMAGE_BASE_URL}/{product_type}/{product_name}/thumbnail/default.jpg"
                    images["thumbnail"]["hover"] = f"{GITHUB_IMAGE_BASE_URL}/{product_type}/{product_name}/thumbnail/hover.jpg"
                
                if "detail" in images:
                    images["detail"] = [
                        f"{GITHUB_IMAGE_BASE_URL}/{product_type}/{product_name}/detail/detail_{idx+1}.jpg"
                        for idx in range(len(images["detail"]))
                    ]
        
        # 업데이트된 JSON 파일 저장
        with open(updated_json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ {updated_json_path} 파일 업데이트 완료!")
    except Exception as e:
        print(f"❌ 오류 발생 ({json_path}): {e}")

if __name__ == "__main__":
    update_image_urls(JSON_PATH, UPDATED_JSON_PATH)
    print("🎉 모든 JSON 파일 업데이트 완료!")
