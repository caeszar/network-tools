

<section id="wrapper">
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
    <article>
<p><span id="status"><img src="ajax-loader.gif" alt="Loading" width="43" height="11" style="margin:2px 6px;"  />Please wait we are trying to locate you...</span></p>
    </article>
<script>
function success(position) {
  var s = document.querySelector('#status');
  if (s.className == 'success') {
    return;
  }
  //Message after tracing the location
  s.innerHTML = "Found your Location!";
  s.className = 'success';
  //Create div for showing map
  var mapcanvas = document.createElement('div');
  mapcanvas.id = 'mapcanvas';
  mapcanvas.style.height = '400px';
  mapcanvas.style.width = '900px';
  mapcanvas.style.margin = '1px auto';
    
  document.querySelector('article').appendChild(mapcanvas);
  
  var latlng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  var myOptions = {
    zoom: 14,
    center: latlng,
    mapTypeControl: true,
    navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL},
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("mapcanvas"), myOptions);
  
  var marker = new google.maps.Marker({
      position: latlng, 
      map: map, 
      title:"You are here!"
  });
}

function error(msg) {
  var s = document.querySelector('#status');
  s.innerHTML = typeof msg == 'string' ? msg : "failed";
  s.className = 'fail';
}

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(success, error);
} else {
  error('not supported');
}
</script> 
</section>

