



$(document).ready(function() {


    $("#getProfile").on("click", function(){
      var longString = "I am a full stack developer with experience in Python, CSS, HTML, \
          and a touch of Javascript. I enjoy taking a pragmatic approach to problem solving and \
          designing web architecture that is both sensible and aesthetically pleasing. The creation of \
          this site is achieved using Django with SQLite and Git for version control."
      $(".message").html(longString);
    });

    $("#getProjects").on("click", function(){
      $(".message").html("Here is the getProjects");
    });

    $("#getTechnology").on("click", function(){
      $(".message").html("Here is the getTechnology");
    });

    $("#getContact").on("click", function(){
      $(".message").html("Here is the getContact");
    });


});






