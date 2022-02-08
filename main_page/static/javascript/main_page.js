const slides = document.querySelector('.slides'); //전체 슬라이드 컨테이너
const slideImg = document.querySelectorAll('.slides li'); //모든 슬라이드들
let currentIdx = 0; //현재 슬라이드 index
const slideCount = slideImg.length; // 슬라이드 개수
const prev = document.querySelector('.prev'); //이전 버튼
const next = document.querySelector('.next'); //다음 버튼
const slideWidth = 200; //한개의 슬라이드 넓이
const slideMargin = 100; //슬라이드간의 margin 값
// 전체 슬라이드 컨테이너 넓이 설정
slides.style.width = (slideWidth + slideMargin) * slideCount + 'px';

function moveSlide(num) {
    slides.style.left = -num * 200 + 'px';
    currentIdx = num;
}

prev.addEventListener('click', function () { /*첫 번째 슬라이드로 표시 됐을때는 이전 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==0일때만 moveSlide 함수 불러옴 */
    if (currentIdx !== 0) {
        moveSlide(currentIdx - 1);
    }
});
next.addEventListener('click', function () { /* 마지막 슬라이드로 표시 됐을때는 다음 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==slideCount - 1 일때만 moveSlide 함수 불러옴 */
    if (currentIdx !== slideCount / 2) {
        moveSlide(currentIdx + 1);
    }
});


const slides_1 = document.querySelector('.slides-1'); //전체 슬라이드 컨테이너
const slideImg_1 = document.querySelectorAll('.slides-1 li'); //모든 슬라이드들
let currentIdx_1 = 0; //현재 슬라이드 index
const slideCount_1 = slideImg_1.length; // 슬라이드 개수
const prev_1 = document.querySelector('.prev-1'); //이전 버튼
const next_1 = document.querySelector('.next-1'); //다음 버튼
const slideWidth_1 = 200; //한개의 슬라이드 넓이
const slideMargin_1 = 100; //슬라이드간의 margin 값
// 전체 슬라이드 컨테이너 넓이 설정
slides_1.style.width = (slideWidth_1 + slideMargin_1) * slideCount_1 + 'px';

function moveSlide_1(num) {
    slides_1.style.left = -num * 200 + 'px';
    currentIdx_1 = num;
}

prev_1.addEventListener('click', function () { /*첫 번째 슬라이드로 표시 됐을때는 이전 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==0일때만 moveSlide 함수 불러옴 */
    if (currentIdx_1 !== 0) moveSlide_1(currentIdx_1 - 1);
});
next_1.addEventListener('click', function () { /* 마지막 슬라이드로 표시 됐을때는 다음 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==slideCount - 1 일때만 moveSlide 함수 불러옴 */
    if (currentIdx_1 !== slideCount_1 / 2) {
        moveSlide_1(currentIdx_1 + 1);
    }
});


const slides_2 = document.querySelector('.slides-2'); //전체 슬라이드 컨테이너
const slideImg_2 = document.querySelectorAll('.slides-2 li'); //모든 슬라이드들
let currentIdx_2 = 0; //현재 슬라이드 index
const slideCount_2 = slideImg_2.length; // 슬라이드 개수
const prev_2 = document.querySelector('.prev-2'); //이전 버튼
const next_2 = document.querySelector('.next-2'); //다음 버튼
const slideWidth_2 = 200; //한개의 슬라이드 넓이
const slideMargin_2 = 100; //슬라이드간의 margin 값
// 전체 슬라이드 컨테이너 넓이 설정
slides_2.style.width = (slideWidth_2 + slideMargin_2) * slideCount_2 + 'px';

function moveSlide_2(num) {
    slides_2.style.left = -num * 200 + 'px';
    currentIdx_2 = num;
}

prev_2.addEventListener('click', function () { /*첫 번째 슬라이드로 표시 됐을때는 이전 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==0일때만 moveSlide 함수 불러옴 */
    if (currentIdx_2 !== 0)
        moveSlide_2(currentIdx_2 - 1);
});
next_2.addEventListener('click', function () { /* 마지막 슬라이드로 표시 됐을때는 다음 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==slideCount - 1 일때만 moveSlide 함수 불러옴 */
    if (currentIdx_2 !== slideCount_2 / 2) {
        moveSlide_2(currentIdx_2 + 1);
        console.log(slideCount_2)
    }

});

const slides_3 = document.querySelector('.slides-3'); //전체 슬라이드 컨테이너
const slideImg_3 = document.querySelectorAll('.slides-3 li'); //모든 슬라이드들
let currentIdx_3 = 0; //현재 슬라이드 index
const slideCount_3 = slideImg_3.length; // 슬라이드 개수
const prev_3 = document.querySelector('.prev-3'); //이전 버튼
const next_3 = document.querySelector('.next-3'); //다음 버튼
const slideWidth_3 = 200; //한개의 슬라이드 넓이
const slideMargin_3 = 100; //슬라이드간의 margin 값
// 전체 슬라이드 컨테이너 넓이 설정
slides_3.style.width = (slideWidth_3 + slideMargin_3) * slideCount_3 + 'px';

function moveSlide_3(num) {
    slides_3.style.left = -num * 200 + 'px';
    currentIdx_3 = num;
}

prev_3.addEventListener('click', function () { /*첫 번째 슬라이드로 표시 됐을때는 이전 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==0일때만 moveSlide 함수 불러옴 */
    if (currentIdx_3 !== 0) moveSlide_3(currentIdx_3 - 1);
});
next_3.addEventListener('click', function () { /* 마지막 슬라이드로 표시 됐을때는 다음 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==slideCount - 1 일때만 moveSlide 함수 불러옴 */
    if (currentIdx_3 !== slideCount_3 / 2) {
        moveSlide_3(currentIdx_3 + 1);
    }
});


