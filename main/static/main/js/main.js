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


   $('#change_profile a').click(function(){

 var toLoad = $(this).attr('href')+' #content_profile';

 $('#content_profile').hide(0,loadContent);
 $('#load').remove();
 $('#wrapper').append('<span id="load">LOADING...</span>');
 $('#load').fadeIn(0);
 function loadContent() {
 $('#content_profile').load(toLoad,'',showNewContent())
 }
 function showNewContent() {
 $('#content_profile').show(0,hideLoader());
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

   $(".coupon-btn").on("click", function() {
    copyToClipboard("#coupon-field");
    $(".coupon-alert").fadeIn("slow");
  });



    $("#push_profile_1").on("click", function() {
    $("#push_profile_1").addClass("button-settings-active");
    $("#push_profile_2").removeClass("button-settings-active");
    $("#push_profile_3").removeClass("button-settings-active");

  });

    $("#push_profile_2").on("click", function() {
    $("#push_profile_2").addClass("button-settings-active");
    $("#push_profile_1").removeClass("button-settings-active");
    $("#push_profile_3").removeClass("button-settings-active");

  });

    $("#push_profile_3").on("click", function() {
    $("#push_profile_3").addClass("button-settings-active");
    $("#push_profile_2").removeClass("button-settings-active");
    $("#push_profile_1").removeClass("button-settings-active");

  });

  // copy coupone code to clipboard
  $("#push0").on("click", function() {
    $("#push0").addClass("button-active");
    $("#push1").removeClass("button-active");
    $("#push2").removeClass("button-active");
    $("#push3").removeClass("button-active");
    $("#push4").removeClass("button-active");
  });
   $("#push1").on("click", function() {
    $("#push0").removeClass("button-active");
    $("#push1").addClass("button-active");
    $("#push2").removeClass("button-active");
    $("#push3").removeClass("button-active");
    $("#push4").removeClass("button-active");
  });
   $("#push2").on("click", function() {
    $("#push0").removeClass("button-active");
    $("#push1").removeClass("button-active");
    $("#push2").addClass("button-active");
    $("#push3").removeClass("button-active");
    $("#push4").removeClass("button-active");
  });
   $("#push3").on("click", function() {
    $("#push0").removeClass("button-active");
    $("#push1").removeClass("button-active");
    $("#push2").removeClass("button-active");
    $("#push3").addClass("button-active");
    $("#push4").removeClass("button-active");
  });
    $("#push4").on("click", function() {
    $("#push0").removeClass("button-active");
    $("#push1").removeClass("button-active");
    $("#push2").removeClass("button-active");
    $("#push3").removeClass("button-active");
    $("#push4").addClass("button-active");
  });
});

$(function() {
       $("#friend_form").submit(function(event) {
           // Stop form from submitting normally
           event.preventDefault();
           var friendForm = $(this);
           // Send the data using post
           var posting = $.post( friendForm.attr('action'), friendForm.serialize() );
           // if success:
           posting.done(function(data) {

               // success actions, maybe change submit button to 'friend added' or whatever
           });
           // if failure:
           posting.fail(function(data) {
               // 4xx or 5xx response, alert user about failure
           });
       });
});