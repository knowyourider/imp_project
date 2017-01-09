// Single base layer (stamen) is present for all possible states
// Location set list is set by Django and template
// 	JS generates the Sites list, an Ajax template generates the Dig Deeper list
// Map overlays are set by-hand in this file
//  overlay index numbers need to correspond to map_blurb indexes set in Admin

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

	// ----- define overlays ----- 
	var hitchcock   = L.tileLayer('/static/map/tiles/Hitchcock_Map/{z}/{x}/{y}.png', {
		attribution: 'Hitchcock map',
		bounds: mybounds, //tempbounds
		minZoom: 9,
		maxZoom: 16,
		//opacity: .7,
        tms: true
	}),
    // Adding vector tiled roads via Tangram - layer parameters, source, etc... 
    // are defined in scene.yaml file
    roads = Tangram.leafletLayer({
        // scene: '/static/js/map_assets/cinnabar-style.yaml',
        scene: '/static/js/map_assets/roads.yaml',
        // scene: '/static/js/map_assets/scene.yaml',
        attribution: '<a href="https://mapzen.com/tangram" target="_blank">Tangram</a> '
        + '| &copy; OSM contributors | <a href="https://mapzen.com/" '
        + 'target="_blank">Mapzen</a>',
		bounds: mybounds,
		minZoom: 9,
		maxZoom: 13
    }), 
	hitchcock_1833   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: 'Hitchcock map',
		bounds: mybounds, //tempbounds
	    minZoom: 9,
	    maxZoom: 13,
	    id: 'donaldo.d51bywq4',
	    accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
	});

	// ----- define base layer -----
	var stamen = L.tileLayer('http://stamen-tiles-{s}.a.ssl.fastly.net/terrain-'
		+ 'background/{z}/{x}/{y}.{ext}', {
		attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
		+ '<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; '
		+ 'Map data &copy; ' 
		+ '<a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
		subdomains: 'abcd',
		bounds: mybounds,
		minZoom: 9,
		maxZoom: 13,
		ext: 'png'
	 });

	// Set array of objects defined above
	var mapLayerObjects = [roads, hitchcock, hitchcock_1833 ]; // , stamen , lake
	// era short names. Will come from ajax

	// load GeoJSON from an external file
	$.getJSON("/static/js/map_assets/lake2.geojson",function(data){
		// add GeoJSON layer to the map once the file is loaded
		var lake = L.geoJson(data);
		// lake = L.geoJson(data).addTo(map);
		mapLayerObjects.push(lake);
	});

	var myStyle = {
	    "color": "#eeeeee",
	    "weight": 3,
	    "opacity": 0.85
	};

	// load GeoJSON from an external file
	$.getJSON("/static/js/map_assets/glacier.geojson",function(data){
		// add GeoJSON layer to the map once the file is loaded
		var glacier = L.geoJson(data, {
	    	style: myStyle
		});
		mapLayerObjects.push(glacier);
	});

	// L.geoJSON(myLines, {
	//     style: myStyle
	// }).addTo(map);

	// --------- SET THINGS IN MOTION ----------

	// setSiteLayer('today');
	// better place to do this?
    $(".map-layers li:nth-child(1)").addClass('selected');
	// initial overlay
	var layerIndex = 0;

	map = L.map('map', {
		center: [42.0, -72.45],
		zoom: 9,
		//layers: [streets, markerList]
		// layers: [mapLayerObjects[layerIndex]] //, siteMarkers hitchcock
		layers: [stamen] // topobase stamen , siteMarkers hitchcock
	});

	// ----- Location Set Handling -----

	// handle click on radio button for location set
	$("#loc_sets input[name=loc_set]").change(function(event){
	    // console.log(" --- radio " );
	    var layerSlug = $(this).val()
	    // var layerSlug = $('#loc_sets input[name=loc_set]:checked').val()
	    setSiteLayer(layerSlug);
	});

	// set initial state
	// checked
	$('#loc_sets input:first').prop("checked", true);
	// setSiteLayer('none'); // called by script in template with slug for 1st item
	// site_list click event handler set in setSiteLayer after Ajax success

	// ----- Map Overlay checkbox Handling -----

	// 
	// handle click on checkboxes for overlays
	$("#overlays input[name=overlay]").change(function(event){
      // console.log(" --- checbox val: " + $(this).get(0).tagName);
      // determine whether checked or unchecked
      var intVal = parseInt($(this).val());
      if ($(this).is(':checked')) {
      	addOverlay(mapLayerObjects, intVal);
      } else { // action was to uncheck
      	removeOverlay(mapLayerObjects, intVal);
      }
	});

	// handle link for more map info
	// Call to "Regular" Ajax (getURL() in application.js) 
	// to re-populate the About this Map box
	// The layer_index in the href has to match the index order set in 
	// var mapLayerObjects above
	$(document).on("click", ".about_map", function(event){
		event.preventDefault();
		// get href
		var layerIndex = $(event.target).attr('href');
		// console.log('layerIndex: ' + layerIndex);
		// call ajax for the slim pop. 
		getURL("/map/about/" + layerIndex + "/", $('#about_map_ajax_wrapper'));
	});

	// GeoJSON experiment
	// var myLines = [{
	//     "type": "LineString",
	//     "coordinates": [[-72.4, 42.1], [-72.5, 42.2], [-72.6, 42.3]]
	// }, {
	//     "type": "LineString",
	//     "coordinates": [[-72.9, 42.6], [-73, 42.2], [-72.9, 42.8]]
	// }];
	// var myStyle = {
	//     "color": "#ff7800",
	//     "weight": 5,
	//     "opacity": 0.65
	// };

	// L.geoJSON(myLines, {
	//     style: myStyle
	// }).addTo(map);

	// var geojsonFeature = {
	//     "type": "Feature",
	//     "properties": {
	//         "name": "Coors Field",
	//         "amenity": "Baseball Stadium",
	//         "popupContent": "This is where the Rockies play!"
	//     },
	//     "geometry": {
	//         "type": "Point",
	//         "coordinates": [-72.4, 42.1]
	//     }
	// };

	// L.geoJSON(geojsonFeature).addTo(map);

	// // load GeoJSON from an external file
	// $.getJSON("/static/js/map_assets/test.geojson",function(data){
	// 	// add GeoJSON layer to the map once the file is loaded
	// 	L.geoJson(data).addTo(map);
	// });

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
	mapLayerObjects[0].bringToFront();
}
function removeOverlay(mapLayerObjects,layerIndex) {  
	map.removeLayer(mapLayerObjects[layerIndex]);		
	// mapLayerObjects[layerIndex].addTo(map);
}

