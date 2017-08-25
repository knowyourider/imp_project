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

// establish global vars for lake switching
var lakeLayerNames = ["lake_15600", "lake_17200", "lake_17900", "lake_19500"]; 
var lake_15600, lake_17200, lake_17900, lake_19500;
var lakeLayerObjects = [lake_15600, lake_17200, lake_17900, lake_19500]; 
var prevLayerIndex = -1;

// experiment with icons
var greenIcon = L.icon({
    iconUrl: '/static/js/images/leaf-green.png',
    shadowUrl: '/static/js/images/leaf-shadow.png',

    iconSize:     [38, 95], // size of the icon
    shadowSize:   [50, 64], // size of the shadow
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    shadowAnchor: [4, 62],  // the same for the shadow
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

$(document).ready(function(){

	// ------------ BASE LAYER SECTION -------------
	// ----- define bounds ------
	// var southWest = L.latLng(41.225, -72.98), 
	// 	northEast = L.latLng(42.71, -72.42), // -72.37
	// 	mybounds = L.latLngBounds(southWest, northEast);

	// // ----- define bounds ------
	// var southWest = L.latLng(41.225, -72.98), 
	// 	northEast = L.latLng(42.71, -72.5), // -72.37
	// 	tempbounds = L.latLngBounds(southWest, northEast);

	var impBounds = [
		[40.55, -74], // southWest
		[44, -71.5] // northEast
	];

	var impMaxBounds = [
		[41.18, -73.43],
		[43.4, -71.82]
	];

	// ----- define map overlays ----- 
	var hitchcock1857   = L.tileLayer('/static/map/tiles/hitchcock1857/{z}/{x}/{y}.png', {
		attribution: 'Hitchcock map',
		// bounds: mybounds, //tempbounds
		minZoom: 9,
		maxZoom: 13,
		//opacity: .7,
        tms: true
	}),
	hitchcock1834   = L.tileLayer('/static/map/tiles/hitchcock1834/{z}/{x}/{y}.png', {
		attribution: 'Hitchcock map',
		// bounds: mybounds, //tempbounds
		minZoom: 9,
		maxZoom: 13,
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
		// bounds: mybounds,
		minZoom: 9,
		maxZoom: 13
    }), 
	hitchcock1833   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
	    attribution: 'Hitchcock map',
		// bounds: mybounds, //tempbounds
	    minZoom: 9,
	    maxZoom: 13,
	    id: 'donaldo.d51bywq4',
	    accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
	});

	var mapLayerObjects = [roads, hitchcock1857, hitchcock1834, hitchcock1833]; 


	// ----- define base layer -----
	var stamen = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain-'
		+ 'background/{z}/{x}/{y}.{ext}', {
		attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, '
		+ '<a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; '
		+ 'Map data &copy; ' 
		+ '<a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
		subdomains: 'abcd',
		// bounds: mybounds,
		bounds: impBounds,
		minZoom: 9,
		maxZoom: 13,
		ext: 'png'
	});

	// ----- set map -----
	map = L.map('map', {
		center: [42.0, -72.6], // -72.45
		zoom: 9, // 9
		maxBounds: impMaxBounds,
		maxBoundsViscosity: 0.5,
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
	// handle click on CHECKBOXES for overlays
	// $("#overlay_form input:checkbox").change(function(event){ // name=overlay
	$("#overlay_form input:checkbox").change(function(event){ // name=overlay
      // console.log(" --- checbox val: " + $(this).get(0).tagName);
      // determine whether checked or unchecked
      var intVal = parseInt($(this).val());
      if ($(this).is(':checked')) {
      	addImpOverlay(mapLayerObjects, intVal);
      } else { // action was to uncheck
      	removeImpOverlay(mapLayerObjects, intVal);
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

	// handle click on RADIO BUTTONS for lake
	$("#overlay_form input:radio").change(function(event){ // name=lake [type=radio]
		// radio button set will take care of its own checking and unchecking
		var intVal = parseInt($(this).val());
		// console.log(" --- radio val: " + intVal);
		switchLake(intVal);
	});

	$(document).on("click", "#clear_lake", function(event){
		event.preventDefault();
		switchLake(99);
	});

	// --------- SET THINGS IN MOTION ----------

	// start with toda roads on
	addImpOverlay(mapLayerObjects, 0);
	// $("#overlay_form input[type=checkbox]")[0].prop('checked', true);
	$("#overlay_form").find('input:checkbox:first').prop('checked', true);
	// :nth-child(0)

}); // end doc ready

// --------- Asychronous map setup ----------

function getGeoJson (thePath) {
	return $.getJSON(thePath);
}

// --------- RADIO LAKE SECTION ----------

// putting all the styling into one function to keep code short as possible
function HitchcockStyle(feature) {
    switch (feature.properties['Type']) {
        case 'glacier':
            return {
                fillColor: '#dadfd6',
                opacity: '0.0',
                fillOpacity: '0.70',
            };
            break;

        case 'lake':
            return {
                fillColor: '#1f93b4',
                opacity: '0.0',
                fillOpacity: '0.65',
            };
            break;
    }
}

function switchLake(lakeIndex) { //  layerShortName, 
	// console.log(" --- switch to: " + lakeIndex);
	// if a layer was added previously, remove it
	if (prevLayerIndex > -1) {
		map.removeLayer(lakeLayerObjects[prevLayerIndex]);
	}

	// catch 99 for none -- or clear
	if (lakeIndex > 90) {
		// uncheck all (any) radieo buttons
		$("#overlay_form input[type=radio]").prop('checked', false);
		// set prev to -1 since it'll already be cleared
		prevLayerIndex = -1;
	} else { // valid layer number
		prevLayerIndex = lakeIndex;

		// find out if this layer has already been generated
		// if not get the geoJson
		if (lakeLayerObjects[prevLayerIndex] == null){
			// console.log(" ----- got to null for this layer");
			// need to get promise for geoJson - use when success is returned
			// var geoPromise = getGeoJson("/static/js/map_assets/json_1950.geojson");
			var geoPromise = getGeoJson("/static/js/map_assets/" + 
				lakeLayerNames[lakeIndex] + ".geojson");

			// on successful return of geoJson
			// geoPromise.success(function (data) {
			geoPromise.done(function (data) {
				lakeLayerObjects[lakeIndex] = L.geoJson(data, {
			    	style: HitchcockStyle
				});

				// add this layer
				map.addLayer(lakeLayerObjects[lakeIndex]);
			});
		} else { // this layer is already defined, just switch it
			map.addLayer(lakeLayerObjects[lakeIndex]);
		}

		// // keep roads on top, if present
		// mapLayerObjects[0].bringToFront();
	}

}

// --------- CHECKBOX OVERLAY SECTION ----------

function openPopUpFromSide(markerIndex) {
	// console.log("got to open popup. markerIndex: " + markerIndex);
	markerList[markerIndex].openPopup();
}

function addImpOverlay(mapLayerObjects,layerIndex) { //  layerShortName, 
	map.addLayer(mapLayerObjects[layerIndex]);
	// mapLayerObjects[layerIndex].addTo(map);
	// keep roads on top, if present
	mapLayerObjects[0].bringToFront();
}

function removeImpOverlay(mapLayerObjects,layerIndex) {  
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
	// siteListPromise is a jqXHR object
	var siteListPromise = getSiteList("/map/sites/" + layerShortName + "/");

	// this is triggered when we get the json site list back (data)
	// siteListPromise.success(function (data) {
	// success method depricated in jquery 3.0. use "done" instead.
	siteListPromise.done(function (data) {

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
		var popHtml = "<p><strong>" + siteListJson[i].title + "</strong> </p>" + 
			// don't know why, but src attribute needs to not be quoted
			"<img src=/static/supporting/place/menupics/" + 
				siteListJson[i].slug  + ".jpg>" + siteListJson[i].map_blurb;
		// create marker, with popHtml
		// console.log(" --- siteListJson[i].latitude: " + siteListJson[i].latitude);	
		// make sure there's a valid lat and long
		if (siteListJson[i].latitude && siteListJson[i].longitude) {
			// add marker
			// since we're creating the array all we need is the index in order to pop it up
			// custom markers:   ..siteListJson[i].longitude], {icon: greenIcon}).bindPopup(popHtml));
			markerList.push(L.marker([siteListJson[i].latitude, 
				siteListJson[i].longitude]).bindPopup(popHtml));
			// add to HTML for site list links
			siteLinks += '<li><a class="site_link" href="' + i + '">' +
				siteListJson[i].title + "</a></li>" 		
		} else {
			siteLinks += '<li>' + siteListJson[i].title + " (missing lat, long)</li>" // site_info.title		
		}

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
