// explore jurassic landscape
var textBoxHeightOffset = 15;

$(document).ready(function(){

    // hover in js rather than css to accomodate mobile
    $(".dinospot").hover(function(event){ 
        // console.log(" --- got to hover on");
            // $(event.target).css("fill-opacity", "0.5");
            $(event.target).addClass("dino-roll");
            setTooltip($(event.target), this);
        }, function(event){
            // console.log(" --- got chapter-nav-- hover off");
            // $(event.target).css("fill-opacity", "0");
            $(event.target).removeClass("dino-roll");
            $('.tooltip').css("opacity", "0");
        }
    );

    // since this is loaded by the slim (at the bottom of the html)
    // we don't want the $(document).on syntax for the event listener
    $(".dinospot").on("click", function(event){
        event.preventDefault();

        // set tooltip
        setTooltip($(event.target), this);
        // remove any standing sticky highlights 
        $(".dinospot").removeClass("dino-stick");
        // set sticky highlight
        $(event.target).addClass("dino-stick");

        var targetName = $(event.target).parent().find("name").html();

        // set the variable for the explanations
        var expos = $(".explanations");
        // clear all visible text
        for (i = 0; i < expos.length; i++) {
          expos[i].style.display = "none"; 
        }
        // console.log(" -- targetName: " + targetName);

        // set expo text visible for current selection
        // object name in the "name" element has to match image_name for slide in Admin
        $("#" + targetName).css("display", "block") ;
        // BTW, the following doesn't work consistently:
        // $("#-" + targetName).style.display = "block";


	});

}); // end document ready

function setTooltip (eventTarget, thisDinospot) {
    $('.tooltip').css("opacity", "1");
    // get target element bounding box
    // console.log(" --- bbox width: " + $(event.target)[0].getBBox().width);
    var targetBBox = eventTarget[0].getBBox();
    // get the target title
    var targetTitle = eventTarget.parent().find("text").html();
    // object name in the "name" element has to match image_name for slide in Admin

    // set the tooltip and narrative text
    $(".tooltip").html(targetTitle);

    console.log(" -- hover targetTitle: " + targetTitle);

    // get the height of box with current text
    var textBoxHeight = $(".tooltip").height();

    // console.log(" -- textbox height: " + $(".tooltip").height());
    // console.log(" -- text: " + targetTitle);
    
    //for the HTML tooltip, we're not interested in a
    //transformation relative to an internal SVG coordinate
    //system, but relative to the page body
    
    //We can't get that matrix directly,
    //but we can get the conversion to the
    //screen coordinates.
    // using svg getBBox() for path location
    // var matrix = this.getScreenCTM()
    var matrix = thisDinospot.getScreenCTM()
            .translate(targetBBox.x,
             targetBBox.y);

    // jQuery offset for slimp-wrapper relative to page
    // We'll need to subract doc scrollTop to compensate for scroll
    var slimOffset = $('#slimpop-wrapper').offset();

    // console.log(" --- slim left: " + slimOffset.left);
    // console.log(" --- slim top: " + slimOffset.top);
    // console.log(" --- scrolltop: " + $(document).scrollTop());
    
    var styles = {
      left : (matrix.e - slimOffset.left) + "px",
      top: (matrix.f - (slimOffset.top + textBoxHeight + textBoxHeightOffset -
        $(document).scrollTop())) + "px"
    };

    $('.tooltip').css( styles );

}
