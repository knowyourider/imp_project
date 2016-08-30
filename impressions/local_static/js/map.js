// per http://leafletjs.com/examples/layers-control.html

var markerList = []; // on a level with map, markers can be accessed by index
// siteMarkers is a layerGroup - temp
var siteMarkers;
var map = 0;
var prevLayerIndex = 0;

$(document).ready(function(){

	// ------------ BASE LAYER SECTION -------------
	// ----- define bounds ------
	var southWest = L.latLng(41.211, -73.225), 
		northEast = L.latLng(42.747, -72.294),
		mybounds = L.latLngBounds(southWest, northEast);

	// ----- define base layers ----- 
	var terrain = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png' +
		'?access_token={accessToken}', {
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> ' +
			'contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		bounds: mybounds,
		minZoom: 9,
		maxZoom: 18,
		//id: 'mapbox.streets',
		id: 'mapbox.mapbox-terrain-v2',
		accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
	}),
	satellite   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', 
		{
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' + 
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		bounds: mybounds,
		minZoom: 9,
		maxZoom: 18,
		id: 'mapbox.satellite',
		accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
	}),
	today   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, '+
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		bounds: mybounds,
		minZoom: 8,
		maxZoom: 18,
		id: 'mapbox.streets',
		//id: 'mapbox.mapbox-terrain-v2',
		accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
	}),
	hitchcock   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
		attribution: 'Hitchcock map',
		bounds: mybounds,
		minZoom: 10,
		maxZoom: 13,
		id: 'donaldo.d51bywq4',
		accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
	});
	// Set array of objects defined above
	var baseLayerObjects = [today, hitchcock, satellite, satellite];
	// era short names. Will come from ajax

	setLayer('today');
	var layerIndex = 0;

	map = L.map('map', {
		center: [42.35, -72.59],
		zoom: 10,
		//layers: [streets, markerList]
		layers: [baseLayerObjects[layerIndex]] //, siteMarkers hitchcock
	});
	// add markers separately -- need to defer until ajax gets json

	// Set click action on the layer links
	// call utility function because I may want to change several overlays
	$(".map-layers li a").on('click', function(event) {
    event.preventDefault();
    // get element index for highlight
    //var elementIndex = $(event.target).index();
    //console.log(" map-layers target index: " + $(this).index());

    // come back to this after I have highlight style from Juliet

    //console.log(" map-layers target index: " + $(this).parent().attr("class"));

    // remove class from all li's then add highlight to this one
    //$(".map-layers li").removeClass('map-layers--item');
    //$(this).parent().attr('class', 'map-layers--item');
    //console.log(" $(this).parent().attr('class')): " + $(this).parent().attr('class'));

    // get params for switch
    var url_params = $(event.target).attr('href');
    var href_split = url_params.split('/');    
    // console.log(" lmap-layers href_split[0]: " + href_split[0] + " split[1]: " + href_split[1]);
    // href_split[0] = layer.short_name
    // href_split[1] = layer.layer_index
    // siteMarkers is the layerGroup (not the list)
    switchLayer(baseLayerObjects, href_split[0], href_split[1], siteMarkers);
  });
   

}); // end doc ready

// --------- UTILITY SECTION ----------

function writeLayerList (layerLinks) {
	$('#layer_list').html(layerLinks);
}

function writeSiteList (siteLinks) {
	// console.log("got to writeSiteList");
	//var siteListHtml = "<p>site list From js</p>";
	// write the inner html
	$('#site_list').html(siteLinks);
}

function openPopUpFromSide (markerIndex) {
	// console.log("got to open popup. markerIndex: " + markerIndex);
	markerList[markerIndex].openPopup();
}

function switchLayer(baseLayerObjects, layerShortName, layerIndex) {
		map.removeLayer(baseLayerObjects[prevLayerIndex]);
		map.addLayer(baseLayerObjects[layerIndex]);
		prevLayerIndex = layerIndex;


		// Remove site markers before calling switch
		map.removeLayer(siteMarkers);		
		setLayer(layerShortName);
}

function setLayer(layerShortName) {

		// "Regular" Ajax (in application.js) to re-populate the right column with a template
		// calls first of two views
	  getURL("/map/assoc/" + layerShortName + "/", $('.map-about-panel'));

		// Get site list for this layer
		// get ansynchronous data via a "promise" per 
		// http://stackoverflow.com/questions/5316697/jquery-return-data-after-ajax-call-success
		var siteListPromise = getSiteList("/map/sites/" + layerShortName + "/");

		siteListPromise.success(function (data) {

			var siteListJson = $.parseJSON( data );
			// setTempList(data);
			setSites(siteListJson);

			// add markers separately -- need to defer until ajax gets json
			// siteMarkers is set in setSites
			map.addLayer(siteMarkers);


		});
}

// ----------- AJAX ----------

// jQuery Ajax
// Need to set up call to ajax asynchronously. Use promise per 
// http://stackoverflow.com/questions/5316697/jquery-return-data-after-ajax-call-success
function getSiteList(theURL) { //, contentDiv
	return $.ajax({
		url: theURL
	});
}

	// -------- MARKER SECTION ---------


	// create array for site Markers and populate with siteListOfDicts defined in html header
function setSites(siteListJson) {

	// var siteListJson = $.parseJSON( siteListOfDicts );

	// console.log("site list in setSites: " + String(siteListOfDicts));
	console.log("siteListJson[0].short_name: " + siteListJson[0].short_name);
	// console.log("siteListJson[0].longitude: " + String(siteListJson[0].longitude));


	var siteLinks = '<ul class="map-sites">';
	markerList = [];
	//var markerList = [];
	for (var i = 0; i < siteListJson.length; i++) {
		// create HTML for popup
		var popHtml = "<p>" + siteListJson[i].site_type_verbose + "<br />" +  
			"<strong>" + siteListJson[i].site_info.title + "</strong> </p>" + 
			// don't know why, but src attribute needs to not be quoted
			"<img src=/static/supporting/" + siteListJson[i].site_type + "/menupics/" + 
				siteListJson[i].short_name  + ".jpg>" + siteListJson[i].site_info.map_blurb;

		markerList.push(L.marker([siteListJson[i].latitude, 
			siteListJson[i].longitude]).bindPopup(popHtml));
			//siteListJson[i].short_name));

		// create HTML for site list links
		// since we're creating the array all we need is the index in order to pop it up
		siteLinks += '<li><a href="' + i + '">' + siteListJson[i].short_name + "</a></li>" // site_info.title

	} // end for 
	siteLinks += "</ul>";

	// write slite links to sidebar
	writeSiteList(siteLinks);

  // Need to set new markerList on the map
  //var siteMarkers = L.layerGroup(markerList);
	// map.addLayer(L.layerGroup(markerList));

	// Set click action on the links
	$("#site_list li a").on('click', function(event) {
    event.preventDefault(); 
    //console.log("link on site_list works");
    var markerIndex = $(event.target).attr('href');
    openPopUpFromSide(markerIndex)
  });

	// temp spot for this
	siteMarkers = L.layerGroup(markerList);
	// siteMarkers.addTo(map);

}


