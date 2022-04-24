var modal = $(".modal");//модальное окно
var blockwork = $(".workitem");//блок с онкликом
var spanclose = $(".close");//спан с закрытием
console.log(blockwork);

for (i=0; i < blockwork.length; i++){
    var k = blockwork[i];
    $(k).attr('onClick', 'showmodal(' + i + ')');//онклик к блокам на открытие
    var cls = spanclose[i];
    $(cls).attr('onClick', 'closemodal(' + i + ')');//онклик спанов на закрытие
}
//функция открытия
function showmodal(i){
  var a = $(".modal")[i];
  $(a).css('display', 'block');
}
//функция закрытия
function closemodal(i){
    var a = $(".modal")[i];
    $(a).css('display', 'none');
}
