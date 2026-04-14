# Qshing-simulation
큐싱 공격 시연

*cloudflared.exe 실행 파일이 존재해야 함* 

VScode 에서 server.py를 실행하고 터미널을 추가로 하나 열어서.\cloudflared tunnel --url http://localhost:8000 입력 
(VScode에서 server.py가 실행 되지 않을시 pip python 다운 및 경로 지정 필요)

cloudflared 가 만들어준 url을 QR로 제작하여 핸드폰을 QR 인식

이후 http://localhost:8000/dashboard.html 을 브라우저로 열어서 실시간 탈취 확인
