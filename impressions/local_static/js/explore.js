// explore jurassic landscape

$(document).ready(function(){

	$(document).on("click", ".dinospot", function(event){
	    event.preventDefault();

		$('.tooltip').css("opacity", "1");

        // get target element bounding box
        // console.log(" --- bbox width: " + $(event.target)[0].getBBox().width);
        var targetBBox = $(event.target)[0].getBBox();
        // get the target text
        var targetTitle = $(event.target).parent().find("title").html();
        var targetText = $(event.target).parent().find("text").html();
        // set the tooltip text
        $(".tooltip").html(targetTitle);
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
        var matrix = this.getScreenCTM()
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
          top: (matrix.f - (slimOffset.top + textBoxHeight -
            $(document).scrollTop())) + "px"
        };

        $('.tooltip').css( styles );

	});

});
