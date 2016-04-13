// per http://leafletjs.com/examples/layers-control.html
// define markers
var bigfoot = L.marker([42.265169, -72.592089]).bindPopup('Big footprint.'),
    fossil    = L.marker([42.292416, -72.653876]).bindPopup('Curious Fossil.'),
    bone    = L.marker([42.172750, -72.562724]).bindPopup('leg bone.');

var cragrock = L.marker([42.19, -72.592089]).bindPopup('Craggy rock.'),
    coal    = L.marker([42.31	, -72.562724]).bindPopup('coal deposit.');

var sites = L.layerGroup([bigfoot, fossil, bone]);
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

var baseMaps = {
    "Satellite": satellite,
    "Hitchcock": hitchcock,
    "Streets": streets,
    "Terrain": terrain
};

var overlayMaps = {
    "Sites": sites,
    "Geo Stuff": geostuff
};

var map = L.map('map', {
    center: [42.26, -72.59],
    zoom: 10,
    //layers: [streets, sites]
    layers: [hitchcock, sites]
});

L.control.layers(baseMaps, overlayMaps).addTo(map);
