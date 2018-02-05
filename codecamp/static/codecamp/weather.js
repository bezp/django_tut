$(document).ready(function() {
  var key = "AIzaSyCyO5h_y76zYSFqhmSFUwciUjG0jEp56s0";
  var latitude;
  var longitude;

  var weatherMain;
  var weatherIcon;

  var mainTemp;
  var mainHumidity;

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      latitude = position.coords.latitude;
      longitude = position.coords.longitude;

      if (latitude && longitude) {
        $.ajax({
          url:
            "https://fcc-weather-api.glitch.me//api/current?lon=" +
            longitude +
            "&lat=" +
            latitude,
          dataType: "json",
          //            jsonp: 'jsonp',
          success: function(response) {
            weatherMain = response.weather[0].main;
            weatherIcon = response.weather[0].icon;
            mainTemp = response.main.temp;
            mainHumidity = response.main.humidity;

            $("#data2").html(weatherMain);
            if (weatherIcon) {
              $("#weatherIcon").html(
                "<img src='" + weatherIcon + "' alt=icon_pic'>"
              );
            } else {
              $("#weatherIcon").html("");
            }
            $("#data3").html("<br>Humidity: " + mainHumidity + "%");
            $("#tempConvert").html(mainTemp.toFixed(0) + " °C");
            $(".change-temp").bind("click", function() {
              var celTemp = mainTemp.toFixed(0);
              var farTemp = (celTemp * 9 / 5 + 32).toFixed(0); // tofixed = 0 decimal points
              $("#tempConvert").html(
                $("#tempConvert").html() == farTemp ? celTemp : farTemp
              );
              $("#tempConvertCF").html(
                $("#tempConvertCF").html() == "°F" ? "°C" : "°F"
              );
            });
          }
        });
      }

      if (longitude && latitude) {
        $.ajax({
          url:
            "https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
            latitude +
            "," +
            longitude +
            "&key=" +
            key,
          dataType: "json",
          //            cache: false,
          //            type:'GET',
          //            crossDomain: true,
          success: function(response) {
            //                console.log(response.results[0].address_components[3].long_name);
            //                var y = JSON.stringify(response);
            //                var yy = JSON.parse(y);
            $("#dataCity").html(
              response.results[0].address_components[3].long_name
            );
            $("#dataCountry").html(
              response.results[0].address_components[5].long_name
            );
          }
        });
      }
    });
  }
});
