$(document).ready(function(){

  var numCorrect = 0;
  var numOfCorrect = 3; // needs to be correct number for image included by template
  var feedback = $("#feedback");
  var score = $("#score");

  score.html("found: " + numCorrect + " of " + numOfCorrect);

  // set initial image
  // currently set by include in template instead
  // getURL("/supporting/special/find-footprints/grallator/", $('#svg_wrapper'));


  $(document).on("click", ".hotspot", function(event){
    // event.preventDefault();
    // store target
    var chosen = $(event.target);
    // get name attribute
    var chosenCorrectness = chosen.attr('name'); // xlink:href
    // tally
    if (chosenCorrectness=="correct" && numCorrect < numOfCorrect) {
      numCorrect++;
    }
    // conditional feedback
    if (numCorrect >= numOfCorrect) {
      // console.log("got all: " +  numCorrect); 
      score.html("found: " + numCorrect + " of " + numOfCorrect);
      feedback.html("Found them all! ");
    } else {
      // console.log("got one: " + chosenCorrectness + " numCorrect: " + $("#feedback").html()); 
      // console.log("index of this element: " + chosen.index()); 
      score.html("found: " + numCorrect + " of " + numOfCorrect);
      feedback.html("found one! ");
    }
    // can't use addClass for svg, use attr
    // highlight the footprint, offset by the numOfCorrect
    var indexOffset = chosen.index() - numOfCorrect + 1;
    $("#hotspot_group path:nth-child(" + indexOffset + ")").attr("class", 
        "footprint footprint_correct");
    // chosen.attr("class", "hotspot hotspot_correct");

  });

  $(document).on("click", ".show", function(event){
    event.preventDefault();
    // can't use addClass for svg, use attr
    // $("#hotspot_group").children().attr("class", "footprint footprint_correct");
    $("#hotspot_group path").attr("class", "footprint footprint_correct");
  });

  $(document).on("click", "#document", function(event){
    var eventPageX = event.pageX;
    var baseImage = $(event.target);
    baseImageX = baseImage.attr('x');

    // can I get px for left edge of doc area? for offset
    //$(.doc-area).css();

    feedback.html("Sorry, not a footprint. "); 

    // feedback.html("NAFP. eventPageX: " + eventPageX + " baseImage x: " + baseImageX + 
    //   " doc-area css: "); // + $(.doc-area).css());

  });


  $(document).on("click", ".switch_interactive", function(event){
    event.preventDefault();
    // get target href
    var chosen_href = $(event.target).attr('href');
    var href_split = chosen_href.split('/');    
    console.log('href_split[0]: ' +  href_split[0]);
    // e.g. /grallator/3
    // clear num correct
    numCorrect = 0;
    numOfCorrect = href_split[1];
    // reset score and feedback text
    feedback.html("Feedback..."); 
    score.html("found: " + numCorrect + " of " + numOfCorrect);    // get href
    // call ajax for the slim pop. 
    getURL("/supporting/special/find-footprints/" + href_split[0] + "/", $('#svg_wrapper'));
   
  });



}); // end doc ready


