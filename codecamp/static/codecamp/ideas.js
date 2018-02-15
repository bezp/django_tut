



$(document).ready(function() {
        if(!$('#myCanvas').tagcanvas({
          textColour: '#498638',
          outlineColour: '#F8F8F8',
          reverse: true,
          depth: 0.8,
          textHeight: 20,
          maxSpeed: 0.1
        },'tags')) {
          // something went wrong, hide the canvas container
          $('#myCanvasContainer').hide();
        }
      });



