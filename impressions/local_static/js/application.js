$(document).ready(function(){

  // ------- SLIM POPS ------

  // enable click event on menu items and text links
  // $('.pop_item').click(function(event){
  $(document).on("click touchstart", ".pop_item", function(event){
    // console.log("--- got to pop_item");
    event.preventDefault();
    // get href
    // use closest -- target may be image in dig deeper gallery
    var chosen_href = $(event.target).closest('a').attr('href');
    var href_split = chosen_href.split('/');    
    // href_split[2] = person, evidence, fastfact, special
    var slimpopSizeClass = href_split[2];

    // test mobile for find-footprints and test state of mobile menu
    if (href_split[3] == "find-footprints" && $('#js-top-navigation-mobile-menu').is(":visible")) {
      var fullHref = "/supporting/fullspecial/" + href_split[3] + "/";
      window.location.href = fullHref;
    } else {
      // call ajax for the slim pop. (href, size class)
      slimPop(chosen_href, slimpopSizeClass);  
    }
  });

  // enable click event on slim that's already up
  // document on required since this the markup was loaded by ajax.
  $(document).on("click", ".swap_pop", function(event){
    event.preventDefault();
    // get href
    var chosen_href = $(event.target).attr('href');
    console.log('chosen_href: ' + chosen_href);
    var href_split = chosen_href.split('/');    
    // var slimpopSizeClass = href_split[2];
    var contentDiv = $('#slimpop-container');
    // resize contentDiv
    contentDiv.removeClass().addClass("slimpop-basic").addClass(href_split[2]); 
    // call ajax for the slim pop. 
    getURL(chosen_href, contentDiv);
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
  // This is happening on page load
  // Assign var menuToggle to stand for the element js-top-navigation-mobile-menu
  // and remove (unbind) any previous event handler
  var menuToggle = $('#js-top-navigation-mobile-menu').unbind();
  // Here, on page load, we're going to remove the class show
  // .. if we happen to be in mobile mode, this will make sure the menu isn't dropped down
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
      if($('#js-2nd-navigation-menu').is(':hidden')) {
        $('#js-2nd-navigation-menu').removeAttr('style');
      }
    });
  });

  // ------- Chapter Navigation

  // this drops menu on click
  // $(".chapter-nav--dropdown a").click(function(event){ // .mobile
  $(document).on("click", ".chapter-nav--dropdown a", function(event){
    // event.preventDefault();
    event.stopPropagation();
    // console.log(" --- got chapter-nav-- click");
    $("ol.chapter-subnav").toggle();
  });

  $(document).click( function(){
      $('ol.chapter-subnav').hide();
  });

  // try js hover instead of css
  $(".chapter-nav--dropdown").hover(
    function(event){ 
      // console.log(" --- got chapter-nav-- hover on");
      $("ol.chapter-subnav").show();
    }, function(event){
      // console.log(" --- got chapter-nav-- hover off");
      $("ol.chapter-subnav").hide();
    }
  );


  // --- ARTIFACTS AND DOCUMENTS ------------

  // ------- Docment text show/hide ------
  // use .on syntax since element is loaded by ajax
  $(document).on("click", "#toggle-transcription", function(event){
  // $("#toggle-transcription").click(function() {
    // console.log(" -- got to toggle-transcription");
    $("#document-text").slideToggle();
    if ( $(this).text() == "Show Transcription") {
      $(this).text('Hide Transcription') 
    } else {
      $(this).text('Show Transcription') 
    }
  });

  // ------- Docment paging ------

  $(document).on("click", ".item_page", function(event){
    event.preventDefault();
    // highlight current selection
    $("#document-paging--list li").removeClass('document-paging--selected');
    $(event.target).parent().addClass('document-paging--selected'); 

    // get params from href
    theURL = $(event.target).attr('href');
    // e.g. /documents/montague_letter/p001/36608
    var href_split = theURL.split('/');  
    var link_type = href_split[2]  
    var slug = href_split[3]
    var page_suffix = href_split[4]

    console.log('href:' + theURL);

    // set first item selected
    // change zoomify image
    var zoomPath = "/static/supporting/evidenceitem/zooms/" + slug;

    // avoid adding suffix for special case of artifact primary view
    // and don't bother trying to change the document text
    if(link_type != "artifact") {
      zoomPath += "-" + page_suffix;
      // call ajax for new page text. use href as-is.
      getURL(theURL, $('#document-text'));
    }
    console.log('zoom path:' + zoomPath);

    Z.Viewer.setImagePath(zoomPath);

  });


  // ------- SEARCH ------

  // click on checkbox submits form
  $('input[type="checkbox"]').change(function(event){
    // each time a new box is checked we should reset to page 1
    // (if nothing else there may not be a page 2 in new result)
    $('#search-form').find('[type=hidden][name=page]').val('1')
    $('#search-form').submit()   
  });

  // ------- pagination ------

  // Turn page selection into form submit
  // q (and other?) parameters are in the form and will be submited? 
  // document.on syntax required since this the markup was loaded by ajax.
  $(document).on("click", "#paging", function(event){
    event.preventDefault();
    // get the page number from href
    var chosen_href = $(event.target).closest('li').children('a').attr('href');
    var href_split = chosen_href.split('=');  
    // page number = href_split[1]  
    // alert('in page nav. page num: ' + href_split[1]); 
    // set the page number in the hidden field
    $('#search-form').find('[type=hidden][name=page]').val(href_split[1])
    $('#search-form').submit()
  });

  // link to clear search
  $('#clear').click(function(event){
    event.preventDefault();
    var searchForm = $('#search-form')
    // Clear entire form
    $('input[name="q"]').val('')
    // searchForm.find('input:text').val('');
    searchForm.find('input:checkbox')
         .removeAttr('checked').removeAttr('selected');
    // submit
    searchForm.submit()
    
  });

  // ------ SPECIAL FEATURES -------

  // ------ SOCIETY ---
  // can't be loaded as a script by the slimpop because it could get loaded multiple times
  // set_society_choice();
  $(document).on("click touchstart", ".society_choice", function(event){
    event.preventDefault();
    var choiceURL = $(this).attr('name')
    // var choice = $(event.target).val()
    console.log(" --- society name: " + choiceURL );
    // call to ajax
    getURL(choiceURL, $('#society_feedback'));
    // disable and grey-out the buttons
    $(".society_choice").prop("disabled",true);
  });

  // version of swap_pop just for the society quiz
  // need to re-enable .society_choice
  $(document).on("click", ".quiz_swap", function(event){
    event.preventDefault();
    // get href
    var chosen_href = $(event.target).attr('href');
    console.log('--- quiz_swap: ' + chosen_href);
    // call ajax for the slim pop. 
    getURL(chosen_href, $('#slimpop-container'));
    // re-enable the buttons
    $(".society_choice").prop("enabled",true);
  });

  // ---- DISCOVERERS VOTE ---
  $(document).on("click", "#discoverers-form .vote", function(event){
    event.preventDefault();
    var voteValue = $(this).attr('value')
    // var choice = $(event.target).val()
    console.log(" --- vote: " + voteValue );
    // Add vote value next
    constructed_href = 
      "/special/discoverers/discoverers-vote/" + voteValue + "/";
    // call to ajax
    slimPop(constructed_href, "discoverers");  
    // getURL(choiceURL, $('#society_feedback'));
    // // disable and grey-out the buttons
    // $(".society_choice").prop("disabled",true);
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
