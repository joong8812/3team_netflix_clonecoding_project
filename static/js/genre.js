const next = document.querySelector('.next');
const back = document.querySelector('.back');
const genre = document.querySelector('.genre_cards');
let angle = 0;

next.addEventListener("click", ()=>{
    angle -= 45;
    genre.style.transform = `translateZ(-25rem) rotateY(${angle}deg)`;
})

back.addEventListener("click", ()=>{
    angle += 45;
    genre.style.transform = `translateZ(-25rem) rotateY(${angle}deg)`;
})

const img = document.querySelectorAll(".genre_img");

for(var i = 0; i<img.length; i++){
    img[i].addEventListener("click",clickpic)
}
 // 사진 선택 및 해제하는 함수
function clickpic(){
    pic_list = []
    if(this.getAttribute("class").indexOf("img-selected") == -1){
        this.setAttribute("class", "genre_img img-selected");
        const selected_img = Array.from(document.getElementsByClassName('img-selected'))
        selected_img.forEach(element => {
            var imgAttribute = element.getAttribute("src");
            pic_list.push(imgAttribute.split("/")[5].split(".")[0])
        });
        document.getElementById("genre_list").value = pic_list;
    } else { // image-selected 삭제
        this.setAttribute("class", "genre_img");
        const selected_img = Array.from(document.getElementsByClassName('img-selected'))
        selected_img.forEach(element => {
            var imgAttribute = element.getAttribute("src");
            pic_list.push(imgAttribute.split("/")[5].split(".")[0])
        });
        document.getElementById("genre_list").value = pic_list;
    }
}

// function genre_post(){
//     const genre_list = document.getElementById('genre_list');
//     pic_list = []
//     const selected_img = Array.from(document.getElementsByClassName('img-selected'))
//     selected_img.forEach(element => {
//         var imgAttribute = element.getAttribute("src");
//         // pic_list.push(imgAttribute.split("/")[5].split('.')[0])
//         pic_list.push(imgAttribute.split("_")[1])
//     });
// }