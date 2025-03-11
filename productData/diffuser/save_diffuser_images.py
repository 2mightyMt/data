import os
import json
import requests
import time

# JSON 파일 경로
JSON_PATH = "C:\\Users\\EZEN\\Documents\\data\\productData\\diffuser\\diffuser.json"

# 이미지 저장 기본 경로
SAVE_DIR = "C:\\Users\\EZEN\\Documents\\data\\productData\\diffuser\\images"

# 최대 재시도 횟수
MAX_RETRIES = 5

# 요청 헤더 설정 (브라우저처럼 보이도록)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.diptyqueparis.com/"
}


def download_image(url, save_path):
    """이미지를 다운로드하고 저장하는 함수"""
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                print(f"✅ 다운로드 성공: {save_path}")
                return True
            else:
                print(f"⚠️ 다운로드 실패 [{response.status_code}] {url}")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ 요청 오류: {e}")

        retries += 1
        print(f"🔄 재시도 ({retries}/{MAX_RETRIES})...")
        time.sleep(1)  # 재시도 전에 2초 대기

    print(f"❌ 최대 재시도 횟수 초과: {url}")
    return False


def process_images():
    """JSON 데이터를 읽고, 이미지 다운로드 후 저장하는 함수"""
    if not os.path.exists(JSON_PATH):
        print(f"❌ JSON 파일을 찾을 수 없음: {JSON_PATH}")
        return

    with open(JSON_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    failed_downloads = []

    for item in data:
        product_type = item["type"].replace(" ", "_")
        product_name = item["name"].replace(" ", "_")

        base_path = os.path.join(SAVE_DIR, "diffuser", product_type, product_name)
        thumbnail_path = os.path.join(base_path, "thumbnail")
        detail_path = os.path.join(base_path, "detail")

        os.makedirs(thumbnail_path, exist_ok=True)
        os.makedirs(detail_path, exist_ok=True)

        for option in item.get("options", []):
            images = option.get("images", {})

            # 썸네일 이미지 저장
            for thumb_type, url in images.get("thumbnail", {}).items():
                file_name = f"{thumb_type}.jpg"
                save_path = os.path.join(thumbnail_path, file_name)
                if not os.path.exists(save_path):  # 이미 다운로드된 파일은 건너뛰기
                    if not download_image(url, save_path):
                        failed_downloads.append((url, save_path))

            # 디테일 이미지 저장
            for idx, url in enumerate(images.get("detail", [])):
                file_name = f"detail_{idx + 1}.jpg"
                save_path = os.path.join(detail_path, file_name)
                if not os.path.exists(save_path):  # 이미 다운로드된 파일은 건너뛰기
                    if not download_image(url, save_path):
                        failed_downloads.append((url, save_path))

    # 실패한 이미지 다시 시도
    retry_failed_downloads(failed_downloads)


def retry_failed_downloads(failed_list):
    """다운로드 실패한 파일들을 다시 시도하는 함수"""
    remaining_failures = []

    for url, save_path in failed_list:
        if not download_image(url, save_path):
            remaining_failures.append((url, save_path))

    if remaining_failures:
        print("\n❌ 여전히 실패한 파일들:")
        for url, _ in remaining_failures:
            print(url)


if __name__ == "__main__":
    process_images()
