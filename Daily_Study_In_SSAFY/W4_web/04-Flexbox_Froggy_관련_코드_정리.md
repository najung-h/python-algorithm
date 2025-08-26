# Flexbox Froggy
[Flex_box_개구리](https://flexboxfroggy.com/#ko) 를 해보면서,
Flexbox관련 CSS 속성을 익혀보자.



---



| 속성                                             | 주요 값                                                  | 설명                           |
| ------------------------------------------------ | -------------------------------------------------------- | ------------------------------ |
| **justify-content** (가로축 정렬)                | `flex-start / start / left`                              | 왼쪽 정렬                      |
|                                                  | `flex-end / end / right`                                 | 오른쪽 정렬                    |
|                                                  | `center`                                                 | 가운데 정렬                    |
|                                                  | `space-between`                                          | 양 끝 고정 + 사이 균등         |
|                                                  | `space-around`                                           | 각 아이템 양 옆 여백 반씩 분배 |
|                                                  | `space-evenly`                                           | 모든 간격 동일                 |
|                                                  | `stretch`                                                | auto 크기 요소 늘려 균등       |
| **align-items** (세로축 정렬)                    | `stretch`                                                | 기본값, 컨테이너 높이에 맞춤   |
|                                                  | `flex-start / start / self-start`                        | 위쪽 정렬                      |
|                                                  | `flex-end / end / self-end`                              | 아래쪽 정렬                    |
|                                                  | `center`                                                 | 세로축 중앙 정렬               |
|                                                  | `baseline / first baseline / last baseline`              | 텍스트 기준선 맞춤             |
| **flex-direction** (주축 방향)                   | `row`                                                    | 가로(왼→오, 기본)              |
|                                                  | `row-reverse`                                            | 가로(오→왼)                    |
|                                                  | `column`                                                 | 세로(위→아래)                  |
|                                                  | `column-reverse`                                         | 세로(아래→위)                  |
| **order** (요소 순서)                            | 정수값 (`-1`, `0`, `1` 등)                               | 순서 재정렬                    |
| **align-self** (개별 세로 정렬)                  | `auto`                                                   | 부모 설정 따름                 |
|                                                  | `flex-start / flex-end / center / self-start / self-end` | 개별 위치 정렬                 |
|                                                  | `baseline / stretch`                                     | 기준선 맞춤 / 늘림             |
| **flex-wrap** (줄바꿈)                           | `nowrap`                                                 | 기본, 줄바꿈 없음              |
|                                                  | `wrap`                                                   | 줄바꿈 (위→아래)               |
|                                                  | `wrap-reverse`                                           | 줄바꿈 (아래→위)               |
| **flex-flow** (단축 속성)                        | `row nowrap` (기본)                                      | 방향+줄바꿈 동시에 설정        |
|                                                  | `column wrap`                                            | 세로 + 줄바꿈                  |
| **align-content** (여러 줄 세로 정렬, wrap 필요) | `flex-start / start`                                     | 위쪽 정렬                      |
|                                                  | `flex-end / end`                                         | 아래쪽 정렬                    |
|                                                  | `center`                                                 | 세로 중앙 정렬                 |
|                                                  | `space-between`                                          | 위·아래 고정 + 사이 균등       |
|                                                  | `space-around`                                           | 각 줄에 여백 반씩 분배         |
|                                                  | `space-evenly`                                           | 모든 줄 간격 동일              |
|                                                  | `stretch`                                                | auto 크기 줄을 늘려 맞춤       |









---

[justify-content](https://developer.mozilla.org/ko/docs/Web/CSS/justify-content)

```css
/* 위치 기준 정렬 */
justify-content: center; /* 항목들을 축의 중심 부분에 정렬합니다. */
justify-content: start; /* 항목들을 축의 시작 부분에 정렬합니다.. */
justify-content: end; /* 항목들을 축의 끝 부분에 정렬합니다. */
justify-content: flex-start; /* 플렉스 항목들을 축의 시작 부분에 정렬합니다. */
justify-content: flex-end; /* 플렉스 항목들을 축의 끝 부분에 정렬합니다. */
justify-content: left; /* 항목들을 축의 왼쪽 부분에 정렬합니다. */
justify-content: right; /* 항목들을 축의 오른쪽 부분에 정렬합니다. */

/* 기준선 정렬 */
/* justify-content은 기준선에 대한 값은 갖지 않습니다. */

/* 기본 정렬 */
justify-content: normal;

/* 분산 정렬 */
justify-content: space-between; /* 항목들을 고르게 정렬합니다.
                                   첫 항목은 시작 부분에 밀착되어 정렬됩니다.
                                   마지막 항목은 끝 부분에 밀착되어 정렬됩니다. */
justify-content: space-around; /* 항목들을 고르게 정렬합니다. 
                                   각 항목들은 양쪽 여백의 절반만큼 나누어 갖습니다. */
justify-content: space-evenly; /* 항목들을 고르게 정렬합니다.
                                   각 항목들은 서로 간에 동일한 여백을 갖습니다. */
justify-content: stretch; /* 항목들을 고르게 정렬합니다.
                                   'auto' 크기로 설정된 항목들을 컨테이너에 맞게 늘립니다. */

/* 오버플로우 정렬 */
justify-content: safe center;
justify-content: unsafe center;

/* 전역 값들 */
justify-content: inherit;
justify-content: initial;
justify-content: revert;
justify-content: revert-layer;
justify-content: unset;
```



[align-items](https://developer.mozilla.org/ko/docs/Web/CSS/align-items)

```css
/* 기본 키워드 값 */
align-items: normal;
align-items: stretch;

/* 위치 기준 정렬 */
/* align-items는 좌우 값을 가지지 않습니다. */
align-items: center;
align-items: start;
align-items: end;
align-items: flex-start;
align-items: flex-end;
align-items: self-start;
align-items: self-end;

/* 기준선 정렬 */
align-items: baseline;
align-items: first baseline;
align-items: last baseline; /* 오버플로우 정렬 (위치 정렬에서만) */
align-items: safe center;
align-items: unsafe center;

/* 전역 값 */
align-items: inherit;
align-items: initial;
align-items: revert;
align-items: revert-layer;
align-items: unset;
```



[flex-direction](https://developer.mozilla.org/ko/docs/Web/CSS/flex-direction)

```css
/* 한 줄의 글을 작성하는 방향대로 */
flex-direction: row;

/* <row>처럼, 대신 역방향 */
flex-direction: row-reverse;

/* 글 여러 줄이 쌓이는 방향대로 */
flex-direction: column;

/* <column>처럼, 대신 역방향 */
flex-direction: column-reverse;

/* 전역 값 */
flex-direction: inherit;
flex-direction: initial;
flex-direction: unset;
```



[order](https://developer.mozilla.org/ko/docs/Web/CSS/order)

```css
/* <integer> 값 */
order: 5;
order: -5;

/* 전역 값 */
order: inherit;
order: initial;
order: unset;
```



[align-self](https://developer.mozilla.org/en-US/docs/Web/CSS/align-self)

```css
/* Keyword values */
align-self: auto;
align-self: normal;

/* Positional alignment */
/* align-self does not take left and right values */
align-self: center; /* Put the item around the center */
align-self: start; /* Put the item at the start */
align-self: end; /* Put the item at the end */
align-self: self-start; /* Align the item flush at the start */
align-self: self-end; /* Align the item flush at the end */
align-self: flex-start; /* Put the flex item at the start */
align-self: flex-end; /* Put the flex item at the end */
align-self: anchor-center;

/* Baseline alignment */
align-self: baseline;
align-self: first baseline;
align-self: last baseline;
align-self: stretch; /* Stretch 'auto'-sized items to fit the container */

/* Overflow alignment */
align-self: safe center;
align-self: unsafe center;

/* Global values */
align-self: inherit;
align-self: initial;
align-self: revert;
align-self: revert-layer;
align-self: unset;
```



[flex-wrap](https://developer.mozilla.org/ko/docs/Web/CSS/flex-wrap)

```css
flex-wrap: nowrap; /* Default value */
flex-wrap: wrap;
flex-wrap: wrap-reverse;

/* Global values */
flex-wrap: inherit;
flex-wrap: initial;
flex-wrap: unset;
```



[flex-flow](https://developer.mozilla.org/ko/docs/Web/CSS/flex-flow)

```css
/* flex-flow: <'flex-direction'> */
flex-flow: row;
flex-flow: row-reverse;
flex-flow: column;
flex-flow: column-reverse;

/* flex-flow: <'flex-wrap'> */
flex-flow: nowrap;
flex-flow: wrap;
flex-flow: wrap-reverse;

/* flex-flow: <'flex-direction'>과 <'flex-wrap'> */
flex-flow: row nowrap;
flex-flow: column wrap;
flex-flow: column-reverse wrap-reverse;

/* 전역 값 */
flex-flow: inherit;
flex-flow: initial;
flex-flow: unset;
```



[align-content](https://developer.mozilla.org/ko/docs/Web/CSS/align-content)

```css
/* Basic positional alignment */
/* align-content does not take left and right values */
align-content: center; /* Pack items around the center */
align-content: start; /* Pack items from the start */
align-content: end; /* Pack items from the end */
align-content: flex-start; /* Pack flex items from the start */
align-content: flex-end; /* Pack flex items from the end */
/* Normal alignment */
align-content: normal;
/* Baseline alignment */
align-content: baseline;
align-content: first baseline;
align-content: last baseline;
/* Distributed alignment */
align-content: space-between; /* Distribute items evenly
                                 The first item is flush with the start,
                                 the last is flush with the end */
align-content: space-around; /* Distribute items evenly
                                 Items have a half-size space
                                 on either end */
align-content: space-evenly; /* Distribute items evenly
                                 Items have equal space around them */
align-content: stretch; /* Distribute items evenly
                                 Stretch 'auto'-sized items to fit
                                 the container */
/* Overflow alignment */
align-content: safe center;
align-content: unsafe center;
/* Global values */
align-content: inherit;
align-content: initial;
align-content: revert;
align-content: unset;
```

