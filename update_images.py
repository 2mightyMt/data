import os
import json
import requests
from urllib.parse import urlparse

def download_image(url, save_path):
    """이미지를 다운로드하여 지정된 경로에 저장"""
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ 이미지 저장 완료: {save_path}")
        else:
            print(f"❌ 이미지 다운로드 실패 (HTTP {response.status_code}): {url}")
    except Exception as e:
        print(f"❌ 이미지 다운로드 오류: {e} - {url}")

def process_json(json_path, category):
    """JSON 파일을 처리하여 이미지 다운로드 및 경로 업데이트"""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    images_base_path = os.path.join("images", category)
    os.makedirs(images_base_path, exist_ok=True)
    
    for product in data:
        product_name = product["name"].replace(" ", "_").replace("/", "_")
        product_folder = os.path.join(images_base_path, product_name)
        os.makedirs(product_folder, exist_ok=True)
        
        for option in product.get("options", []):
            images = option.get("images", {})
            
            for key in ["thumbnail", "detail"]:
                if key in images:
                    if isinstance(images[key], dict):  # 썸네일 처리
                        for img_type, url in images[key].items():
                            filename = f"{product_name}_{img_type}.jpg"
                            save_path = os.path.join(product_folder, filename)
                            download_image(url, save_path)
                            images[key][img_type] = os.path.relpath(save_path, start=os.getcwd())
                    elif isinstance(images[key], list):  # 디테일 이미지 리스트 처리
                        for idx, url in enumerate(images[key], start=1):
                            filename = f"{product_name}_detail_{idx}.jpg"
                            save_path = os.path.join(product_folder, filename)
                            download_image(url, save_path)
                            images[key][idx - 1] = os.path.relpath(save_path, start=os.getcwd())
    
    updated_json_path = os.path.join(os.path.dirname(json_path), f"{category}_updated.json")
    with open(updated_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"🎉 JSON 업데이트 완료: {updated_json_path}")

if __name__ == "__main__":
    base_path = os.path.join(os.getcwd(), "productData")
    categories = ["body", "candle", "diffuser", "perfume"]
    
    for category in categories:
        json_path = os.path.join(base_path, category, f"{category}_updated.json")
        if os.path.exists(json_path):
            process_json(json_path, category)
        else:
            print(f"⚠️ 파일 없음: {json_path}")
