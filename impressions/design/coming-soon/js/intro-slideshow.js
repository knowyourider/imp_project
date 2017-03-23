$(document).ready(function(){

    var slides = $(".mySlides");
    var dots = $(".dot");
    // var slides = document.getElementsByClassName("mySlides");
    // var dots = document.getElementsByClassName("dot");
	var timer;
	var slideIndex = 0;
	showSlides();


	function showSlides() {
	    slideIndex++;	
		showSingle(slideIndex);	    
	    // set the timer
	    timer = setTimeout(showSlides, 7000); // 1000 = a second
	}

	function showSingle(n) {
		var i;
	    // restart count if at end
		if (n > slides.length) {slideIndex = 1} 
		// if 0 (how?) go to end
		if (n < 1) {slideIndex = slides.length}
		// hide all slides
		for (i = 0; i < slides.length; i++) {
		  slides[i].style.display = "none"; 
		}
	    // clear the dot highlights  
		for (i = 0; i < dots.length; i++) {
		  dots[i].className = dots[i].className.replace(" active", "");
		}
	    // show the current slide
		slides[slideIndex-1].style.display = "block"; 
	    // show the current dot
		dots[slideIndex-1].className += " active";
	}

	// set event listener for dots
	$('.dot').click(function(event){
		// event.preventDefault();
	    var slide_num = $(event.target).attr('name');
	    // Stop timer
	    clearTimeout(timer);
	    // set index
	    slideIndex = slide_num;
	    // show single
	    showSingle(slide_num);
	});

});
