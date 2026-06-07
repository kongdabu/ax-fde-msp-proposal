# AX FDE 사업 추진안 — 타깃별 두 버전

AX FDE(AI Transformation Forward Deployed Engineer) 사업 추진안을 **두 가지 타깃 시장**으로 분리한 경영진 보고용 문서·웹사이트입니다.

초기 통합본은 타깃 시장이 **① SI 구축 · ② ITO/MSP 운영 · ③ Palantir 제품모델** 세 준거로 혼재돼 있었습니다. 이를 명확한 두 버전으로 분리했습니다.

## 두 버전

| 버전 | 타깃 시장 | 한 줄 정의 | 마크다운 | 웹페이지 |
|------|-----------|-----------|---------|---------|
| **A** | **한국 SI 구축시장** | 맨먼스 인력기반이 아닌 **FDE 딜리버리 모델**로 구축시장 혁신 | `AX_FDE_사업추진안_SI시장.md` | `si.html` |
| **B** | **ITO · Application MSP 운영시장** | **FDE 기반**으로 ITO·애플리케이션 운영(SM) 업무 자체를 혁신 | `AX_FDE_사업추진안_ITO_MSP시장.md` | `ito-msp.html` |
| (참고) | 통합본(분리 전) | 5개 축 통합 초기본(타깃 혼재) | `AX_FDE_사업추진안.md` / `proposal.md` | `combined.html` |

## 두 버전의 핵심 차이

| 구분 | A · SI 구축시장 | B · ITO/MSP 운영시장 |
|------|----------------|----------------------|
| 대상 업무 | 시스템을 새로 "짓기"(구축) | 맡긴 운영을 "잘 돌리기"(운영·SM) |
| 혁신 대상 | 맨먼스 구축 모델 | 상주 단가 기반 운영위탁 |
| 통증 | 납기 지연·재작업·고정가 리스크 | 운영비 상승·SLA 압박·인력 의존 |
| FDE 적용 | 재사용 자산·AI로 구축 생산성↑ | 현장 내재화, AIOps·GenAI로 운영 성과 |
| G1 게이트 | PoC → 본구축 전환/가치확정 | PoC → 운영 전환 |
| 핵심 KPI | 납기·재작업·자산재사용·구축생산성 | MTTR·자동화율·운영비·SLA |
| 과금 전환 | 맨먼스 → 가치/성과기반 | 상주 맨먼스 → 성과/구독 |

> 공통 확정 입력(약 50명, Squad 4~7명, 6~8주 타임박스, 역할패밀리×시니어리티 매트릭스, 2→4→6 Squad 로드맵)은 두 버전 모두 동일하며, 맥락만 타깃 시장에 맞게 재해석했습니다.

## 웹페이지

- `index.html` — **비교 진입용 랜딩**. 두 버전 카드 + 한눈에 보는 차이표.
- `si.html` / `ito-msp.html` / `combined.html` — 각 버전의 **자체 완결형(self-contained) 반응형 대시보드**(목차 네비게이션·스크롤 스파이). 본문이 HTML에 미리 렌더링되어 내장됨(런타임 `fetch` 없음, Google Fonts만 사용).
- `build.py` — 각 마크다운을 pandoc로 변환해 위 HTML들을 생성하는 다중 페이지 빌더. 본문 수정 시 `python3 build.py`로 재생성.

## 빌드

```bash
python3 build.py   # si.html · ito-msp.html · combined.html · index.html 생성 (pandoc 필요)
```

## 배포

`main` 브랜치 푸시 시 `.github/workflows/deploy.yml`이 GitHub Pages로 자동 배포합니다.
(저장소 Settings → Pages → Source = **GitHub Actions** 필요)

- 진입: `https://kongdabu.github.io/ax-fde-msp-proposal/`
- SI 버전: `.../si.html` · ITO/MSP 버전: `.../ito-msp.html`

---
*모든 추정치는 "추정/가정"으로 표기했으며, 실데이터 입력 시 갱신 대상입니다.*
