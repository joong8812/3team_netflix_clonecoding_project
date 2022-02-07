    // DOM tree가 구성되면
    window.addEventListener('DOMContentLoaded', function(){
        const emailElement = document.querySelector('#email');
        const pwdElement = document.querySelector('#password');
        const loginForm = document.querySelector('#login-info');

        // 쿠키에 value(이메일) 정보 저장
        const setCookie = (name, value, expiredays) => {
            const todayDate = new Date();
            todayDate.setDate(todayDate.getDate() + expiredays);
            document.cookie = name + "=" + escape(value) + "; path=/; expires="
                    + todayDate.toGMTString() + ";";
        }

        // 해당 이름의 쿠키 정보를 불러오기
        const getCookie = (name) => {
            const search = name + '='; // 쿠키값에서 검색할 key값 설정
            const docCookie = document.cookie; // 현재 갖고 있는 쿠키값 불러오기

            if (docCookie.length > 0) { // 쿠키값이 있다면
                let offset = docCookie.indexOf(search); // 검색할 key 값에 첫번째 인덱스를 얻는다
                if (offset != -1) { // 그 인덱스가 -1이 아니라면(key값이 검색이 된다면)
                    offset += search.length; // 해당 key의 value값 첫번째 index를 얻는다
                    end = docCookie.indexOf(';', offset); // value값 이후로 ';' 인덱스 얻음(이 index가 value의 마지막 index다)
                    if (end == -1) end = docCookie.length; // ';' 가 없다면 쿠키전체값의 길이를 마지막 인덱스로 넣음
                    return unescape(docCookie.substring(offset, end)); // 얻고자 하는 쿠키 key의 value만 리턴
                }
            }
        }

        // 로그인 버튼을 누르면 ...
        const handleLoginForm = (event) => {
            event.preventDefault(); // form 값 요청 멈춤
            const saveEmailCheckBox = document.querySelector('#remember-my-id');
            
            // 이메일 기억 체크박스 유무 확인 및 처리
            if (saveEmailCheckBox.checked == true) {
                setCookie('myEmail', emailElement.value, 7); // 7일 동안 쿠키 저장
            } else {
                setCookie('myEmail', emailElement.value, 0); // 날짜를 0으로 저장하여 쿠키 삭제
            }

            loginForm.submit(); // form 값 요청
        }

        loginForm.addEventListener('submit', handleLoginForm);

        // 정해진 이름의 쿠키 값이 있다면 ...
        if (getCookie('myEmail')) {
            emailElement.value = getCookie('myEmail');
            document.querySelector('#remember-my-id').checked = true;
        }
    });