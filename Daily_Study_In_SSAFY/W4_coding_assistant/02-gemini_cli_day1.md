1. 실행

   - 터미널에서 `gemini` 입력

   - 기본 설정 모델 : `gemini-2.5-pro`

     

2. 프롬프트(질문, 명령) 입력

   ```
   1. 로그인 페이지 html로 만들어주세요. html, css, js 세 가지 파일을 만들어주세요. 
   
   2. 우리 사이트는 글로벌한 사이트입니다. 영어로 로그인 페이지를 수정해주세요. 
   
   3. 회원가입 페이지를 만들고, 로그인 페이지랑 연결하는 Navbar를 만들어 주세요.
   
   4. 인덱스 페이지를 만들어 주세요. 
   
   5. 인덱스 페이지에는 챗봇 서비스를 소개하는 안내 글을 넣어주고, 
      기존에 만든 Navbar에도 인덱스 페이지를 연결해 주세요. 
   ```

   - `WriteFile` 도구 사용 허용해주기

     

3. AI 생성 파일 확인

   - AI 생성 파일 `마우스 우클릭` - `Open with Live Server` 클릭
   - 

   

   ## 명령어

   - `/tools` : 도구 목록 출력

   - `/quit` 또는 `ctrl + ccccccccccccccc` : 종료

   - `/compress` : 대화 요약하기
   - `chat save <tag>` : `<tag>`라는 이름의 대화를 저장 (checkpoint) 생성 
   - `/chat list` : 대화 목록 조회
   - `/chat resume <tag>` :  `<tag>`라는 이름의 대화 불러오기
   - `/chat delete <tag>` : 저장한 대화 삭제
   - `gemini -p "정현이가 누구에요?"` : 간단 프롬프팅 - `-p` 명령어로 CLI 실행 없이 답변 생성 가능
   - `gemini -m "gemini-1.5-flash"` 특정 모델로 Gemini CLI 실행
   -  `/auth` : 다른 구글 아이디로 로그인할 때 사용
   - 