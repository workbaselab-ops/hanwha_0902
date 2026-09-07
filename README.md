# README

# hanwha_0902

한화시스템 K-뉴딜아카데미 「지능형(AI) 에이전트 기반 서비스 개발 과정 1기」 
(2026.09.01 ~ 2026.11.13)

## 폴더 구조

```
.
├── 01_class/          수업 중 따라 친 코드
│   └── week01/
│       ├── 0902/
│       ├── 0903/
│       └── 0904/
├── 02_review/         복습 — 백지 타이핑 코드 + 가이드 문서
│   └── week01/
└── 03_assignment/     별도 제출물
```

- 최상위 폴더는 **hanwha_0902**
- 폴더는 `week{NN}/{MMDD}`까지만. 주제별 하위 폴더는 만들지 않는다.
- 파일명은 **전부 소문자**, 띄어쓰기 대신 `_`, **한글 금지** (Windows/Mac 호환).
- 단어는 W3Schools 메뉴명에서 가져온다. 모르겠으면 `01.py`, `02.py`도 무방.
- **`import` 뒤에 오는 이름은 파일명으로 쓰지 않는다.** `numpy.py`, `streamlit.py`, `time.py`처럼 만들면
`import numpy`가 라이브러리 대신 내 파일을 불러와서 깨진다. 뒤에 `_단어`를 붙인다 → `numpy_review.py`, `streamlit_toast.py`.
(`classes.py`, `strings.py`처럼 import하지 않는 단어는 괜찮다.)

## 작업 시작 순서 (매번)

1. GitHub Desktop → **Fetch/Pull** (다른 컴퓨터에서 올린 것 받기)
2. VS Code로 `hanwha_0902` 폴더 열기
3. 가상환경이 없으면 만들기 (컴퓨터마다 한 번): 터미널에서 `python -m venv .venv` (Mac은 `python3`)
4. 가상환경 켜기: Windows `.venv\Scripts\activate` / Mac `source .venv/bin/activate`
5. 작업 → 끝나면 GitHub Desktop에서 Commit → Push → (강의실이면) 로그아웃

## 커밋 전 확인

- [ ]  가상환경 폴더가 스테이징에 없는가 (`venv/`는 .gitignore 처리됨)
- [ ]  API 키·토큰이 코드에 하드코딩돼 있지 않은가 → `.env`로 분리
- [ ]  `git status`에 의도하지 않은 파일이 없는가

> 이 저장소는 **Public**입니다. 민감정보는 절대 커밋하지 않습니다.
> 

## 작업 환경

| 위치 | 장비 | 비고 |
| --- | --- | --- |
| 강의실 | 공용 Windows 노트북 (D드라이브) | 종료 시 VS Code·GitHub Desktop **로그아웃 필수** |
| 집 | Mac Studio M2 (`~/Desktop/dev`) | Python 3.12.10 |









# 26-09-07 수업

### **깃허브에서 충돌나는거 해결하는 방법**

.git 아얘 삭하기 또는 충돌나는 지점 찾아서 수정하기

**Conplict 발생**
(교육장)수정 하고나서 push : a  → (집) 수정 push  : b 

## **Pydantic**

https://pydantic.dev/docs/validation/latest/get-started/
혼자 연습용 official 사이트

pip install pydantic 

pip install annotated_types

### **수업시간에 코랩 이용해서 연습**

코랩에서 연습한 파일을 → 

 (.ipyd),(.py)

Jupyter 검색 해서 확장프로그램 다운받기 → ipyd문서가 열린다

### **강사님 깃허브 계정**

https://github.com/skc4365/hanwha_0902

day1~day4 : 혼자연습용   

### **markdown 문서**

.md

코드처럼 볼수도있고, preview를 다운받거나 열리는 프로그램에서 열어서 직접 수정도 가능

markdown 확장자 설치 vs code에서도 볼수있음

### **디버깅하는 방법**

행번호 앞에 마우스오버시 빨간 점 노출

vs code에서 디버깅 하는 방법 검색해서 확인가능
