

$(document).ready(function() {

var userSearch;


var pageId = [];
var pageTitle = [];
var pageDesc = [];
var goodUrl = "https://en.wikipedia.org/w/api.php?format=json&action=query&generator=search&gsrnamespace=0&gsrlimit" +
"=5&prop=pageimages|extracts&pilimit=max&exintro&explaintext&exsentences=4&exlimit=max&gsrsearch="
// gets the input from user to search...
console.log(goodUrl);
document.getElementById("a").onclick = function() {myFunction()};

    function myFunction() {
    userSearch = document.getElementById('textbox_id').value;
        $.ajax({
            url : goodUrl + userSearch,
            dataType : 'jsonp',
            success: function(response) {
            if (response.query.pages) {
            var x = response.query.pages;
            console.log(x);

            var ss = 1;
            while (ss < 6) {
                for (var y in x) {
                    $("#article" + ss).html(
                    '<a href="https://en.wikipedia.org/?curid=' +
                    y +
                    '" target="_blank">' +
                    '<h2>' +
                     x[y].title +
                    '</h2>' +
                     '<p>' + x[y].extract +
                      '</p>' +
                     '</a>' +
                     '<hr>'
                     );
                    ss += 1;
                }
            }
            }
            }
        });
    }
});











