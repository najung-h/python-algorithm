### git 협업 환경 세팅하기 (25.09.08)

1. #### github 리포지토리 생성

- README.md 생성
- 커밋 메시지 컨벤션 파일 업로드
- 1차 회의를 위한 md 파일 (대외용) 업로드

---

2. #### branch 전략 세우기

   우리는 master - dev - feat 순으로 구성하기로 함

   - `master` → 최종 배포용 (CI, CD)

     `dev` → 개발 통합용 (CI)

     `feat/*` → 기능/개인 단위 개발용

---

3. #### branch 생성 및 보호 규칙 설정

- master branch에 대해 branch protection rules 생성

  - Require a pull request before merging ✅

    Require approvals ➜ **2명** 

    Dismiss stale approvals ✅

    Require status checks to pass ✅

    Require branches up to date ✅

    Require conversation resolution ✅

    Do not allow bypassing ✅

    

- dev 생성

- dev branch에 대해 branch protection rules 생성

  - Require a pull request before merging ✅

    Require approvals ➜ **1명** 

    Dismiss stale approvals ✅

    Require status checks to pass ✅

    Require conversation resolution ✅

---

4. #### CI 추가 - `dev` 브랜치에 PR되면 자동 실행

   - `.github/workflows/ci.yml` 생성

     - Python: **Ruff** 자동수정 및 포맷팅
     - JavaScript/TypeScript: **ESLint** 자동수정 및 검사
     - Dockerfile 존재 시: **빌드 확인**

     

   - 레포지토리 권한 설정 확인

     ```markdown
     1. GitHub 레포 → Settings
     2. 좌측 메뉴 → Actions → General
     3. Workflow permissions 섹션
     	- Read and write permissions ✅
     	- Allow GitHub Actions to create and approve pull requests ✅
     ```



---

5. #### 기대 효과

   - 브랜치 보호 규칙 덕분에 PR를 통한 협업 방식이 정착될 것으로 기대
   - CI를 통해 자동으로 코드 스타일을 맞춤으로써 팀 코드가 깔끔하고 일관해질 것으로 기대
   - 리뷰어는 사소한 스타일 지적 대신 로직과 핵심 아이디어에 집중 가능!