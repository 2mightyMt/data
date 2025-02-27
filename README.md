# DATA

# 개요

Diptyque 리뉴얼 프로젝트를 위한 데이터 저장소입니다.

productData에는 상품 카테고리별 데이터를 구분하였으며,
resources에는 상품의 썸네일 혹은 상세페이지에 쓰일 사진들을 저장합니다.

# JSON 데이터 구조

이 프로젝트는 Diptyque 리뉴얼을 위한 JSON 데이터 구조를 정의합니다. 아래는 각 필드에 대한 설명입니다.

## 📂 데이터 구조 설명

```json
[
    {
        "id": 1,
        "olfactory": "amber",
        "name": "Sample Name",
        "category": "fragrance",
        "type": "Eau de parfum",
        "notes": ["citrus", "woody"],
        "description": "This is a sample description.",
        "story": "This is a related story.",
        "price": {
            "75ml": 190
        },
        "images": {
            "thumbnail": {
                "default": "path/to/default.webp",
                "hover": "path/to/hover.webp"
            },
            "detail": ["path/to/detail1.webp", "path/to/detail2.webp", "path/to/detail3.webp"],
            "option": {
                "75ml": "path/to/option.webp"
            }
        },
        "option": [
            {
                "option": "75ml",
                "url": "path/to/option_page"
            }
        ],
        "collection": [
            {
                "collectionName": "Special Collection"
            }
        ]
    }
]
```

## 📝 필드 설명

| 필드명                     | 타입     | 설명                                                                    |
| -------------------------- | -------- | ----------------------------------------------------------------------- |
| `id`                       | `number` | 상품의 고유 ID (숫자 값)                                                |
| `olfactory`                | `string` | 향 계열 (`amber`, `woody`, `floral`, `citrus` 중 하나)                  |
| `name`                     | `string` | 영문 상품명                                                             |
| `category`                 | `string` | 해당 JSON 파일에 따른 상품 카테고리                                     |
| `type`                     | `string` | 상품 유형 (`Eau de parfum`, `Eau de toilette`, `Solid perfume` 중 하나) |
| `notes`                    | `array`  | 향의 구성 요소 (영문 시향 종류)                                         |
| `description`              | `string` | 상품 설명 (영문)                                                        |
| `story`                    | `string` | 상품과 관련된 이야기 (영문)                                             |
| `price`                    | `object` | 상품 가격 (예: `{ "75ml": 190 }`)                                       |
| `images`                   | `object` | 이미지 정보                                                             |
| `images.thumbnail.default` | `string` | 기본 썸네일 이미지 경로 (webp)                                          |
| `images.thumbnail.hover`   | `string` | 호버 시 변경될 이미지 경로 (webp)                                       |
| `images.detail`            | `array`  | 상세 이미지 경로 목록                                                   |
| `images.option`            | `object` | 옵션별 이미지 경로                                                      |
| `option`                   | `array`  | 상품 옵션 정보 (`option`: 옵션명, `url`: 옵션 관련 페이지)              |
| `collection`               | `array`  | 특정 콜렉션에 포함된 경우에만 값이 존재 (`collectionName`: 콜렉션명)    |

## 🚀 기타 참고사항

-   `olfactory`, `type` 필드는 지정된 값 중 하나만 입력 가능
-   `collection` 필드는 특정 콜렉션 상품이 아닐 경우 `null` 값
-   모든 이미지 경로는 `.webp` 형식을 사용
