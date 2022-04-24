var cal = $(".calcname");
var costs = $(".cost");

for (i=0; i < cal.length; i++){
    var k = cal[i]
    $(k).attr('onClick', 'calc(' + i + ')');
  }

function calc(i){
    var ch = $(".resultcost").text();
        ch = ch.replace(/[a-zа-яё]/gi, '');
    var ch2 = '0' + costs[i].textContent;
    ch2 = ch2.replace(/[a-zа-яё]/gi, '');
    if (!$(cal[i]).hasClass('active')){
        $(".resultcost").text( 'от ' + Number(Number(ch) + Number(ch2)) + ' р')
        cal[i].classList.add("active");
    } 
    else {
        $(".resultcost").text( 'от ' + Number(Number(ch) - Number(ch2)) + ' р')
        cal[i].classList.remove("active");
    }
}