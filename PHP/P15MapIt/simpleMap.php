<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<style type="text/css">
  html { height: 100% }
  body { height: 100%; margin: 0px; padding: 0px }
  #map_canvas { height: 100% }
</style>
<script type="text/javascript"
    src="http://maps.google.com/maps/api/js?sensor=false">
</script>
<script type="text/javascript">
  function initialize() {
    var SGlatlng = new google.maps.LatLng(1.283333, 103.833333);

    var myOptions = {
      zoom: 10,
      center: SGlatlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

    var RPlatlng = new google.maps.LatLng(1.446022, 103.78441);

    var RPmarker = new google.maps.Marker({
      position: RPlatlng,
      map: map,
      title: "Republic Polytechnic!"
    });

    var RPinfowindow = new google.maps.InfoWindow({
	content: "Best Polytechnic in Singapore & JB. Some say Batam."
    });

    google.maps.event.addListener(marker, 'click', function() {RPinfowindow.open(map,RPmarker);});
  }
</script>
</head>
<body onload="initialize()">
  <div id="map_canvas" style="width:100%; height:100%"></div>
</body>
</html>