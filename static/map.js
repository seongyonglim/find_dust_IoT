var marker = [];

show = function() {             
    marker.forEach(element => {
        element.setMap(null);
    });
    var bounds = map.getBounds();
    $.get(
        "/dust_data?bounds="+JSON.stringify(bounds),
        function(response) {
            response['data'].forEach(element => {
                marker.push(new kakao.maps.CustomOverlay({
                    position : new kakao.maps.LatLng(element[1], element[0]),  // 좌표 입니다 
                    content: '<div class="data_label">'+element[2]+'</div>'  
                }));
            });
            marker.forEach(element => {
                element.setMap(map);
            });
        }
    );

};

kakao.maps.event.addListener(map, 'bounds_changed', show);

show();