## ⚙️ CI 설정 (GitHub Actions)

### 1. 개요
본 프로젝트는 코드 품질 유지와 협업 효율성을 위해 **GitHub Actions 기반의 CI 파이프라인**을 설계·구현했습니다.  
PR 생성 시 자동으로 코드 스타일 검사, 포맷팅, 자동수정, 빌드 확인이 실행됩니다.

---

### 2. 워크플로우 설계

워크플로우는 `.github/workflows/ci.yml`에 정의되어 있으며, 다음과 같이 세 가지 핵심 Job으로 구성됩니다.

#### (1) Ruff Auto Fix (Python)

- **목적**: Python 코드의 문법 오류 및 스타일 불일치를 자동으로 수정하고 일관성을 유지.
- **주요 동작**:
  - `ruff check --fix`로 규칙 위반 사항 자동 수정
  - `ruff format`으로 Black 스타일 기반 포맷팅 적용
  - 수정 사항이 발생하면 GitHub Actions 봇이 **PR 브랜치에 자동 커밋/푸시**
- **효과**:
   코드 리뷰에서 사소한 포맷 지적을 제거하고, 리뷰어는 비즈니스 로직 검토에만 집중할 수 있음.

#### (2) ESLint (프론트엔드)

- **조건부 실행**: `package.json` 또는 `.eslintrc*` 파일이 존재할 경우에만 실행
- **주요 동작**:
  - `eslint --fix`로 JS/TS 코드 스타일 자동 수정
  - 수정 사항 발생 시 자동 커밋/푸시
  - 최종 검사 단계에서 오류가 남아 있을 경우 CI 실패 처리
- **효과**:
   프론트엔드 코드 역시 Python과 동일한 일관성 있는 품질 기준을 적용할 수 있음.

#### (3) Docker Build

- **조건부 실행**: Dockerfile이 존재할 경우에만 실행
- **주요 동작**:
  - `docker build`로 이미지 빌드 검증 (실제 배포는 제외)
- **효과**:
   배포 환경에서 발생할 수 있는 기본 빌드 오류를 사전에 탐지 가능.

---

### 3. 권한 및 보안 설계

- GitHub Actions 기본 제공 토큰(`GITHUB_TOKEN`)을 활용하여, 별도 secret keys 없이 자동 커밋/푸시를 수행할 수 있도록 설계했습니다.
- 레포지토리 설정에서 **Read and write permissions** 및 **PR 작성 권한**을 부여하였습니다.

---

### 4. Branch Protection 연계
- `master`와 `dev` 브랜치에는 **Branch Protection Rules**를 적용:
  
  - Require pull request before merging
  - Require approvals (1명 이상)
  - Require status checks to pass before merging
  
  CI Job(`ci/ruff-auto-fix`, `ci/lint-frontend`, `ci/docker-build`)을 Required Checks로 등록하여, 
  검증을 통과하지 않으면 머지할 수 없도록 제도화하였습니다.

---

### 5. 설계 의도 및 기대 효과
- **자동화된 코드 품질 관리**: PR마다 린트·포맷·빌드 검증을 자동화하여, 일관된 코드 품질을 유지.
- **리뷰 효율화**: 리뷰어가 사소한 코드 스타일 대신 핵심 로직 검토에 집중할 수 있게 함.
- **협업 안정성 강화**: Branch Protection과 CI 연계를 통해, 미검증 코드가 `dev` 및 `master`로 유입되는 것을 원천 차단.
- **재현 가능성 확보**: Ruff, ESLint, Docker 빌드 검증을 포함하여 실제 배포 환경과 유사한 조건에서의 안정성을 확인.