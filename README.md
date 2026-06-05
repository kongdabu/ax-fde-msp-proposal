# AX FDE 사업 추진안 — 한국 MSP 운영 내재화형 FDE

한국 MSP(IT운영 위탁) 시장에서 **"운영 내재화형 AX FDE"**(AI Transformation Forward Deployed Engineer) 조직·사업 추진안을 5개 축으로 통합한 경영진 보고용 문서입니다.

> **AX FDE** = 고객의 기존 IT운영(MSP) 현장에 내재화되어, AI(AIOps·GenAI)로 운영 성과(MTTR·자동화율·운영비)를 내고 그 성과로 값을 받는 전담 엔지니어.

## 구성 (5개 축)
1. **전략·차별화** — 시장 정의, Global(Palantir형) 대비 차별화, 수익모델, GTM
2. **조직·거버넌스** — CoE+상주팀 하이브리드, R&R/RACI, 채용·운영모델
3. **프로세스·방법론** — Engagement→Delivery, D0~D6 방법론, PoC→운영 전환 게이트
4. **툴·플랫폼** — 플랫폼 비종속 4레이어 스택, 재사용 Asset, 규제산업 대응
5. **역량·인력양성·CDP** — 복합역량 모델, 내부 전환 중심 양성, 듀얼 래더 CDP

추가로 **4-Phase 이행 로드맵 · 통합 KPI 트리 · 리스크 대응 · 정합성 검수**를 포함합니다.

## 웹페이지
- `index.html` — **자체 완결형(self-contained) 반응형 대시보드**(목차 네비게이션·스크롤 스파이). 본문이 HTML에 미리 렌더링되어 내장됨(런타임 `fetch`·외부 마크다운 라이브러리 의존 없음, Google Fonts만 사용).
- `proposal.md` / `AX_FDE_사업추진안.md` — 통합 추진안 본문 소스(동일 내용).
- `build.py` — `proposal.md`를 pandoc로 변환해 `index.html`을 생성하는 빌더. 본문 수정 시 `python3 build.py`로 재생성.

## 배포
`main` 브랜치 푸시 시 `.github/workflows/deploy.yml`이 GitHub Pages로 자동 배포합니다.
(저장소 Settings → Pages → Source = **GitHub Actions** 필요)

---
*모든 추정치는 "추정/가정"으로 표기했으며, 실데이터 입력 시 갱신 대상입니다.*
