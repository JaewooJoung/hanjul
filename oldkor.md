# 옛한글 글꼴 제작 가이드 (Old Korean Font Creation Guide)

## 1. 필수 설치 항목 (Required Dependencies)

먼저 FontForge를 설치해야 합니다. 터미널에서 다음 명령어를 실행하세요:

```bash
pip install fontforge
```

## 2. 기본 프로그램 실행 (Basic Program Execution)

기본 글꼴 생성을 위한 파이썬 코드입니다:

```python
# 글꼴 객체 생성
font = OldKoreanFontForge("옛한글서체")  # Create font instance

# 모든 가능한 조합 생성
# (초성, 중성, 종성의 모든 조합을 자동으로 생성)
forge.generate_all_combinations()

# 최종 글꼴 파일 생성 (.ttf 형식)
forge.generate_font("옛한글서체.ttf")
```

## 3. 개별 글리프 디자인 (Custom Glyph Design)

특정 문자의 세부 디자인을 위한 코드입니다:

```python
# 글리프 디자이너 객체 생성
designer = GlyphDesigner(forge.font)

# 특정 문자 디자인 정의
# 획의 시작점, 끝점, 곡선 제어점 등을 정의
strokes = [
    {
        # 획의 시작점 (100,100 좌표)
        'start': (100, 100),
        
        # 획의 끝점 (900,900 좌표)
        'end': (900, 900),
        
        # 곡선 제어점 정의
        'curve_points': [
            {
                'control1': (400, 400),
                # ... 추가 제어점 정의 가능
            }
        ]
    }
]
```

## 주요 기능 설명 (Key Features)

- **초성 조합**: ㄱ, ㄴ, ㄷ 등 모든 옛한글 초성 지원
- **중성 조합**: ㅏ, ㅑ, ㅓ, ㅕ 등 모든 옛한글 모음 지원
- **종성 조합**: 받침 문자 전체 지원
- **특수 문자**: ㆍ(아래아), ㆆ, ㅿ 등 옛한글 특수 문자 지원
- **자동 조합**: 초성, 중성, 종성의 자동 조합 기능

## 기술적 고려사항 (Technical Considerations)

1. **유니코드 매핑**: 
   - 기본 한글 영역: 0xAC00 ~ 0xD7A3
   - 확장 영역: Private Use Area (0xE000 ~) 활용

2. **폰트 메타데이터**:
   - 폰트 이름: 한글/영문 지원
   - 버전 정보
   - 저작권 정보

3. **OpenType 기능**:
   - 자동 조합 규칙
   - 대체 글리프 지원
   - 커닝 정보
