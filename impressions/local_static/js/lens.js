var canvas;
var ctx;
var statusDiv;

var isMouseDown = false;

// Canvas Dimensions
var cw = 0; // 850
var ch = 0; // 1327

// Puck Dimensions (and Half thereof)
var pw = 300;
var ph = 180;
var pw2 = 0;
var ph2 = 0;

// Puck Position
var px = 50;
var py = 100;

// cursor offset relative to the puck
var cx = 0;
var cy = 0;

// Attr:Actual dimensions Scale
var sx = 1.0;
var sy = 1.0;

// div offset -- left and top edge of where mouse is active over puck
// may have only been necessary in elaborate canvas placement in Jernegan
var divOffsetLeft = 0; // 428
var divOffsetTop  = 0; //60

// new
var textImg;

$(document).ready(function(){


  // -------- lens/canvas ---------
  // $('.pop_item').click(function(event){
  $(document).on("click", "#startLens", function(event){
    event.preventDefault();
    startLens();
  });



	function startLens() {
		
		// lay down the manuscript as the background
		var msc=document.getElementById("msCanvas");
		var msCtx=msc.getContext("2d");
		
		var msImg = new Image();
		msImg.onload = function(){
			msCtx.drawImage(msImg,0,0);
			//msCtx.fillStyle="#999999";
			//msCtx.fillRect(0,0,200,125);
			
			//msCtx.clearRect(40, 40, 130, 100);
			
		};
		// path is relative to the page on which this operates, not this js file
		msImg.src = 'images/indenture-lens-image.jpg';
		
		
		// set up dragable rectangle on text canvas
	    canvas = document.getElementById("textCanvas");
	    ctx = canvas.getContext("2d");
	    statusDiv = document.getElementById("statusDiv");

		// don: try image instead of drawing rectangle
		textImg = new Image();
		textImg.onload = function(){
			// context.drawImage(img,sx,sy,swidth,sheight,x,y,width,height);
			
			//ctx.drawImage(textImg,100,100,200,125,100,100,200,125);
			
		};
		textImg.src = 'images/indenture-lens-text.jpg';
		

	    cw = canvas.width;
	    ch = canvas.height;

	    // get the scale based on actual width;
	    sx = cw / canvas.offsetWidth;
	    sy = ch / canvas.offsetHeight;

	    // Rescale the puck
	    pw = pw * sx;
	    ph = ph * sy;
	    pw2 = pw/2;
	    ph2 = ph/2;

	    // Rescale the puck position
	    px = px * sx;
	    py = py * sy;

	    statusDiv.innerHTML = "canvas w,h:" + canvas.width + "," + canvas.height
	                     + "; Actual:" + canvas.offsetWidth + "," + canvas.offsetHeight
	                    + "; Scale:" + sx + "," + sy
	                     + "; Puck:" + pw + "," + ph;

	    canvas.onmouseup = MouseUp;
	    canvas.onmousedown = MouseDown;
	    canvas.onmousemove = MouseMoved;

	    return setInterval(Repaint, 10); // repaint the canvas at intervals

		/* */
	}


	function Repaint() {
	    // Clear the canvas - otherwise the puck leaves a trail
	    ctx.clearRect(0, 0, cw, ch);

	    // Draw the background
	    // DrawRect(0, 0, cw, ch, "rgb(220,220,190)");

	    // Draw the puck
	    //DrawRect(px, py, pw, ph, "blue");

		//
		//ctx.drawImage(textImg,px,py,300,200,px,py,300,200);
		ctx.drawImage(textImg,px,py,pw,ph,px,py,pw,ph);
		
	}

	function DrawRect(x, y, w, h, colour) {    
	    ctx.fillStyle = colour;
	    ctx.beginPath();
	    ctx.rect(x, y, w, h);
	    ctx.closePath();
	    ctx.fill();
	}

	function MouseMoved(e) {
	    statusDiv.innerHTML = "Cursor[" + e.pageX + ", " + e.pageY + "], Offset["
	        + (e.pageX - canvas.offsetLeft - divOffsetLeft) + ", " + 
	        (e.pageY - canvas.offsetTop - divOffsetTop) + "]";
	    
	    if ( IsCursorOverPuck(e.pageX, e.pageY) ) {
	        document.body.style.cursor = 'pointer';
	    } else {
	        document.body.style.cursor = 'auto';
	    }

	    if (isMouseDown) {
	        px = (e.pageX - canvas.offsetLeft - divOffsetLeft)*sx - cx*sx;
	        py = (e.pageY - canvas.offsetTop - divOffsetTop)*sy - cy*sy;

	        statusDiv.innerHTML = "mouse down. Offset[" + cx + ", " + cy + "], Puck[" + 
	        px + ", " + py + "]";
	    }
	}


	function MouseUp() {
	    isMouseDown = false;
	}

	function MouseDown(e) {
		
		//alert("mouse down");
		
	    if ( IsCursorOverPuck(e.pageX, e.pageY) )
	    {
	        cx = (e.pageX - canvas.offsetLeft - divOffsetLeft)*sx - px;
	        cy = (e.pageY - canvas.offsetTop - divOffsetTop)*sy - py;
	        isMouseDown = true;
	    }
	}


	function IsCursorOverPuck(x, y) {
	    statusDiv.innerHTML = "Cursor x,y[" + x + ", " + y + 
	    	"], canvas.offsetLeft: " + canvas.offsetLeft +
	    	"], x- canvas.offsetLeft -divOffsetLeft[" +
	        (x - canvas.offsetLeft - divOffsetLeft) + ", " + 
	        (y - canvas.offsetTop - divOffsetTop) + 
	        "], Puck[" +
	        px + ", " + py + "]";

	    return (x - canvas.offsetLeft - divOffsetLeft) * sx > px  &&  
	    	(x - canvas.offsetLeft - divOffsetLeft) * sx < px + pw
	        && (y - canvas.offsetTop - divOffsetTop) * sy > py   &&  
	        (y - canvas.offsetTop - divOffsetTop) * sy < py + ph;
	}

	    
// Init();
	startLens();

}); // end doc ready


function startLensX() {
	
	var textc=document.getElementById("textCanvas");
	var textCtx=textc.getContext("2d");
	
	var textImg = new Image();
	textImg.onload = function(){
		textCtx.drawImage(textImg,0,0);
	};
	textImg.src = '/journal/lens/text_views/journal_0203.gif';
	//textImg.src = '/journal/views/journal_0203.jpg';
	
	
	var msc=document.getElementById("msCanvas");
	var msCtx=msc.getContext("2d");
	
	var msImg = new Image();
	msImg.onload = function(){
		msCtx.drawImage(msImg,0,0);
		//msCtx.fillStyle="#999999";
		//msCtx.fillRect(0,0,200,125);
		msCtx.clearRect(40, 40, 130, 100);
	   	
		
	};
	msImg.src = '/journal/views/journal_0203.jpg';
	
}

