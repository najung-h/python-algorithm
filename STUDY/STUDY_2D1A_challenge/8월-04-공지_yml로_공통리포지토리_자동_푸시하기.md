# GitHub Actions용 PAT 생성 

# & `main.py` 실행 워크플로우 배포 명세서

[공동 레파지토리](https://github.com/13aek/algostudy)

------



## 0) 개요

- 목적:  코드 제출 관리를 효율적으로 해볼까요!
- yaml 파일에 대해 알아가봅시다.

------



## 1) PAT 만들기

> 개인 **GitHub 계정 프로필** 클릭 → **Settings → **좌측 최하단의 **Developer settings → Personal access tokens - Tokens(classic)** 
>  (Classic  선택 — 아래 권장 스코프 참고)

### ![만들기](image1.png)

1. **Generate new token (Classic)** 클릭
2. **Note**: `STUDY_PAT`
3. **Expiration**: 90일/커스텀
4. **Scopes(권한)** :
   - `repo` (푸시, 커밋 등 레포 콘텐츠 쓰기)

5. **Generate token** → 토큰 문자열 즉시 복사 (다시 못 봄)

> ⚠️ 토큰은 비밀입니다. 노출 금지(코드/로그/스크린샷에 넣지 않기).

------



## 2) 레포 Secret 등록

개인 레포지토리 페이지 → **Settings → Security → Secrets and variables → Actions → New repository secret**

- **Name**: `STUDY_PAT`  (대문자/언더스코어 권장)
- **Secret**: (방금 복사한 PAT 값 붙여넣기)
- **Add secret** 클릭

>  `Repository secrets`에 `STUDY_PAT`가 보이면 성공.

------



## 3) 워크플로우 파일 만들기

개인 레포지토리 - 상단의 `actions` 들어가서,

`set up a workflow yourself ` 클릭한다음,



### `main.yml` 복붙하기

```
name: Sync selected problems to study repo

on:
  push:
    branches: [ master ]  # main이면 main로 변경
  workflow_dispatch:

jobs:
  sync-selected:
    runs-on: ubuntu-latest

    steps:
      - name: Check out personal repo
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set git identity
        run: |
          git config --global user.name "${{ github.actor }}"
          git config --global user.email "${{ github.actor }}@users.noreply.github.com"

      - name: Clone study repo
        env:
          STUDY_PAT: ${{ secrets.STUDY_PAT }}
        run: |
          git clone --depth=1 "https://x-access-token:${STUDY_PAT}@github.com/13aek/algostudy.git"

      - name: Install Python deps
        run: |
          python -m pip install --upgrade pip
          pip install pyyaml

      - name: Build changed-file list
        run: |
          BEFORE="${{ github.event.before }}"
          AFTER="${{ github.sha }}"
          if [ -z "$BEFORE" ] || [ "$BEFORE" = "0000000000000000000000000000000000000000" ]; then
            git diff --name-only HEAD~20 > changed_files.txt || true
          else
            git diff --name-only "$BEFORE" "$AFTER" > changed_files.txt || true
          fi
          echo "Changed files:"; cat changed_files.txt || true

      - name: Select & sync ONLY allowlisted problems (full scan, number or name)
        run: |
          python << 'PY'
          import os, re, shutil, yaml, pathlib, sys

          study_repo = "algostudy"
          allow_path = os.path.join(study_repo, "_config", "study-allowlist.yml")
          actor = os.environ.get("GITHUB_ACTOR", "")
          dest_root = os.path.join(study_repo, "members", actor)

          # 1) allowlist 로드
          with open(allow_path, "r", encoding="utf-8") as f:
            allow = yaml.safe_load(f) or {}
          plat = allow.get("platforms", {}) or {}
          boj_nums   = set(map(str, plat.get("boj",  [])))
          swea_nums  = set(map(str, plat.get("swea", [])))
          boj_names  = [str(x) for x in plat.get("boj_names",  [])]
          swea_names = [str(x) for x in plat.get("swea_names", [])]

          # 2) 후보 파일 전체 스캔 (BOJ/boj/백준/SWEA/swea 폴더만)
          roots = ["BOJ", "boj", "백준", "SWEA", "swea"]
          exts  = (".py", ".cpp", ".java", ".md", ".txt")
          candidates = []
          for root in roots:
            if os.path.isdir(root):
              for dp, _, fns in os.walk(root):
                for fn in fns:
                  if fn.endswith(exts):
                    candidates.append(os.path.join(dp, fn))

          # 3) 숫자/이름 매칭
          num_token = re.compile(r'(?<!\d)(\d{2,6})(?!\d)')

          def has_num(path):
            nums = set(num_token.findall(path))
            return bool(nums & boj_nums) or bool(nums & swea_nums)

          def has_name(path):
            # 언더스코어를 공백처럼 취급해 부분일치 강화
            raw   = path
            lower = raw.lower().replace("_", " ")
            for kw in boj_names + swea_names:
              if not kw: 
                continue
              if kw.lower() in lower or kw in raw:
                return True
            return False

          selected = [p for p in candidates if has_num(p.replace("\\","/")) or has_name(p)]

          print(f"ALLOW stats -> BOJ#:{len(boj_nums)} SWEA#:{len(swea_nums)} BOJname:{len(boj_names)} SWEAname:{len(swea_names)}")
          print("CANDIDATES:", len(candidates))
          for i, p in enumerate(selected, 1):
            print(f"SELECTED[{i}]: {p}")

          if not selected:
            sys.exit(0)

          pathlib.Path(dest_root).mkdir(parents=True, exist_ok=True)
          for src in selected:
            dst = os.path.join(dest_root, src)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
          PY

      - name: Commit & Push to study repo (master)
        working-directory: algostudy
        run: |
          git checkout -B master
          if [ -n "$(git status --porcelain)" ]; then
            git add -A
            git commit -m "sync(selected): ${{ github.actor }} from ${{ github.repository }}@${GITHUB_SHA::7}"
            git push origin master
          else
            echo "No selected changes to sync."
          fi

```

