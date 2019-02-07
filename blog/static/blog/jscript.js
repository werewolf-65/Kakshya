function call(arg,argn) {
  var btnDiv=document.getElementsByClassName('btndiv');
  for ( i=0;i<btnDiv.length;i++){
    btnDiv[i].style.display="none";
  }
  console.log(arg);
  document.getElementById(arg).style.display="block";
}

window.onload= function () {

   document.getElementById('defaultclick').click();
}


$(function () {
  $(".return").change(function () {
    var st=this.checked;
    if (st){
      $(".renew").prop("disabled",true);
    }
    else{
      $(".renew").prop("disabled",false);
    }
  })
  $(".renew").change(function () {
    var st=this.checked;
    if (st){
      $(".return").prop("disabled",true);
    }
    else{
      $(".return").prop("disabled",false);
   }
  })
});
