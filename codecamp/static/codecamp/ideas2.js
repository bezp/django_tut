$(document).ready(function() {
    // changing the initial logo color from white to green
    $("#greenHover").hover(
        function() {
            $("#greenHover").attr("src", "/static/css/images/bp_logo8_x.png");
        },
        function() {
            $("#greenHover").attr("src", "/static/css/images/bp_logo7_x.png");
        }
    );

    // the sphere with skills
    if (
        !$("#myCanvas").tagcanvas(
            {
                textColour: "#31E981",
                outlineThickness: 0.1,
                outlineColour: "#053451",
                reverse: true,
                depth: 0.8,
                textHeight: 15,
                radiusX: 0.8,
                radiusY: 0.8,
                radiusZ: 0.8,
                textFont: "Arial",
                offsetY: -80,
                maxSpeed: 0.08
            },
            "tags"
        )
    ) {
        // something went wrong, hide the canvas container
        $("#myCanvasContainer").hide();
    }

    // showing the different items 1,2,3,4
    $(".selector").click(function() {
        //    $(".selector").removeClass("active");
        //    $(this).addClass("active");
        var status = $(this).attr("id");
        if (status === "About") {
            $(".item1").removeClass("hidden");
            $(".item2, .item3, .item4").addClass("hidden");
        } else if (status === "Projects") {
            $(".item2").removeClass("hidden");
            $(".item1, .item3, .item4").addClass("hidden");
        } else if (status === "Skills") {
            $(".item3").removeClass("hidden");
            $(".item1, .item2, .item4").addClass("hidden");
        } else if (status === "Contact") {
            $(".item4").removeClass("hidden");
            $(".item1, .item3, .item2").addClass("hidden");
        }
    });
    // showing the active page ppl click on, about,projects,skills,contact
    var header = document.getElementById("myTopnav");
    var xx = header.getElementsByClassName("selector");
    for (var i = 0; i < xx.length; i++) {
        xx[i].addEventListener("click", function() {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";
        });
    }
});

// navbar open close depending on width
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}