const slides_4 = document.querySelector('.slides-4'); //전체 슬라이드 컨테이너
const slideImg_4 = document.querySelectorAll('.slides-4 li'); //모든 슬라이드들
let currentIdx_4 = 0; //현재 슬라이드 index
const slideCount_4 = slideImg_4.length; // 슬라이드 개수
const prev_4 = document.querySelector('.prev-4'); //이전 버튼
const next_4 = document.querySelector('.next-4'); //다음 버튼
const slideWidth_4 = 200; //한개의 슬라이드 넓이
const slideMargin_4 = 100; //슬라이드간의 margin 값
// 전체 슬라이드 컨테이너 넓이 설정
slides_4.style.width = (slideWidth_4 + slideMargin_4) * slideCount_4 + 'px';

function moveSlide_4(num) {
    slides_4.style.left = -num * 200 + 'px';
    currentIdx_4 = num;
}

prev_4.addEventListener('click', function () { /*첫 번째 슬라이드로 표시 됐을때는 이전 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==0일때만 moveSlide 함수 불러옴 */
    if (currentIdx_4 !== 0)
        moveSlide_4(currentIdx_4 - 1);
});
next_4.addEventListener('click', function () { /* 마지막 슬라이드로 표시 됐을때는 다음 버튼 눌러도 아무런 반응 없게 하기 위해 currentIdx !==slideCount - 1 일때만 moveSlide 함수 불러옴 */
    if (currentIdx_4 !== slideCount_4 / 2) {
        moveSlide_4(currentIdx_4 + 1);
    }
});


// const body = document.querySelector('body');
// const modal = document.querySelector('.modal');
// const btnOpenPopup = document.querySelector('.btn-open-popup');
//
// btnOpenPopup.addEventListener('click', () => {
//     modal.classList.toggle('show');
//
//     if (modal.classList.contains('show')) {
//         body.style.overflow = 'hidden';
//     }
// });
//
// modal.addEventListener('click', (event) => {
//     if (event.target === modal) {
//         modal.classList.toggle('show');
//
//         if (!modal.classList.contains('show')) {
//             body.style.overflow = 'auto';
//         }
//     }
// });

var modals = document.getElementsByClassName("modal");
var btns = document.getElementsByClassName("btn-open-popup");
const body = document.querySelector('body')
var funs = [];

function Modal(num) {
    return function () {
        btns[num].onclick = function () {
            modals[num].style.display = "block";
            body.style.overflow = 'hidden'

        };
    };
}

for (var i = 0; i < btns.length; i++) {
    funs[i] = Modal(i);
}

for (var j = 0; j < btns.length; j++) {
    funs[j]();
}

window.onclick = function (event) {
    if (event.target.className === "modal") {
        event.target.style.display = "none"
        body.style.overflow = 'auto';
    }
}


const makeIframeForClip = (clipUrl) => {
    const iframeTag = document.createElement('iframe');
    iframeTag.setAttribute('src', clipUrl);
    iframeTag.setAttribute('frameborder', 'no');
    iframeTag.setAttribute('scrolling', 'no');
    iframeTag.setAttribute('marginwidth', '0');
    iframeTag.setAttribute('marginheight', '0');
    iframeTag.setAttribute('WIDTH', '300');
    iframeTag.setAttribute('HEIGHT', '180');
    iframeTag.setAttribute('allow', 'autoplay');
    return iframeTag;
}

const makeImgForMR = (mr) => {
    const imgTag = document.createElement('img');
    let imgName = "../static/images/mr/";
    if (mr == '전체') {
        imgName += 'all.png';
    } else if (mr === '12') {
        imgName += '12.png';
    } else if (mr === '15') {
        imgName += '15.png';
    } else {
        imgName += '18.png';
    }
    imgTag.setAttribute('src', imgName);
    return imgTag;
}

const mouseEnterMovieDiv = (event) => {
    event.target.children[0].classList.toggle('hidden'); // .movie-thumb-fist
    event.target.children[1].classList.toggle('hidden'); // .movie-thumb-last
    const lastTop = event.target.children[1].children[0];
    const clipUrl = lastTop.getAttribute('data-url');
    
    lastTop.children[0].classList.toggle('hidden');
    let newTag = makeIframeForClip(clipUrl);
    lastTop.appendChild(newTag)

    // 관람 등급
    const maturityRating = lastTop.getAttribute('data-mr');
    newTag = makeImgForMR(maturityRating);
    const mrDiv = event.target.children[1].children[1].querySelector(".maturity-rating");
    if (mrDiv.children.length == 0) {
        mrDiv.appendChild(newTag);
    }
};

const mouseLeaveMovieDiv = (event) => {
    event.target.children[0].classList.toggle('hidden');
    event.target.children[1].classList.toggle('hidden');
    lastTop = event.target.children[1].children[0];
    lastTop.children[0].classList.toggle('hidden');
    lastTop.removeChild(lastTop.children[1]);
};

slideImages = document.querySelectorAll('.movie-thumb');
console.log(slideImg)
for (let i=0; i<slideImages.length; i++) {
    slideImages[i].addEventListener('mouseenter', mouseEnterMovieDiv);
    slideImages[i].addEventListener('mouseleave', mouseLeaveMovieDiv);
}

