

$(document).ready(function() {

var quote;
var author;

    function getNewQuote() {
        $.ajax({
            url:'http://api.forismatic.com/api/1.0/',
            jsonp: 'jsonp',
            dataType: 'jsonp',
            data: {
                method: 'getQuote',
                lang: 'en',
                format: 'jsonp'
            },
            success: function(response) {
//                console.log(response.quoteText);
                quote = response.quoteText;
                author = response.quoteAuthor;

                $('#quote').text(quote);
                if (author) {
                    $('#author').text('said by ' + author);
                } else {
                    $('#author').text('-unknown');
                }
            }
        });
    }



getNewQuote();  // calls to the function for an api call when page first loads

$('.get-quote').on('click', function(event) {
    event.preventDefault();     // stops page from refreshing to top
    getNewQuote();
});


$('.share-quote').on('click', function(event) {
    event.preventDefault();
    window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(quote + '--' + author));
});


});