function setSiteLayer(layerShortName) {

	// Call to "Regular" Ajax (getURL() in application.js) 
	// to re-populate the dig deeper box
	getURL("/map/deeper/" + layerShortName + "/", $('#deeper_ajax_wrapper'));

	// Get site list for this layer
	// get ansynchronous data via a "promise" per 
	// http://stackoverflow.com/questions/5316697/jquery-return-data-after-ajax-call-success
	var siteListPromise = getSiteList("/map/sites/" + layerShortName + "/");

	// this is triggered when we get the json site list back (data)
	siteListPromise.success(function (data) {

		// remove previous marker layer
		// site markers are undefined on initial visit, 
		// siteMarkers is defined by the time of first radio click, even though 
		// previous was "none"
		if (siteMarkers != undefined) { // e.g. if defined
			map.removeLayer(siteMarkers);				
		}

		var siteListJson = $.parseJSON( data );
		// setSites sets global siteMarkers
		setSites(siteListJson, layerShortName);
		// add markers -- need to defer until ajax gets json
		// siteMarkers is set in setSites

		// only add if defined
		if (layerShortName != "none") { 
			siteMarkers.addTo(map);
		}

		// write site list, but substitue blank list for none
		if (layerShortName == "none") {
			_siteLinks = '<ul class="map-sites">';
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += '<li>&nbsp;</li>'
			_siteLinks += "</ul>";
		}

		$('#site_list').html(_siteLinks);

		// now that list is in place add event listener
		// Set click action on the links
		$(".site_link").on('click', function(event) {
		    event.preventDefault(); 
		    // console.log("---- link on site_list works");
		    var markerIndex = $(event.target).attr('href');
		    openPopUpFromSide(markerIndex)
		 });

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
function setSites(siteListJson, layerShortName) {
	// console.log("site list in setSites: " + String(siteListOfDicts));
	// console.log("siteListJson[0].short_name: " + siteListJson[0].short_name);

	var siteLinks = '<ul class="map-sites">';
	markerList = [];
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
		siteLinks += '<li><a class="site_link" href="' + i + '">' 
			+ siteListJson[i].site_info.title + "</a></li>" // site_info.title

	} // end for 
	siteLinks += "</ul>";

	// set site links for sidebar
	// need to wait for ajax success
	_siteLinks = siteLinks;

	// Set click action on the links
	// above in "promise" - setSiteLayer
	// create layer group
	siteMarkers = L.layerGroup(markerList);
	// add in "promise" above

}
