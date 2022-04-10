kakao.maps.event.addListener(map, 'bounds_changed', function() {             
    
    var bounds = map.getBounds();
    
    var swLatlng = bounds.getSouthWest(); //남서
    
    var neLatlng = bounds.getNorthEast(); //북동
    
    $.get(
        "/dust_data?bounds="+bounds,
            function(response) {
                //console.log (response);
            }
    );

});