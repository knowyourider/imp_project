$(document).ready(function(){

	$("#intro_slideshow > div:gt(0)").hide();

	setInterval(function() { 
	  $('#intro_slideshow > div:first')
	    .fadeOut(1000)
	    .next()
	    .fadeIn(1000)
	    .end()
	    .appendTo('#intro_slideshow');
	},  3000);

}); // end doc ready
