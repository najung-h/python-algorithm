## bootstrap

---

1. [bootstrap](https://github.com/twbs/bootstrap)이란
   - CSS 프론트엔드 프레임워크 (Toolkit; 도구상자)로,
   - 현재 가장 인기 있는 프론트엔드 프레임워크이며 
   - [github star 기준 랭킹 21위](https://gitstar-ranking.com/repositories)
2. 필요성
   - 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 도움
   - -> 생산성을 높이자.

3. 사용예시

   - ```bash
     <!DOCTYPE html>
     <html lang="en">
     <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Najung Site</title>
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
       <!--확장자임을 참고, 웹상의 주소에서 css 및 js 파일을 가져오는 것.-->
     </head>
     <body>
       <p>바디에 쓴 것만 눈에 보입니다</p>
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
     
     </body>
     
     ```

*** 구글 검색 시 , 한글 페이지 사용은 지양합니다.



```bash
</html>$ npm i bootstrap@5.3.8

npm install bootstrap@5.3.8

gem install bootstrap -v 5.3.8
```



CDN

- 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화

  - 웹 페이지 로드 속도를 높임
  - *사용하지 않는다면, 미국 사용자와 한국 사용자 간의 지연시간이 많이 차이가 날 것*

- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

  - *아시아, 유럽, 미주 등 각각의 대륙마다 서버들을 제공하는 서버 회사들에게 대여료를 내고,* 
    *부트스트랩이 CSS와 JS 파일을 업로드 해달라고 부탁하는 것.*
    *그래서 그 서버와 가까운 사람들을 그쪽 서버에 접속을 해서 파일을 쓸 수 있도록*
    *만드는 것 (지리적으로 가깝게끔!)*

    ```CSS
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    ```

    그래서, 아까의 링크를 다시 보면, `cdn.jsdelivr.net`이 미국에 있지 않을 것(아시아 어딘가에 있을 것이라는 사실)임을 추측할 수 있음. 



참고로, CDN 말고, 로컬에 다운로드 받아서 쓸 수도 있는데
부트스트랩 공식 문서에서, [DOWNLOAD](https://getbootstrap.com/docs/5.3/getting-started/download/) 함으로써 직접 파일을 사용할 수 있음.

다운로드 받은 파일에서 `bootstrap.css`파일을 한 번 확인해보면, 
12000줄짜리 파일을 확인할 수 있음
보면, h3 고 뭐고 다 싹 다 갈아엎은 걸 볼 수 있었음.
bootstrap 전체를 쓰고 싶으면, 이것 하나만 가져오면 돼요. 나머지 코드들은 12000줄을 조각낸 코드기 때문에

그리고, 이를 한 줄로 정리한 것이 `bootstrap.min.css`파일



하여튼 여기서는 

그리고, 다 `.`으로 시작하는 것을 볼 수 있는데,

클래스 선택자만 쓰고 있는 것이다.

*(수업때 우리 클래스 씁시다 했었자나요)*

**즉, 클래스 선택자로 이미 스타일을 만들어두었다.**

우리는 이 이름들을 이제, 공식 문서를 보면서 가져다가 쓰면 된다.





---

## Bootstrap 기본 사용법

- Bootstrap에는 특정한 규칙이 있는 클래스 이름으로
  스타일 및 레이아웃이 미리 작성되어 있음

- 예를 들어 클래스 이름으로 Spacing을 표현하고 싶다면
  `{property}{sides}-{size}` 을 찾아서 쓰면 됨

  - property로는 `m`(margin) 혹은 `p`(padding)

  - sides로는 방향 `t`(top) `b`(bottom) `s`(left) `e`(right) `y`(top, bottom) `x`(left,right) `blank` (4sides)

  - size로는 `0`(0rem / 0px) `1`(0.25rem / 4px) `2`(0.5rem / 8px) `3`(1 rem / 16px) `4`(1.5rem / 24px) `5`(3rem / 48px) , `auto`

  - 예 : `.mt-5` 는 이렇게 작성되어잇음
    ```css
    .mt-5 {
      margin-top: 3rem !important;
    }
    ```

    참고로, `!important;`는 지양하기로 했는데, 부트스트랩은 왜 붙여놨을까요?

    우리는 이들이 만들어놓은 도구를 쓰는 것.

    우리가 부트스트랩과 자체적인 css를 함께 사용하다가, 클래스 이름을 만들었는데 하필 부트스트랩과 이름이 똑같다면 어쩌죠. 그럼 기껏 도구 불러와놓고 안 쓰이게 될 것 아니에요. 그런 상황을 방지하기 위해서, 부트스트랩에게 우선순위를 부여하겠다는 거에요.

    

    이런 내용들은 공식 문서에 다 정리가 되어있습니다. 

    공식 문서에 `spacing` `margin-and-padding`이런 것을 보면 되는거에요

    그래서 오늘은 많이 읽으면서 찾아내서 활용하겠습니다.

    


---

참고



bootstrap을 사용하는 이유

- 가장 많이 사용되는 css 프레임워크
- 사전에 디자인된 다양한 컴포넌트 및 기능
  - 빠른 개발과 유지보수
- 손쉬운 반응형 웹 디자인 구현
- 커스터마이징(customizing)이 용이
- 크로스 브라우징 지원
  - 모든 주요 브라우저에서 작동하도록 설계되어 있음





cdn 없이 사용하기 == Bootstrap 코드 파일을 다운로드 받아 활용

1. Bootstrap 코드 파일 다운로드  
   - https://getbootstrap.com/docs/5.3/getting-started/download/

2. `bootstrap.css` 와 `bootstrap.bundle.js` 만 선택

3. CSS 파일은 HTML `<head>` 태그에 가져와서 사용

4. JS 파일은 HTML `<body>` 태그에 가져와서 사용

- 파일 별 포함된 기능이 다르므로 공식문서를 통해 확인  
  - https://getbootstrap.com/docs/5.3/getting-started/contents/



- Bootstrap 코드 파일을 다운로드 받아 활용하는 방법 (예시)

1. 디렉토리 구조
   
   ```mark
   - css/
     - bootstrap.css
   - js/
     - bootstrap.bundle.js
   - index.html
   ```
   
2. index.html 예시 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/bootstrap.css">
  <title>Document</title>
</head>
<body>
  <script src="js/bootstrap.bundle.js"></script>
</body>
</html>
```











