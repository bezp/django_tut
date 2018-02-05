var channels = ["freecodecamp", "riotgames", "ESL_SC2"];
var showingChannels = [];
function getInfo() {
  channels.forEach(function(channel) {
    function makeLink(name) {
      return (
        "https://wind-bow.glitch.me/twitch-api/streams/" + name + "?callback=?"
      );
    }
    showingChannels.push(channel);
    $.getJSON(makeLink(channel), function(data) {
      var status, // stream title   or offline
        name, //stream name ex.SparcMac
        logo, //stream pic
        game, // LoL
        url,
        show; // see it depending on button
      if (data.stream !== null) {
        show = "on";
        status = data.stream.channel.status;
        name = data.stream.channel.display_name;
        logo = data.stream.channel.logo;
        game = data.stream.channel.game;
        url = data.stream.channel.url;
        //                console.log(status, name, logo, game);
      } else {
        show = "off";
        game = "Offline";
        status = "";
        name = channel;
        url = "https://www.twitch.tv/" + channel;
        logo = "https://www.twitch.tv/p/assets/uploads/glitch_474x356.png";
      }

      html =
        '<div class="row ' +
        show +
        '"><div class="col-xs-2 col-sm-1" id="icon">' +
        '<a href="' +
        url +
        '" target="_blank">' +
        '<img src="' +
        logo +
        '" class="logo"></div><div class="col-xs-10 col-sm-3" id="name">' +
        "</a></div>" +
        "<div>" +
        name +
        "</div>" +
        '<div class="col-xs-7 col-sm-7 col-md-offset-3" id="streaming">' +
        game +
        ': <span class="hidden-xs">' +
        status +
        "</span></div></div>";
      show =
        show === "on"
          ? $("#display").prepend(html)
          : $("#display").append(html);
    });
  });
}

$(document).ready(function() {
  getInfo();
  $(".activeAll").css("color", "red");
  $(".selector").click(function() {
    //    $(".selector").removeClass("active");
    //    $(this).addClass("active");
    var status = $(this).attr("id");
    if (status === "all") {
      $(".on, .off").removeClass("hidden");
    } else if (status === "online") {
      $(".on").removeClass("hidden");
      $(".off").addClass("hidden");
    } else {
      $(".off").removeClass("hidden");
      $(".on").addClass("hidden");
    }
  });
  //change color depending on what they pick
  $(".activeAll").click(function(e) {
    $(e.target).css("color", "red");
    $(".activeOnline").css("color", "black");
    $(".activeOffline").css("color", "black");
  });
  $(".activeOnline").click(function(e) {
    $(e.target).css("color", "red");
    $(".activeAll").css("color", "black");
    $(".activeOffline").css("color", "black");
  });
  $(".activeOffline").click(function(e) {
    $(e.target).css("color", "red");
    $(".activeAll").css("color", "black");
    $(".activeOnline").css("color", "black");
  });
});

//they can look up channels
window.onload = function() {
  document.getElementById("a").onclick = function() {
    myFunction();
  };
  function myFunction() {
    userSearch = document.getElementById("textbox_id").value;
    var unnecessary =
      $.inArray(userSearch, channels) === -1
        ? channels.push(userSearch)
        : console.log("exists");
    var unnecessary2 =
      $.inArray(userSearch, showingChannels) === -1
        ? addNew(userSearch)
        : console.log("in list");
  }
};

function addNew(userSearch) {
  function makeLink(userSearch) {
    return (
      "https://wind-bow.glitch.me/twitch-api/streams/" +
      userSearch +
      "?callback=?"
    );
  }
  showingChannels.push(userSearch);
  $.getJSON(makeLink(userSearch), function(data) {
    var status, // stream title   or offline
      name, //stream name ex.SparcMac
      logo, //stream pic
      game, // LoL
      url,
      show; // see it depending on button
    if (data.stream !== null) {
      show = "on";
      status = data.stream.channel.status;
      name = data.stream.channel.display_name;
      logo = data.stream.channel.logo;
      game = data.stream.channel.game;
      url = data.stream.channel.url;
      //                console.log(status, name, logo, game);
    } else {
      show = "off";
      game = "Offline";
      status = "";
      name = userSearch;
      url = "https://www.twitch.tv/" + userSearch;
      logo = "https://www.twitch.tv/p/assets/uploads/glitch_474x356.png";
    }

    html =
      '<div class="row ' +
      show +
      '"><div class="col-xs-2 col-sm-1" id="icon">' +
      '<a href="' +
      url +
      '" target="_blank">' +
      '<img src="' +
      logo +
      '" class="logo"></div><div class="col-xs-10 col-sm-3" id="name">' +
      "</a></div>" +
      "<div>" +
      name +
      "</div>" +
      '<div class="col-xs-7 col-sm-7 col-md-offset-3" id="streaming">' +
      game +
      ': <span class="hidden-xs">' +
      status +
      "</span></div></div>";
    show =
      show === "on" ? $("#display").prepend(html) : $("#display").append(html);
  });
}
