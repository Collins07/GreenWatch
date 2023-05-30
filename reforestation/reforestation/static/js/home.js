

var marker;

function initMap(lat, lng) {
    var myLatLng = {lat: lat, lng: lng};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 8,
        center: myLatLng
    });
    marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'My Location'
    });
}

console.log("hello")



