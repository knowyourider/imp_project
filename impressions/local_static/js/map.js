// per http://leafletjs.com/examples/layers-control.html

var markerList = []; // on a level with map, markers can be accessed by index
// siteMarkers is a layerGroup - (not the list of markers themselves)
var siteMarkers ;
// cheating and making this global, should find way to send to promise
var _siteLinks = "site links";
var map = 0;
var prevLayerIndex = 0;

$(document).ready(function(){

	// ------------ BASE LAYER SECTION -------------
	// ----- define bounds ------
	var southWest = L.latLng(41.225, -72.98), 
		northEast = L.latLng(42.71, -72.42), // -72.37
		mybounds = L.latLngBounds(southWest, northEast);

	// ----- define bounds ------
	var southWest = L.latLng(41.225, -72.98), 
		northEast = L.latLng(42.71, -72.5), // -72.37
		tempbounds = L.latLngBounds(southWest, northEast);

	// ----- define layers ----- 
	var today   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, '+
		'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		bounds: mybounds,
		//maxBounds: mybounds,
		//maxBoundsViscosity: 1.0,
		minZoom: 9,
		maxZoom: 18,
		id: 'mapbox.streets',
		//id: 'mapbox.mapbox-terrain-v2',
		accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
	}),
	hitchcock   = L.tileLayer('/static/map/tiles/Hitchcock_Map/{z}/{x}/{y}.png', {
		attribution: 'Hitchcock map',
		bounds: mybounds, //tempbounds
		minZoom: 9,
		maxZoom: 16,
		//opacity: .7,
        tms: true
	}),
    // Adding vector tiled roads via Tangram - layer parameters, source, etc... are defined in scene.yaml file
    roads = Tangram.leafletLayer({
        // scene: '/static/js/map_assets/cinnabar-style.yaml',
        scene: '/static/js/map_assets/roads.yaml',
        // scene: '/static/js/map_assets/scene.yaml',
        attribution: '<a href="https://mapzen.com/tangram" target="_blank">Tangram</a> | &copy; OSM contributors | <a href="https://mapzen.com/" target="_blank">Mapzen</a>',
		bounds: mybounds,
		minZoom: 9,
		maxZoom: 13
    });

	

	var stamen = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.{ext}', {
		attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, ' +
		'<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; ' +
		'<a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
		subdomains: 'abcd',
		bounds: mybounds,
		minZoom: 9,
		maxZoom: 13,
		ext: 'png'
	 });

	// from Joe, seems the same as the stamen I was using
    var topobase = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/terrain-background/{z}/{x}/{y}.{ext}', {
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        subdomains: 'abcd',
        minZoom: 0,
        maxZoom: 18,
        ext: 'png'
    });

	// Set array of objects defined above
	var mapLayerObjects = [today, hitchcock, roads]; // , stamen
	// era short names. Will come from ajax


	// --------- SET THINGS IN MOTION ----------

	// setSiteLayer('today');
	// better place to do this?
    $(".map-layers li:nth-child(1)").addClass('selected');
	// var layerIndex = 0;
	var layerIndex = 2;

	map = L.map('map', {
		center: [42.0, -72.45],
		zoom: 9,
		//layers: [streets, markerList]
		// layers: [mapLayerObjects[layerIndex]] //, siteMarkers hitchcock
		layers: [stamen] // topobase stamen , siteMarkers hitchcock
	});

    // topobase.addTo(map);
    // roads.addTo(map);

	// add markers separately -- need to defer until ajax gets json

	// Set click action on the layer links
	// call utility function because I may want to change several overlays
	// $(".map-layers li a").on('click', function(event) {
	$(".layer_on").on('click', function(event) {
	    event.preventDefault();
	    // remove class from all li's then add highlight to this one
	    // $(".map-layers li").removeClass('selected');
	    // $(this).parent().attr('class', 'selected');
	    // $(this).attr('class', 'selected');

	    // get params for switch
	    var url_params = $(event.target).attr('href');
	    var href_split = url_params.split('/');    
	    //console.log(" map-layers href_split[0]: " + href_split[0] + " split[1]: " + href_split[1]);
	    // href_split[0] = layer.layer_index
	    // href_split[1] = layer.short_name
	    addOverlay(mapLayerObjects, href_split[0]); // , href_split[0] , siteMarkers
	  });

	$(".layer_off").on('click', function(event) {
	    event.preventDefault();
	    // get params for switch
	    var url_params = $(event.target).attr('href');
	    var href_split = url_params.split('/');    
	    // console.log(" map-layers href_split[0]: " + href_split[0] + " split[1]: " + href_split[1]);
	    removeOverlay(mapLayerObjects, href_split[0]); 
	  });

	// site markers  are from from overlays
	$(".location-set").on('click', function(event) {
	    event.preventDefault();

	    // get params for switch
	    var url_params = $(event.target).attr('href');
	    var href_split = url_params.split('/');    
	    // console.log(" map-layers href_split[0]: " + href_split[0] + " split[1]: " + href_split[1]);
	    // href_split[0] = layer.short_name
	    // href_split[1] = layer.layer_index
	    setSiteLayer(href_split[0]);
	  });

}); // end doc ready

// --------- UTILITY SECTION ----------

function openPopUpFromSide(markerIndex) {
	// console.log("got to open popup. markerIndex: " + markerIndex);
	markerList[markerIndex].openPopup();
}

function addOverlay(mapLayerObjects,layerIndex) { //  layerShortName, 
	map.addLayer(mapLayerObjects[layerIndex]);
	// mapLayerObjects[layerIndex].addTo(map);
	// keep roads on top, if present
	mapLayerObjects[2].bringToFront();
}
function removeOverlay(mapLayerObjects,layerIndex) {  
	map.removeLayer(mapLayerObjects[layerIndex]);		
	// mapLayerObjects[layerIndex].addTo(map);
}

function setSiteLayer(layerShortName) {

	// Call to "Regular" Ajax (getURL() in application.js) to re-populate the dig deeper box
	getURL("/map/deeper/" + layerShortName + "/", $('#deeper_ajax_wrapper'));

	// Get site list for this layer
	// get ansynchronous data via a "promise" per 
	// http://stackoverflow.com/questions/5316697/jquery-return-data-after-ajax-call-success
	var siteListPromise = getSiteList("/map/sites/" + layerShortName + "/");

	siteListPromise.success(function (data) {

		// remove previous marker layer
		//console.log("--- siteMarkers length: " + siteMarkers.length);
		if (siteMarkers != undefined) {
			map.removeLayer(siteMarkers);				
		}

		var siteListJson = $.parseJSON( data );
		// setSites sets global siteMarkers
		setSites(siteListJson);
		// add markers -- need to defer until ajax gets json
		// siteMarkers is set in setSites
		map.addLayer(siteMarkers);
		// writeSiteList();
		$('#site_list').html(_siteLinks);

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
	// console.log("site list in setSites: " + String(siteListOfDicts));
	// console.log("siteListJson[0].short_name: " + siteListJson[0].short_name);

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

		// create HTML for site list links
		// since we're creating the array all we need is the index in order to pop it up
		siteLinks += '<li><a href="' + i + '">' + siteListJson[i].site_info.title + "</a></li>" // site_info.title

	} // end for 
	siteLinks += "</ul>";

	// write slite links to sidebar
	// writeSiteList(siteLinks);
	// need to wait for ajax success
	_siteLinks = siteLinks;

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

	// create layer group
	siteMarkers = L.layerGroup(markerList);
	// add in "promisse" above

}

// function writeLayerList(layerLinks) {
// 	$('#layer_list').html(layerLinks);
// }



