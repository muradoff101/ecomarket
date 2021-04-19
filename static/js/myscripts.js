// In the following example, markers appear when the user clicks on the map.
// The markers are stored in an array.
// The user can then click an option to hide, show or delete the markers.

var rowCount = $('.map_info tr').length;

container = []

for (i = 1; i <= rowCount; i++) {
    // container['marker' + i] = {
    //     lat: Number(parseFloat($(".info" + i + " .courier_latitude").text())),
    //     lng: Number(parseFloat($(".info" + i + " .courier_longitude").text()))
    // };

    container.push({
        lat: Number(parseFloat($(".info" + i + " .courier_latitude").text())),
        lng: Number(parseFloat($(".info" + i + " .courier_longitude").text()))
    })
}

// alert(container.marker1.lat)
console.log(container)



let map;
let markers = [];

function initMap() {
    var haightAshbury = {
        lat: 59.9261077000000000,
        lng: 30.2914828000000000
    };

    var secondMarker = {
        lat: 59.9294864000000000,
        lng: 30.2944343000000000
    }
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: haightAshbury,
        mapTypeId: "terrain",
    });
    // This event listener will call addMarker() when the map is clicked.
    map.addListener("click", (event) => {
        addMarker(event.latLng);
    });
    // Adds a marker at the center of the map.
    // addMarker(haightAshbury);

    // alert(container.length)

    for (i = 0; i <= container.length; i++) {
        addMarker(container[i]);
    }
    // addMarker(secondMarker);

}



// Adds a marker to the map and push to the array.
function addMarker(location) {
    const marker = new google.maps.Marker({
        position: location,
        map: map,
        description: 'title1'
    });
    markers.push(marker);
}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
    for (let i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
    setMapOnAll(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    markers = [];
}



$(document).ready(function () {
    function get_hostname(url) {
        return $(location).attr('hostname');
    }

    $('#id_username').addClass("form-control")
    $('#id_password').addClass("form-control")


    // $("#login_form").submit(function (e) {
    //     e.preventDefault();
    //     var form = $(this)

    //     $.ajax({
    //         type: "POST",
    //         data: form.serialize(),
    //         url: 'http://' + get_hostname() + ':8000/api/v1/login/',
    //         success: function (data) {

    //             return false;

    //             if (data != 'fail') {
    //                 window.location.href = 'http://' + get_hostname() + ":8000/";
    //             } else {
    //                 $("#login-desc-content").empty().css("color", "red").append("Не правильные данные")
    //             }
    //         }
    //     });
    // });
});