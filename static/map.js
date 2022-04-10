var marker = [];

var X_RESOLUTION = 12;
var Y_RESOLUTION = 30;
var xhr;

function jetColor(n)
{
    var r,g,b;
    switch(true) {
        case (n<32):
            r = 0;
            g = 0;
            b = n * 4 + 127;
            break;
        case (n<96):
            r = 0;
            g = (n - 31) * 4;
            b = 255;
            break;
        case (n<160):
            r = (n - 95) * 4;
            g = 255;
            b = 255 - (n - 95) * 4;
            break;
        case (n<224):
            r = 255;
            g = 255 - (n - 159) * 4;
            b = 0;
            break;
        case (n<256):
            r = 255 - (n - 223) * 4;
            g = 0;
            b = 0;
            break;
        default:
            r = 127;
            g = 0;
            b = 0;
    }
    return 'rgb('+r+','+g+','+b+')';
}

show = function() {
    try{
        xhr.abort();
    } catch(e){

    }
    var bounds = map.getBounds();
    xhr = $.get(
        "/dust_data?bounds="+JSON.stringify([bounds, X_RESOLUTION, Y_RESOLUTION]),
        function(response) {
            marker.forEach(element => {
                element.setMap(null);
            });
            marker = [];
            response['data'].forEach(element => {
                element.forEach(element => {
                    if(element[0] != null) {
                        marker.push(new kakao.maps.CustomOverlay({
                            position : new kakao.maps.LatLng(element[2], element[1]),  // 좌표 입니다 
                            content: '<div style="background-color: '+jetColor(element[0])+'; opacity: 0.5; box-shadow: 0 0 150px 80px '+jetColor(element[0])+'"></div>'  
                        }));
                    }
                })
            })
            response['data'].forEach(element => {
                element.forEach(element => {
                    if(element[0] != null) {
                        marker.push(new kakao.maps.CustomOverlay({
                            position : new kakao.maps.LatLng(element[2], element[1]),  // 좌표 입니다 
                            content: '<div style="font-size: 2em;">'+Math.ceil(element[0])+'</div>'  
                        }));
                    }
                })
            })
            /*
            response['data'].forEach(element => {
                marker.push(new kakao.maps.CustomOverlay({
                    position : new kakao.maps.LatLng(element[1], element[0]),  // 좌표 입니다 
                    content: '<div class="data_label">'+element[2]+'</div>'  
                }));
            });*/
            marker.forEach(element => {
                element.setMap(map);
            });
        }
    );

};

kakao.maps.event.addListener(map, 'bounds_changed', show);

show();