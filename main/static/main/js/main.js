$(document).ready(function() {

 $('#change a').click(function(){

 var toLoad = $(this).attr('href')+' #content1';

 $('#content1').hide(0,loadContent);
 $('#load').remove();
 $('#wrapper').append('<span id="load">LOADING...</span>');
 $('#load').fadeIn(0);
 function loadContent() {
 $('#content1').load(toLoad,'',showNewContent())
 }
 function showNewContent() {
 $('#content1').show(0,hideLoader());
 }
 function hideLoader() {
 $('#load').fadeOut(0);
 }
 return false;

 });


  $('#change a').click(function(){

 var toLoad = $(this).attr('href')+' #content';

 $('#content').hide(0,loadContent);
 $('#load').remove();
 $('#wrapper').append('<span id="load">LOADING...</span>');
 $('#load').fadeIn(0);
 function loadContent() {
 $('#content').load(toLoad,'',showNewContent())
 }
 function showNewContent() {
 $('#content').show(0,hideLoader());
 }
 function hideLoader() {
 $('#load').fadeOut(0);
 }
 return false;

 });



});


$(function() {
  // copy content to clipboard
  function copyToClipboard(element) {
    var $temp = $("<input>");
    $("body").append($temp);
    $temp.val($(element).text()).select();
    document.execCommand("copy");
    $temp.remove();
  }

  // copy coupone code to clipboard
  $(".coupon-btn").on("click", function() {
    copyToClipboard("#coupon-field");
    $(".coupon-alert").fadeIn("slow");
  });
});

