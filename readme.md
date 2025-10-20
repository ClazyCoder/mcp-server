# MCP Server

한국 기상청 API를 활용한 날씨 이미지 제공 MCP(Model Context Protocol) 서버입니다.

## 기능

- **날씨 이미지 제공**: 한국 기상청 API를 통해 최근 1시간 전의 강수량 분석 이미지를 제공합니다
- **시간별 예보**: 15분 간격으로 3개의 예보 이미지를 제공합니다 (15분 후, 30분 후, 45분 후)
- **이미지 캐싱**: 다운로드한 이미지를 로컬에 저장하여 재사용합니다

## 주요 도구

### `get_current_weather_imgs()`
한국 기상청의 강수량 분석 이미지를 반환합니다.
- 이전 시간의 날씨 이미지를 제공
- 각 이미지는 15분 간격으로 구성
- MCP ImageContent 형식으로 반환

### `greet(name: str)`
간단한 인사말을 반환하는 테스트 도구입니다.

## 설치 및 실행

### Docker를 사용한 실행

```bash
# Docker Compose로 실행
docker-compose up --build

# 백그라운드 실행
docker-compose up -d --build
```

### 로컬 실행

1. Python 3.12 이상이 필요합니다
2. 의존성 설치:
   ```bash
   uv sync
   ```
3. 환경 변수 설정:
   ```bash
   # .env 파일 생성
   WEATHER_API_KEY=your_api_key_here
   IMG_DIR=./src/imgs
   SERVER_PORT=8000
   ```
4. 서버 실행:
   ```bash
   uv run main.py
   ```

## 환경 변수

- `WEATHER_API_KEY`: 한국 기상청 API 키
- `IMG_DIR`: 이미지 저장 디렉토리 경로
- `SERVER_PORT`: 서버 포트 (기본값: 8000)

## 기술 스택

- **FastMCP**: MCP 서버 프레임워크
- **Pillow**: 이미지 처리
- **Requests**: HTTP 요청
- **Docker**: 컨테이너화
- **uv**: Python 패키지 관리

## 프로젝트 구조

```
mcp_server/
├── src/
│   ├── main.py              # 메인 서버 파일
│   ├── utils/
│   │   └── weather.py       # 날씨 API 유틸리티
│   └── imgs/                # 이미지 저장 디렉토리
├── docker-compose.yaml      # Docker Compose 설정
├── Dockerfile              # Docker 이미지 설정
└── pyproject.toml          # 프로젝트 설정
```

## API 사용법

서버가 실행되면 MCP 클라이언트를 통해 다음 도구들을 사용할 수 있습니다:

1. `get_current_weather_imgs()`: 현재 날씨 이미지 가져오기
2. `greet(name)`: 인사말 생성