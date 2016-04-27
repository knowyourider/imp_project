// per http://leafletjs.com/examples/layers-control.html

// define markers

// create array for sites and populate with sitesJson defined in html header
var sites = [];
/*
for (var i = 0; i < sitesJson.length; i++) {
    sites.push(L.marker([sitesJson[i].fields.latitude, 
        sitesJson[i].fields.longitude]).bindPopup(sitesJson[i].fields.site_type + 
        ": " + sitesJson[i].fields.short_name));
} // end for    

for (var i = 0; i < sitesJson.length; i++) {
    sites.push(L.marker([sitesJson[i].latitude, 
        sitesJson[i].longitude]).bindPopup(sitesJson[i].site_type + 
        ": " + sitesJson[i].site_info.title));
        //sitesJson[i].short_name));
} // end for    
*/
for (var i = 0; i < sitesJson.length; i++) {
    var popHtml = "<p>" + sitesJson[i].site_type + "<br />" +
        "<strong>" + sitesJson[i].site_info.title + "</strong> </p>" +
        "<p>" + sitesJson[i].site_info.narrative + "</p>";

    sites.push(L.marker([sitesJson[i].latitude, 
        sitesJson[i].longitude]).bindPopup(popHtml));
        //sitesJson[i].short_name));
} // end for    

var cragrock = L.marker([42.19, -72.592089]).bindPopup(map_params.layers[0]),
    coal    = L.marker([42.31	, -72.562724]).bindPopup(map_params.layers[1]);

//var siteMarkers = L.layerGroup([bigfoot, fossil, bone]);
var siteMarkers = L.layerGroup(sites);
var geostuff = L.layerGroup([cragrock, coal]);

// define base layers
var terrain = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    //id: 'mapbox.streets',
    id: 'mapbox.mapbox-terrain-v2',
    accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
}),
satellite   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.satellite',
    accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
}),
streets   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    //id: 'mapbox.mapbox-terrain-v2',
    accessToken: 'pk.eyJ1IjoiZG9uYWxkbyIsImEiOiJjaWxjbTZ0eXIzNmh5dTJsemozOTRwbWViIn0.xB0UB2teNew30PzKpxHSDA'
}),
hitchcock   = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Hitchcock map',
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

var baseMaps = {
    "Glacier": satellite,
    "Hitchcock's Era": hitchcock,
    "Today": streets,
    "Jurassic": terrain
};

var overlayMaps = {
    "Sites": siteMarkers //,
    //"Geo Stuff": geostuff
};

var map = L.map('map', {
    center: [42.26, -72.59],
    zoom: 10,
    //layers: [streets, sites]
    layers: [hitchcock, siteMarkers]
});

L.control.layers(baseMaps, overlayMaps).addTo(map);
