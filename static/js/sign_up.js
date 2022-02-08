
var email = document.querySelector("#email");

//이메일 형식을 검사할 정규표현식
var exp = /^([0-9a-zA-Z_\.-]+)@([0-9a-zA-Z_-]+)(\.[0-9a-zA-Z_-]+){1,2}$/;
email.addEventListener('keyup', function (){ //키를 놓을 때 발생하는 이벤트
    var e_times = document.querySelector('.e_times');
    var e_check = document.querySelector('.e_check');

    // 조건에 맞지 않을 때는 빨간색, 조건을 충족했다면 초록색
    //test()를 이용해 찾는 문자열 확인
    var e_error = document.querySelector('#e_error')
    if (exp.test(email.value)==false){
        email.style.border = '2px solid red';
        e_times.style.display = 'block';
        e_check.style.display = 'none';
        e_error.innerText = "이메일 형식이 아닙니다."
        e_error.style.visibility ='visible';
        return false
    }else {
        email.style.border = '2px solid green';
        e_times.style.display = 'none';
        e_check.style.display = 'block';
        e_error.style.visibility ='hidden';
    }
})

var password = document.querySelector("#password");
password.addEventListener('keyup', function (){ //키를 놓을 때 발생하는 이벤트
    var p_times = document.querySelector('.p_times');
    var p_check = document.querySelector('.p_check');

    var pwd_error = document.querySelector('#pwd_error')
    if (password.value.length < 5){
        password.style.border = '2px solid red';
        p_times.style.display = 'block';
        p_check.style.display = 'none';
        pwd_error.innerText = "비밀번호는 5자리 이상이여야 합니다.";
        pwd_error.style.visibility ='visible';
        return false
    }else {
        password.style.border = '2px solid green';
        p_times.style.display = 'none';
        p_check.style.display = 'block';
        pwd_error.style.visibility ='hidden';
    }

})

var profile_name = document.querySelector("#profile-name");
profile_name.addEventListener('keyup', function (){ //키를 놓을 때 발생하는 이벤트
    var name_times = document.querySelector('.name_times');
    var name_check = document.querySelector('.name_check');
    var name_error = document.querySelector('#name_error');

    if (profile_name.value.length < 3){
        profile_name.style.border = '2px solid red';
        name_times.style.display = 'block';
        name_check.style.display = 'none';
        name_error.innerText = "프로필명은 3자리 이상이여야 합니다.";
        name_error.style.visibility ='visible';
        return false
    }else {
        profile_name.style.border = '2px solid green';
        name_times.style.display = 'none';
        name_check.style.display = 'block';
        name_error.style.visibility ='hidden';
    }
})

// 오류가 났을 때


// 버튼 클릭시 유효성 검사
// function checkInput(){
//     //trim()을 통해 공백제거 후 값 가져오기
//     emailValue = email.value.trim();
//     passwordValue = password.value.trim();
//
//     // email 형식이 아닐때
//     if(emailValue)
// }