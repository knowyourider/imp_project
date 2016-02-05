$(document).ready(function(){

  // ------- PEOPLE MENU ------

  // enable click event on menu items
  $('#pop-list > li > a').click(function(event){
    event.preventDefault();
    // get params from href
    var chosen_href = $(event.target).attr('href');
    var href_split = chosen_href.split('/');  
    // app_namespace = href_split[1]  
    // short_name = href_split[2]  
    // form local url
    var theURL = "/" + href_split[1] + "/" + href_split[2] + "/";
    alert('url for slimpop: ' + theURL); 
  });


}); // end doc ready
