$(document).ready(function(){

  // ------- SLIM POPS ------

  // enable click event on menu items and text links
  $('.pop_item').click(function(event){
    event.preventDefault();
    // get href
    var chosen_href = $(event.target).attr('href');
    // call ajax for the slim pop. 
    slimPop(chosen_href, 'slimpop-basicsize');
  });

  // enable click event on slim that's already up
  // document on required since this the markup was loaded by ajax.
  $(document).on("click", ".swap_pop", function(event){
    event.preventDefault();
    // get href
    var chosen_href = $(event.target).attr('href');
    // alert('chosen_href: ' + chosen_href);
    // call ajax for the slim pop. 
    getURL(chosen_href, $('#slimpop-container'));
  });

}); // end doc ready

/* 
*  used by popBox() and..
*/
function slimPop(theURL, displayClass) { 
  // append divs if not present
  if (!$('#slimpop-overlay').length > 0) { // overlay html doesn't exist
    //create HTML markup for lightbox window
    var slimpopOverlay = 
    '<div id="slimpop-overlay" class="hidden"></div>' +
    '<div id="slimpop-container" class="hidden"></div>';
    //insert lightbox HTML into page
    $('body').append(slimpopOverlay);
    // assign close click to overlay
    $('#slimpop-overlay').click(function(event){
      hideBox();    
    });
  }
  // unhide overlay
  $('#slimpop-overlay').removeClass().addClass('unhidden');
  // assign contentDiv for further use
  var contentDiv = $('#slimpop-container');
  // contentDiv will be unhidden by specific classes 
  contentDiv.removeClass().addClass(displayClass); 
  // call Ajax
  getURL(theURL, contentDiv);
}

/* simple hide called by Close link in box, and by hideOverlay, below.
*/
function hideBox() {
  // test for existence of audioPlayer element 
  //if (document.getElementById("audioPlayer")) { 
  //  document.getElementById("audioPlayer").pause();     
  //}   
    
  var contentDiv = $('#slimpop-container');
  // empty content div so it won't briefly show old content on new pop
  contentDiv.html = " ";  
  // hide box.. 
  contentDiv.removeClass().addClass('hidden');
  // ..and darkening overlay
  $('#slimpop-overlay').removeClass().addClass('hidden');
}

// ----------- AJAX ----------

// jQuery Ajax
function getURL(theURL, contentDiv) {
  contentDiv.load(theURL);
}

