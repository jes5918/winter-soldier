# WinterSoldier

> 종합알림시스템
>
> 부제: 일상의 모든 소소한 알림(알림)을 하나로 관리하자!!



https://optimistic-swirles-b97b6b.netlify.app/



## :tipping_hand_man:팀원정보

| 이름   | 역할           | 주요 개발 기능                                               |
| ------ | -------------- | ------------------------------------------------------------ |
| 장수민 | 프론트엔드     | (FE) 달력, 리팩토링, 유저, 그룹페이지/ (BE) 그룹/ (기능) 챗봇 |
| 김문정 | 백엔드         | 계정관리,  (기능)알림                                        |
| 명도균 | PM, 프론트엔드 | 기획 문서 작성, 전체 화면 레이아웃 구성 / 반응형, (기능)코로나 현황 |
| 유진우 | PM, 프론트엔드 | 기획 문서 작성, 전체 화면 레이아웃 구성 / 반응형, css 코드 리팩토링, (기능)날씨 |
| 전의수 | 백엔드         | Todo, (기능)주식                                             |
| 신민호 | 프론트엔드     | Todolist CRUD, (기능) 오늘의 뉴스                            |



## :traffic_light: 기획

- 초기 컨셉
  - 약 먹을 시간 알림, 버스까지 최적 타이밍, 영화 예매 타이밍, 주식 지표, 날씨 알림(비오면 무조건 알려줘!) 등 일상의 모든 소소한 알림을 하나로!
- TODOLIST에서 확장되어, 유저가 필요할 만한 혹은 내가 구현해보고 싶은 기능 추가하기



## :funeral_urn: 목표 주요 기능

- **기본 TODO** : CRUD

- **달력** : 달력 구현하여 달력의 날짜별 일정 확인 및 일정 관리 기능

- **알림 서비스** : 일정에 맞춰 유저에게 <u>알림 서비스 제공</u>.

- **정보 제공** : <u>각 컨셉마다 유저가 원하는 데이터를 시각화</u> 또는 다른 해서 제공

  - 수민 : 챗봇
  - 도균 : 코로나
  - 문정 : 알림
  - 의수 : 주식
  - 진우 : 날씨
  - 민호 : 뉴스

  

## :deciduous_tree: 개발 환경

- 언어

  - Python 3.7+
  - Django 3.X
  - Node 14.15.X
  - Vue.js 2.6
- 도구
  - vsCode
  - Chrome Browser & Mobile (반응형 웹, 앱 서비스)
- 아키텍쳐

  - Django REST API 서버 & Vue.js
- 배포
  - ngrok
  - netlify



## :warning: 제약 사항

1. Bootstrap / vuetify 등 사용 금지
2. 에러 or 경고 메세지는 Modal 활용
3. 프론트 단에서 데이터 관리는 반드시 **Vuex** 활용
4. **클린 코드**
5. git commit message 컨벤션 지키기 : 다음 사이트를 기준으로 작성. [Git Commit Convention](https://webruden.tistory.com/486)



## :ice_cream: 서비스 개요

- **데이터 베이스**: 각 컨셉마다 데이터 베이스 구축, RESTFul한 url 구축
- **수집 방법** : 자유롭게 API 활용
- **반응협 웹 구축** : 모바일 + 웹



## :page_facing_up: 산출물

- 기능정의서

![image-20210319001616736](README.assets/image-20210319001616736.png)



- 와이어프레임

![image-20210319001812808](README.assets/image-20210319001812808.png)



- 스토리보드

![image-20210319001713529](README.assets/image-20210319001713529.png)



- 테스트

![image-20210319001854639](README.assets/image-20210319001854639.png)



### :computer: ​화면

- 메인화면

![](README.assets/웹 메인.png)

![image-20210319004305026](README.assets/image-20210319004305026.png)



- 회원가입 / 로그인

![](README.assets/회원가입.png)

![](README.assets/로그인.png)



- 일정관리

![](README.assets/월간 달력.png)

![](README.assets/주간 달력.png)

![](README.assets/일정 추가.png)



- 오늘의 뉴스

![](README.assets/오늘의 뉴스.png)



- 주식

![](README.assets/주식.png)



- 코로나, 날씨

![](README.assets/코로나, 날씨.png)



- 챗봇

![image-20210319004556830](README.assets/image-20210319004556830.png)
