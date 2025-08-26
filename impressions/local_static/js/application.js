$(document).ready(function(){

  // ------- SLIM POPS ------

  // -- .pop_item --
  // enable click event on menu items and text links
  // "document on" sytntax required since this markup may appear on
  // links loaded by ajax. (at least map dig deeper)
  $(document).on("click", ".pop_item", function(event){
  // $(".pop_item").on("click touchstart", function(event){
    // console.log("--- got to pop_item");
    event.preventDefault();
    // get href
    // use closest -- target may be image in dig deeper gallery
    var chosen_href = $(event.target).closest('a').attr('href');
    var href_split = chosen_href.split('/');    
    // href_split[2] = person, evidence, fastfact, special
    var slimpopSizeClass = href_split[2];

    // console.log(" -- slim class size: " + slimpopSizeClass);
    console.log(" -- href_split length: " + href_split.length);

    // for mobile special and supporting items  then insert "/full" into path
    // e.g. /special/footprint/find-footprints/
    //     0/   1   /   2     /     3         / 4


    if ($('#js-top-navigation-mobile-menu').is(":visible"))  { // in mobile mode
      // use "regular" url which calls full view
        window.location.href = chosen_href;        
    } else {
      // call ajax for the slim pop. (href, size class)
      var ajaxHref = "/" + href_split[1] + "/ajax/" + href_split[2] + "/" + 
        href_split[3] + "/";
      // had this condition to accomodate home/intro having only two elements
      // but ran into trouble testing length bcz most have trailing / but not fast facts
      // var ajaxHref = "/" + href_split[1] + "/ajax/" + href_split[2] + "/";
      // // everything except home Learn more is greater than 4
      // if (href_split.length > 4) {
      //   ajaxHref += href_split[3] + "/";  
      // }
      // e.g. /special/ajax/footprint/find-footprints/
      // console.log(" -- ajaxHref: " + fullHref);

      slimPop(ajaxHref, slimpopSizeClass);  
    }


  });

  // -- .swap_pop --
  // enable click event on slim that's already up
  // "document on" sytntax required since this the markup was loaded by ajax.
  $(document).on("click", ".swap_pop", function(event){
    event.preventDefault();
    // get href
    var chosen_href = $(event.target).attr('href');
    // console.log('chosen_href: ' + chosen_href);
    var href_split = chosen_href.split('/');    
    // var slimpopSizeClass = href_split[2];
    // BTW supporting/base_detail_full also has slimpop-wrapper
    var contentDiv = $('#slimpop-container');
    // resize contentDiv
    contentDiv.removeClass().addClass("slimpop-basic").addClass(href_split[2]); 
    // call ajax for the slim pop. 
    getURL(chosen_href, contentDiv);
  });

  // -- .swap_fullpop --
  // the full-screen version of special slims needs in internal swap
  // via ajax so the the shell retains the correct "back" referrer
  $(document).on("click", ".swap_fullpop", function(event){
    event.preventDefault();
    // get href
    var chosen_href = $(event.target).attr('href');
    // console.log(' ---- chosen_href swap_fullpop: ' + chosen_href);
    // e.g. /special/full/slideshow/orra-landscape/1/

    // var contentDiv = $('#fullpop_content_wrapper');
    // special and supporting use same ajax div
    var contentDiv = $('#fullpop_content_wrapper');
    // var contentDiv = $('#slimpop_wrapper');
    // call ajax for the slim pop.
    getURL(chosen_href, contentDiv);
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
  $(".chapter-nav--dropdown a").click(function(event){ // .mobile
  // $(document).on("click", ".chapter-nav--dropdown a", function(event){
    // event.preventDefault();
    event.stopPropagation();
    // console.log(" --- got chapter-nav-- click");
    $("ol.chapter-subnav").toggle();
  });

  $(document).click( function(){
      $('ol.chapter-subnav').hide();
  });

  // hover in js rather than css to accomodate mobile
  $(".chapter-nav--dropdown").hover(
    function(event){ 
      // console.log(" --- got chapter-nav-- hover on");
      $("ol.chapter-subnav").show();
    }, function(event){
      // console.log(" --- got chapter-nav-- hover off");
      $("ol.chapter-subnav").hide();
    }
  );


  // ------- Story Navigation
  
  // this drops menu on click
  $(".more a").click(function(event){ // .mobile
    // console.log(" -- click on more");
    // event.preventDefault();
    event.stopPropagation();
    // console.log(" --- got chapter-nav-- click");
    $("submenu").toggle();
  });

  $(document).click( function(){
      $('submenu').hide();
  });

  // hover in js rather than css to accomodate mobile
  $("li.more").hover(
    function(event){ 
      // console.log(" --- got story-nav-- hover on");
      $(".submenu").show();
    }, function(event){
      // console.log(" --- got chapter-nav-- hover off");
      $(".submenu").hide();
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

// In application.js, update the page click handler:

$('.item_page').click(function(event){
    event.preventDefault();
    var theURL = $(this).attr('href');
    
    var href_split = theURL.split('/');  
    var link_type = href_split[2];
    var slug = href_split[3];
    var page_suffix = href_split[4];
    
    console.log(" -- href_split length: " + href_split.length);

    // Build zoom path - using static since ZIF files are there now
    var zoomPath = "/static/supporting/evidenceitem/zooms/" + slug;
    
    // Add suffix for document pages (but not artifact primary view)
    if(link_type != "artifact") {
      zoomPath += "-" + page_suffix;
      // Call ajax for new page text
      getURL(theURL, $('#document-text'));
    }
    
    // Add .zif extension
    zoomPath += ".zif";
    
    console.log(" in app js -- zoom path: " + zoomPath);

    // Check if the file exists before trying to set it
    fetch(zoomPath, { method: 'HEAD' })
      .then(response => {
        if (response.ok) {
          Z.Viewer.setImagePath(zoomPath);
        } else {
          console.error("Cannot access ZIF file for page change:", zoomPath);
        }
      })
      .catch(error => {
        // Try anyway in case HEAD requests are blocked
        Z.Viewer.setImagePath(zoomPath);
      });
});


  // ------- SEARCH ------

  // click on checkbox submits form
  $('input[type="checkbox"]').change(function(event){
    console.log('got to checkbox change')
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
    // console.log(" --- society name: " + choiceURL );
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
    // console.log('--- quiz_swap: ' + chosen_href);
    // call ajax for the slim pop. 
    getURL(chosen_href, $('#slimpop-container'));
    // re-enable the buttons
    $(".society_choice").prop("enabled",true);
  });

  // ---- DISCOVERERS VOTE ---
  $(document).on("click", "#discoverers-form .vote", function(event){
    // event.preventDefault();
    var voteeNum = $(this).attr('value')
    // console.log(" --- voteeNum: " + voteeNum );
    constructed_href = 
      "/special/discoverers/discoverers-vote/" + voteeNum + "/";
    // disable and grey-out the voting checkboxes
    $(".vote").prop("disabled",true);
    // call to ajax
    slimPop(constructed_href, "discoverers");  
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
    // console.log("--- attr name: " + contentDiv.attr('id'));
    // make sure we're scrolled to the top
    // in the case of full screen (mobile) the scroll has to operate on 
    // the whole windo
    if (contentDiv.attr('id') == 'fullpop_content_wrapper') {
      $(window).scrollTop( 0 );
    } else {
      contentDiv.animate({ scrollTop: 0 }, 0);    
    }
    // following callback wasn't needed since we're operating on the window.
    // contentDiv.html(data).promise().done(function(){
    //   // console.log(" -- success for html")
    //   // scrollTop works on window, not div
    //   $(window).scrollTop( 0 );
    // });
  }).fail(function(jqXHR) {
    contentDiv.html('<div id="slimpop-wrapper">' + '<p>SlimPop error: ' + 
      jqXHR.status + '</p></div>')
    .append(jqXHR.responseText);
  });
}

