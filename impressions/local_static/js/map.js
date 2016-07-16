// per http://leafletjs.com/examples/layers-control.html

// ---- define markers ----

// create array for sites and populate with sitesJson defined in html header
var sites = [];
for (var i = 0; i < sitesJson.length; i++) {
    // create popup
    var popHtml = "<p>" + sitesJson[i].site_type + "<br />" +
        "<strong>" + sitesJson[i].site_info.title + "</strong> </p>" +
        // don't know why, but src attribute needs to not be quoted
        "<img src=/static/supporting/" + sitesJson[i].site_type + "/menupics/" + 
            sitesJson[i].short_name  + ".jpg>" +
        "<p>" + sitesJson[i].site_info.map_blurb + "</p>";

    sites.push(L.marker([sitesJson[i].latitude, 
        sitesJson[i].longitude]).bindPopup(popHtml));
        //sitesJson[i].short_name));
} // end for    

var cragrock = L.marker([42.19, -72.592089]).bindPopup("craig rock"),
    coal    = L.marker([42.31	, -72.562724]).bindPopup("coal");

var siteMarkers = L.layerGroup(sites);
var geostuff = L.layerGroup([cragrock, coal]);

// ----- define vector layers -----

/* from: http://leafletjs.com/examples/geojson.html
var geojsonFeature = {
    "type": "Feature",
    "properties": {
        "name": "Coors Field",
        "amenity": "Baseball Stadium",
        "popupContent": "This is where the Rockies play!"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [-104.99404, 39.75621]
    }
};
*/

var myLines = [{
    "type": "LineString",
    "coordinates": [[-72.4, 42.1], [-72.5, 42.2], [-72.6, 42.3]]
}, {
    "type": "LineString",
    "coordinates": [[-105, 40], [-110, 45], [-115, 55]]
}];
var vectorLines = L.layerGroup([myLines]);

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
/*
hitchcock   = L.tileLayer('hitchcock1833_valley_geo/{z}/{x}/{y}.png', { 
    minZoom: 5,
    maxZoom: 16,
    //maxZoom: 18,
    attribution: 'hitchcock 1833',
    tms: true
});
*/

/*
* If we want to pull layer titles from the db,
can's use varables inside the object literal, 
(String(map_params[testLabelArray][0]): satellite_,
so:
var baseMaps = {};
var name1 = map_params.layers[0];
var name2 = "Hitchcock";
baseMaps[name1] = satellite;
baseMaps[name2] = hitchcock;
*/

// This defines the list used by built-in layer interface (upper right popup)
/* */
var baseMaps = {
    "Glacier": satellite,
    "Hitchcock's Era": hitchcock,
    "Today": today,
    "Jurassic": terrain
};

var mapArray = [today, hitchcock, terrain, satellite, terrain];

// defines checbox options in upper right built-in
/* */
var overlayMaps = {
    //"Sites": siteMarkers,
    "Vectors": vectorLines,
    "Geo Stuff": geostuff
};


var map = L.map('map', {
    center: [42.26, -72.59],
    zoom: 10,
    //layers: [streets, sites]
    layers: [mapArray[map_params.layerIndex], siteMarkers] // hitchcock
});

//L.control.layers(baseMaps, overlayMaps).addTo(map);

//L.geoJson(myLines).addTo(map);
