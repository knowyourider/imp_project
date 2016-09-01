$(document).ready(function(){

  var numCorrect = 0;
  var numOfCorrect = 3;
  var feedback = $("#feedback");
  var score = $("#score");

  score.html("found: " + numCorrect + " of " + numOfCorrect);

  $(document).on("click", ".hotspot", function(event){
    // event.preventDefault();
    // store target
    var chosen = $(event.target);
    // get name attribute
    var chosenCorrectness = chosen.attr('name'); // xlink:href
    // tally
    if (chosenCorrectness=="correct") {
      numCorrect++;
    }
    // conditional feedback
    if (numCorrect >= numOfCorrect) {
      // conslole.log("got all: " +  numCorrect); 
      score.html("found: " + numCorrect + " of " + numOfCorrect);
      feedback.html("Found them all! ");
    } else {
      // conslole.log("got one: " + chosenCorrectness + " numCorrect: " + $("#feedback").html()); 
      score.html("found: " + numCorrect + " of " + numOfCorrect);
      feedback.html("found one! ");
    }
    // can't use addClass for svg, use attr
    chosen.attr("class", "hotspot hotspot_correct");

  });

  $(document).on("click", ".show", function(event){
    event.preventDefault();
    // can't use addClass for svg, use attr
    $("#hotspot_group").children().attr("class", "hotspot hotspot_correct");
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



}); // end doc ready


