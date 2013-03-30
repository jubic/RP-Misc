package sg.edu.rp.c345.p05.whereami;

import java.util.List;

import com.google.android.maps.GeoPoint;
import com.google.android.maps.MapActivity;
import com.google.android.maps.MapController;
import com.google.android.maps.MapView;
import com.google.android.maps.MyLocationOverlay;
import com.google.android.maps.Overlay;
import com.google.android.maps.OverlayItem;

import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;

public class WhereAmI extends MapActivity {
	
	//Declarations
	static final private int MAP_VIEW = Menu.FIRST;
	static final private int SAT_VIEW = Menu.FIRST + 1;
	private MapView map;
	private MapController myMapController;
	private MyLocationOverlay myLocationOverlay;
	private List<Overlay> mapOverlays;
	private Drawable drawable;
	private HelloItemizedOverlay itemizedOverlay;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		// MapView and Controller
		map = (MapView) findViewById(R.id.map);
		map.setBuiltInZoomControls(true);
		myMapController = map.getController();
		myMapController.setZoom(17);

		// MyLocationOverlay
		myLocationOverlay = new MyLocationOverlay(this,map);
		myLocationOverlay.enableMyLocation();
		map.getOverlays().add(myLocationOverlay);

		// Get Overlays
		mapOverlays = map.getOverlays();
		drawable = this.getResources().getDrawable(R.drawable.marker);
		itemizedOverlay = new HelloItemizedOverlay(drawable);
		
		// Add Marker on RP E6
		GeoPoint point = new GeoPoint (1445450, 103784260);
		OverlayItem overlayitem = new OverlayItem(point, "Hello!", "This is Republic Polytechnic E6");
		
		itemizedOverlay.addOverlay(overlayitem);
		mapOverlays.add(itemizedOverlay);
	}

	// Create Options menu
	@Override
	public boolean onCreateOptionsMenu(Menu optionsMenu) {
		super.onCreateOptionsMenu(optionsMenu);
		// Create and add new menu items.
		MenuItem itemMap = optionsMenu.add(0, MAP_VIEW, Menu.NONE,
				R.string.mapview);
		MenuItem itemSatellite = optionsMenu.add(0, SAT_VIEW,
				Menu.NONE, R.string.satview);
		
		itemMap.setIcon(R.drawable.mapview);
		itemSatellite.setIcon(R.drawable.satelliteview);
		return true;
	}

	// Execute option's action based on user click.
	@Override
	public boolean onOptionsItemSelected(MenuItem optionItem) {
		super.onOptionsItemSelected(optionItem);
		switch (optionItem.getItemId()) {
		case (MAP_VIEW): {

			map.setSatellite(false);
			return true;
		}
		case (SAT_VIEW): {

			map.setSatellite(true);
			return true;
		}

		}
		return false;
	}

	@Override
	protected boolean isRouteDisplayed() {
		// TODO Auto-generated method stub
		return false;
	}
}