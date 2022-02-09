function three_count() {
    if ($('#three_count').css('display') == 'none') {
        $('#three_count').show();
    }
    self.setTimeout(function hideDiv() {
        document.getElementById("three_count").style.display = "none";
    }, 3000);
}

function pro_logo() {
    if ($('#pro_logo').css('display') == 'none') {
        $('#pro_logo').show();
    }
    self.setTimeout(function HideDiv() {
        document.getElementById('prolog_start').style.display = "none";
    }, 6000);
}

function landing() {
    self.setTimeout(function (){
        let con = document.getElementById('landing');
        con.classList.remove('hidden_land')
    },8000)
}
