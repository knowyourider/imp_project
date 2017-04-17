// explore jurassic landscape

$(document).ready(function(){
    var textBoxHeightOffset = 15;

    $(document).on("click", ".dinospot", function(event){
        event.preventDefault();

        // get the index of the element selected
        // console.log( $("#hotspot_group g").index($(this).parent()) );
        expoIndex =  $("#hotspot_group g").index($(this).parent());

 
		$('.tooltip').css("opacity", "1");
        // get target element bounding box
        // console.log(" --- bbox width: " + $(event.target)[0].getBBox().width);
        var targetBBox = $(event.target)[0].getBBox();
        // get the target title
        var targetTitle = $(event.target).parent().find("text").html();
        // object name in the "name" element has to match image_name for slide in Admin
        var targetName = $(event.target).parent().find("name").html();
        // set the tooltip and narrative text
        $(".tooltip").html(targetTitle);

        // set the variable for the explanations
        var expos = $(".explanations");
        // clear all visible text
        for (i = 0; i < expos.length; i++) {
          expos[i].style.display = "none"; 
        }
        // set visible for current selection
        // object name in the "name" element has to match image_name for slide in Admin

        console.log(" -- targetName: " + targetName);

        $("#" + targetName).css("display", "block") ;



        // $("#expo-" + targetName).style.display = "block";
        // $("#narrative p[name=expo_1]").style.display = "block";
        // $("#narrative p[1]").style.display = "block";

        // $('td[name^=tcol]')
        // $('explanations[name^=expo_1]').style.display = "block";


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
          top: (matrix.f - (slimOffset.top + textBoxHeight + textBoxHeightOffset -
            $(document).scrollTop())) + "px"
        };

        $('.tooltip').css( styles );

	});

});
