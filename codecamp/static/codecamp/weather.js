


$(document).ready(function() {

var key = 'AIzaSyCyO5h_y76zYSFqhmSFUwciUjG0jEp56s0';
var latitude;
var longitude;

var weatherMain;
var weatherDescription;
var weatherIcon;

var mainTemp;
var mainPressure;
var mainHumidity;
var mainTempMin;
var mainTempMax;
var mainSeaLevel;
var mainGroundLevel;

var windSpeed;
var windDegree;



  if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;

    $("#data").html("latitude: " + latitude + "<br>longitude: " + longitude);


    if (latitude && longitude) {
        $.ajax({
            url:'https://fcc-weather-api.glitch.me//api/current?lon=' + longitude + '&lat=' + latitude,
            dataType: 'json',
//            jsonp: 'jsonp',
            success: function(response) {
                weatherMain = response.weather[0].main;
                weatherDescription = response.weather[0].description;
                weatherIcon = response.weather[0].icon;
                mainTemp = response.main.temp;
                mainPressure = response.main.pressure;
                mainHumidity = response.main.humidity;
                mainTempMin = response.main.temp_min;
                mainTempMax = response.main.temp_max;

                $("#data2").html("weatherMain: " + weatherMain + "<br>weatherDescription: " + weatherDescription);
                $("#data3").html("weatherIcon: <img src='" + weatherIcon + "alt='icon_pic'><br>mainTemp: " + mainTemp);
                $("#data4").html("mainPressure: " + mainPressure + "<br>mainHumidity: " + mainHumidity +'%');
                $("#data5").html("mainTempMin: " + mainTempMin + "<br>mainTempMax: " + mainTempMax);

                $(".change-temp").bind('click', function() {
                    var celTemp = mainTemp;
                    var farTemp = celTemp * 9/5 + 32;
                    $("#tempFar").html(farTemp);
                    $("#tempCel").html(celTemp);
                    $("#switchTemppp").html($("#switchTemppp").html() == celTemp ? farTemp : celTemp);
                });
            }
        });
    }
    

    if (longitude && latitude) {
        $.ajax({
            url:'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + latitude + ',' + longitude + '&key=' +key,
            dataType: 'json',
//            cache: false,
//            type:'GET',
//            crossDomain: true,
            success: function(response) {
//                console.log(response.results[0].address_components[3].long_name);
//                var y = JSON.stringify(response);
//                var yy = JSON.parse(y);
                $("#data55").html(response.results[0].address_components[3].long_name);
                $("#data555").html(response.results[0].address_components[5].long_name);
            },
        });
    }

  });


}




});


















