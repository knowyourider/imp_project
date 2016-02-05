$(document).ready(function(){

  // ------- PEOPLE MENU ------

  // enable click event on menu items
  $('.pop-item').click(function(event){
  //$('.pop-item').live("click", function(event){
  //$(document).on("click", ".pop-item", function(event){
    event.preventDefault();
    // get params from href
    var chosen_href = $(event.target).attr('href');
    //var href_split = chosen_href.split('/');  
    // app_namespace = href_split[1]  
    // short_name = href_split[2]  
    // form local url
    //var theURL = "/" + href_split[1] + "/" + href_split[2] + "/";
    //alert('url for slimpop: ' + chosen_href); 
    // call ajax for the slim pop. 
    slimPop(chosen_href, 'pop_connection');
  });

}); // end doc ready

/* 
*  used by popBox() and..
*/
function slimPop(theURL, displayClass) { 
  // append divs if not present
  if (!$('#lbOverlay').length > 0) { // overlay html doesn't exist
    //create HTML markup for lightbox window
    var lbOverlay = 
    '<div id="lbOverlay" class="hidden"></div>' +
    '<div id="ajax_wrapper" class="hidden"></div>';
    //insert lightbox HTML into page
    $('body').append(lbOverlay);
    // assign close click to overlay
    $('#lbOverlay').click(function(event){
      hideBox();    
    });
  }
  // unhide overlay
  $('#lbOverlay').removeClass().addClass('unhidden');
  // assign contentDiv for further use
  var contentDiv = $('#ajax_wrapper');
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
    
  var contentDiv = $('#ajax_wrapper');
  // empty content div so it won't briefly show old content on new pop
  contentDiv.html = " ";  
  // hide box.. 
  contentDiv.removeClass().addClass('hidden');
  // ..and darkening overlay
  $('#lbOverlay').removeClass().addClass('hidden');
}

// ----------- AJAX ----------

// jQuery Ajax
function getURL(theURL, contentDiv) {
  contentDiv.load(theURL);
}

