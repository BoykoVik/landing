var arr = $(".sername");

//добавил онклики
for (i=0; i < arr.length; i++){
  var k = arr[i]
  $(k).attr('onClick', 'showstep(' + i + ')');
}

function showstep(i){
    $(".servabout").css('display', 'none');
    $(".servabout").css('opacity', '0');
    for (m=0; m < arr.length; m++){
        arr[m].classList.remove("active");
      }
  var a = $(".servabout")[i];
  $(a).css('display', 'block');
  $(a).animate({opacity: '1'}, 'slow');
  arr[i].classList.add("active");
}
showstep(0);
/////////////////////////////////////////2 блок
var arr2 = $(".othersername");

//добавил онклики
for (i=0; i < arr2.length; i++){
  var k = arr2[i]
  $(k).attr('onClick', 'showstep2(' + i + ')');
}

function showstep2(i){
    $(".otherservabout").css('display', 'none');
    $(".otherservabout").css('opacity', '0');
    for (m=0; m < arr2.length; m++){
        arr2[m].classList.remove("otheractive");
      }
  var a = $(".otherservabout")[i];
  $(a).css('display', 'block');
  $(a).animate({opacity: '1'}, 'slow');
  arr2[i].classList.add("otheractive");
}
showstep2(0);

