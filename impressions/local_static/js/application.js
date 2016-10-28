$(document).ready(function(){

  // ------- SLIM POPS ------

  // enable click event on menu items and text links
  // $('.pop_item').click(function(event){
  $(document).on("click", ".pop_item", function(event){
    event.preventDefault();
    // get href
    // use closest -- target may be image in dig deeper gallery
    var chosen_href = $(event.target).closest('a').attr('href');
    var href_split = chosen_href.split('/');    
    // href_split[2] = person, evidence, fastfact, special
    // call ajax for the slim pop. (href, size class)
    slimPop(chosen_href, href_split[2]);
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

  // scroll right for dig deeper
  $(document).on("click", ".go-to-deeper", function(event){
    event.preventDefault();

    //window.scrollTo(500, 0);
    var xscroll = 100;
    var scrollspeed = 20;
    // window.scrollBy(0,-9000);//initial scroll to the top of the page
    for (var iscroll=0; iscroll < xscroll; iscroll++){
        setTimeout('window.scrollBy(' + iscroll + ', 0)',scrollspeed * iscroll);
    }
  });

  // ---------- NAVIGATION ----------
  // Assign var menuToggle to stand for the element js-top-navigation-mobile-menu
  var menuToggle = $('#js-top-navigation-mobile-menu').unbind();
  // Here, on page load, we're going to remove the class show
  // the following re-show the menus after transition from mobile to large screen
  $('#js-top-navigation-menu').removeClass("show");
  $('#js-2nd-navigation-menu').removeClass("show");
  
  // this adds click "listener" to the mobile MENU link
  menuToggle.on('click', function(e) {
    e.preventDefault();
    // toggle the primary mobile menu down (if it's up) and up (if already down)
    $('#js-top-navigation-menu').slideToggle(function(){
      // if css media query has hidden the full menu, then remove "full" style
      // so that we get the plain list for mobile
      if($('#js-top-navigation-menu').is(':hidden')) {
        $('#js-top-navigation-menu').removeAttr('style');
      }
    });
    // toggle the secondary mobile menu down (if it's up) and up (if already down)
    $('#js-2nd-navigation-menu').slideToggle(function(){
      // if css media query has hidden the full menu, then remove "full" style
      // so that we get the plain list for mobile
      if($('#js-2nd-navigation-menu-navigation-menu').is(':hidden')) {
        $('#js-2nd-navigation-menu').removeAttr('style');
      }
    });
  });

}); // end doc ready

/* 
*  used by popBox() and..
*/
function slimPop(theURL, sizeClass) { 
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
  } else { // clear the container -- otherwise previous content flashes by
    $('#slimpop-overlay').html = " ";
  }
  // unhide overlay
  $('#slimpop-overlay').removeClass().addClass('unhidden');
  // assign contentDiv for further use
  var contentDiv = $('#slimpop-container');
  // contentDiv will be unhidden by specific classes 
  contentDiv.removeClass().addClass("slimpop-basic").addClass(sizeClass); 
  // call Ajax
  getURL(theURL, contentDiv);
}

/* simple hide called by Close link in box, and by hideOverlay, below.
*/
function hideBox() {
  // test for existence of audioPlayer element 
  if ($('audio')) {
    $('audio').trigger("pause");
  }
  if ($('video')) {
    $('video').trigger("pause");
  }
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
  //contentDiv.load(theURL);
  // using .get instead of .load so that I can catch errors, especially 404
  // requestData,?
  $.get(theURL, function(data) {  
    contentDiv.html(data);
    // make sure we're scrolled to the top
    contentDiv.animate({ scrollTop: 0 }, 0);
  }).fail(function(jqXHR) {
    contentDiv.html('<div id="slimpop-wrapper">' + '<p>SlimPop error: ' + 
      jqXHR.status + '</p></div>')
    .append(jqXHR.responseText);
  });
}
