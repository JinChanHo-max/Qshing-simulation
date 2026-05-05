<div align= "center">
    <img src="https://capsule-render.vercel.app/api?type=waving&color=0:e100ff,100:00ddfa&height=180&text=Qshing-Simulation&animation=&fontColor=000000&fontSize=60" />
    </div>
    <div style="text-align: left;"> 
    <h2 style="border-bottom: 1px solid #d8dee4; color: #282d33;"> 캡스톤 프로젝트 2팀 </h2>  
    <div style="font-weight: 700; font-size: 15px; text-align: left; color: #282d33;"> 

# 악성 QR 코드 생성 및 데이터 탈취 공격 기법
        
### 1. QR 코드 생성 및 배포
공격자는 정상 서비스(공유 킥보드 등)로 위장한 URL을 포함한 QR 코드를 생성한다.  
해당 QR 코드는 오프라인 환경(스티커, 포스터 등)에 부착되어 사용자의 스캔을 유도한다.

### 2. 가짜 웹페이지로 유도
사용자가 QR 코드를 스캔하면, 실제 서비스와 유사하게 디자인된 웹페이지로 이동한다.  
이 페이지는 모바일 환경에 최적화되어 있으며, 사용자가 의심 없이 접근하도록 구성된다.

### 3. 사용자 정보 입력 유도
웹페이지는 로그인 또는 결제 화면을 제공하며, 사용자에게 다음과 같은 정보를 입력하도록 유도한다.

- 계정 정보 (아이디 / 비밀번호)  
- 결제 정보 (카드 번호, 유효기간, CVC 등)

### 4. 데이터 수집 및 전송
사용자가 입력한 정보는 백엔드 서버로 전송되며, 데이터베이스에 저장된다.  
이 과정은 사용자에게 보이지 않으며 정상적인 요청처럼 처리된다.

---

# 전기자전거 QR 코드 대여 시스템 고도화 및 방어 기법

## 🛠 주요 시스템 구성 및 기능

### 1. 대여 시작 및 스캔 (User Side)
* **사용자 앱 인터페이스:** 사용자가 자전거에 부착된 QR 코드를 스캔하여 대여 프로세스를 시작합니다.
* **서버 검증 요청:** 스캔 즉시 데이터의 무결성을 확인하기 위해 중앙 서버로 검증 요청(Server-validation)을 전송합니다.

### 2. 중앙 보안 및 로직 서버 (Core Logic)
시스템의 중추 역할을 하며 **JWT(JSON Web Token)** 기반의 인증과 다중 보안 검증을 수행합니다.
* **정적 분석 및 검증 (Static Analysis):** QR 코드의 구조와 디지털 서명을 검증합니다.
* **사용자 및 기기 상태 검증:** 현재 사용자의 권한 및 자전거 기기의 상태를 실시간으로 체크합니다.
* **위협 정보 통합 분석:** 기존 공격 패턴 DB 및 위협 인텔리전스를 연동하여 분석합니다.
* **안전 URL 검증:** 코드 내 포함된 URL의 피싱 여부를 검증하여 악성 사이트 연결을 원천 차단합니다.

### 3. 외부 위협 방어 기법 (Security Defense)
다양한 공격 시나리오에 대응하는 방어 메커니즘을 포함합니다.
* **주요 차단 대상:** 악성 QR 스캔, 위조 데이터 삽입 시도, 피싱 공격 시도 등.
* **데이터 격리 (Isolation & Divert):** 위협이 감지된 트래픽은 정상 로직에서 즉시 분리(Diverted)하여 격리 환경으로 유도하거나 폐기합니다.

### 4. 보안 판단 결과 (Outcome)
* **위험 경고 (Danger Alert):** 위조/악성 요소 발견 시 사용자에게 즉각 경고를 전송하고 프로세스를 중단합니다.
* **안전 대여 완료:** 모든 검증 단계를 통과한 경우에만 최종적으로 안전하게 대여 절차를 마무리합니다.

---

##  기대 효과
- **사용자 보호:** QR 피싱으로부터 사용자의 개인정보 및 결제 정보 보호.
- **기기 무결성 유지:** 비인가 기기 및 데이터 조작을 통한 부정 대여 방지.
- **서비스 신뢰도 제고:** 검증된 보안 로직을 통해 안전한 공유 경제 생태계 구축.


---

## ⚙️ 핵심 기술 요소

### 1. 프론트엔드 (Frontend)
- 모바일 중심 UI/UX 설계  
- 실제 서비스와 유사한 인터페이스 구현  
- 사용자 입력(Form) 처리 및 이벤트 전송  

### 2. 백엔드 (Backend)
- 사용자 입력 데이터를 수신하는 API 서버 구축  
- 데이터 저장을 위한 데이터베이스 연동  
- 요청 로그 및 수집 데이터 관리 기능  

### 3. QR 코드 생성
- 특정 URL을 포함한 QR 코드 생성 기능  
- 시연을 위한 다양한 QR 코드 이미지 제작 가능  

### 4. 데이터 흐름 처리
- 사용자 입력 → API 요청 → 서버 처리 → DB 저장  
- 전체 데이터 흐름을 추적 및 확인 가능하도록 설계  
    </div>
    <div style="text-align: left;">
    <h2 style="border-bottom: 1px solid #d8dee4; color: #282d33;"> 🛠️ Tech Stacks </h2> <br> 
    <div style="margin: ; text-align: left;" "text-align: left;"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
          <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white">
          <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
          <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
          <img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white">
          <img src="https://img.shields.io/badge/Claude-181717?style=for-the-badge&logo=Claude&logoColor=white">
          <img src="https://img.shields.io/badge/Gemini-181717?style=for-the-badge&logo=Gemini&logoColor=white">
          <img src="https://img.shields.io/badge/ChatGPT-181717?style=for-the-badge&logo=ChatGPT&logoColor=white">
          <br/></div>
    </div>
    <div style="text-align: left;"> 
    <h2 style="border-bottom: 1px solid #d8dee4; color: #282d33;"> 🏅 Stats </h2> <div style="text-align: left;">  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=GodWearsDior&layout=compact&bg_color=60,c545de,28a8c8&title_color=000000&text_color=000000"
          /> </div> 
    </div>
    
