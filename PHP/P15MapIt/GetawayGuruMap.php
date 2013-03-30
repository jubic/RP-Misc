<?php
    include "dbFunctions.php";
    $arrHotels = executeSelectQuery("SELECT * FROM hotels");
?>
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
    var sgMap;
  function initialize() {
    var sgLatLng = new google.maps.LatLng(1.283333, 103.833333);
    var myOptions = {
      zoom: 13,
      center: sgLatLng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    sgMap = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    <?php
        for($hotelCount = 0; $hotelCount < count($arrHotels); $hotelCount++)
        {
    ?>
            var sgHotelsLatLng = new google.maps.LatLng(<?php echo $arrHotels[$hotelCount][2];?>, <?php echo $arrHotels[$hotelCount][3];?>);
            var sgHotelsMarkers = new google.maps.Marker({
                position: sgHotelsLatLng,
                map: sgMap,
                title: "<?php echo $arrHotels[$hotelCount][1];?>"
            })
            var sgHotelsInfoWindow = new google.maps.InfoWindow({
                content: "<?php echo $arrHotels[$hotelCount][2];?>"
            })
            google.maps.event.addListener(sgHotelsMarkers, 'click', function() {sgHotelsInfoWindow.setContent(this.title),sgHotelsInfoWindow.open(sgMap,this);});
    <?php
        }
    ?>
  }
</script>
</head>
<body onload="initialize()">
  <div id="map_canvas" style="width:75%; height:75%"></div>
</body>
</html>