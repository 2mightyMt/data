# Diptyque 제품 데이터셋 설명

이 프로젝트는 Diptyque의 다양한 제품 정보를 담고 있는 JSON 데이터셋을 포함하고 있습니다.  
각 JSON 파일은 해당 제품군에 대한 정보를 포함하며, 제품의 주요 속성과 옵션(예: 사이즈, 가격, 이미지 등)을 포함하고 있습니다.

## 데이터 파일 설명

### 1. `perfume.json` (향수 데이터)

-   **id**: 제품 고유 ID
-   **olfactory**: 향의 카테고리 (예: Amber, Floral 등)
-   **name**: 제품 이름
-   **type**: 제품 유형 (예: Eau de Parfum)
-   **notes**: 향의 주요 노트 (예: Benzoin, Patchouli 등)
-   **description**: 제품 설명
-   **story**: 제품의 스토리와 영감
-   **options**:
    -   **size**: 용량 (예: 75ml)
    -   **price**: 가격 (달러 기준)
    -   **images**: 제품 이미지 (썸네일, 상세 이미지 포함)
    -   **url**: 제품 옵션 사진 링크 url 밎 사진
    -   **optionId**: 옵션의 고유 ID
-   **collection**: 해당 제품이 속한 컬렉션 (빈 배열일 수도 있음)

---

### 2. `diffuser.json` (디퓨저 데이터)

-   **id**: 제품 고유 ID
-   **olfactory**: 향의 카테고리
-   **name**: 제품 이름
-   **type**: 제품 유형 (예: Room Spray)
-   **notes**: 향의 주요 노트
-   **description**: 제품 설명
-   **options**:
    -   **size**: 용량 (예: 150ml)
    -   **price**: 가격
    -   **weight**: 제품 무게
    -   **images**: 제품 이미지
    -   **url**: 제품 옵션 사진 링크 url 밎 사진
    -   **optionId**: 옵션의 고유 ID
-   **collection**: 해당 제품이 속한 컬렉션

---

### 3. `candle.json` (캔들 데이터)

-   **id**: 제품 고유 ID
-   **olfactory**: 향의 카테고리
-   **name**: 제품 이름
-   **notes**: 향의 주요 노트
-   **description**: 제품 설명
-   **options**:
    -   **size**: 캔들 크기 (예: small, classic)
    -   **price**: 가격
    -   **weight**: 제품 무게 (예: 70g, 190g)
    -   **images**: 제품 이미지
    -   **url**: 제품 옵션 사진 링크 url 밎 사진
    -   **optionId**: 옵션의 고유 ID
-   **collection**: 해당 제품이 속한 컬렉션

---

### 4. `body.json` (바디 관련 데이터)

-   **id**: 제품 고유 ID
-   **olfactory**: 향의 카테고리
-   **name**: 제품 이름
-   **type**: 제품 유형 (예: Scented Soap)
-   **keyword**: 상품 관련 키워드
-   **description**: 제품 설명
-   **story**: 제품의 스토리
-   **options**:
    -   **size**: 제품 크기 (예: 200g)
    -   **price**: 가격
    -   **weight**: 제품 무게
    -   **images**: 제품 이미지
    -   **url**: 제품 옵션 사진 링크 url 밎 사진
-   **collection**: 해당 제품이 속한 컬렉션

---

## 데이터 활용 방법

-   JSON 데이터를 이용해 Diptyque 제품의 상세 정보를 표시할 수 있습니다.
-   옵션(`options`) 배열을 활용하여 제품의 다양한 변형을 표현할 수 있습니다.
-   각 제품의 `collection`을 활용하여 특정 컬렉션별 제품을 분류할 수 있습니다.
