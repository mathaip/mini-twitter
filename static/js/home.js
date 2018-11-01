$(document).ready(function () {
  $(".submit").click(function () {
    $(".overlay").fadeIn(500);
  });
  $(".overlay").not(".text").click(function() {
    $(".overlay").fadeOut(500);
  });
  $("[type = submit]").click(function () {
    var tweet = $("textarea").val();
    $("<p class='tweets'>" + tweet + "</p>").appendTo("section");
  });
});