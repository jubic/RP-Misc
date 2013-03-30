package sg.edu.rp.c345.p08.secretlycountingthedistance;

import android.app.Service;
import android.content.Intent;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.os.IBinder;
import android.util.Log;

public class SvcLatLong extends Service {

	LocationManager lmanager;
	Location myLocation;

	@Override
	public IBinder onBind(Intent arg0) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void onStart(Intent intent, int startId) {
		// TODO Auto-generated method stub
		super.onStart(intent, startId);
		LocationManager lmanager = (LocationManager) getSystemService(LOCATION_SERVICE);
		myLocation = lmanager
				.getLastKnownLocation(LocationManager.GPS_PROVIDER);

		Log.d("lat",myLocation.getLatitude()+"");
		Log.d("long",myLocation.getLongitude()+"");
		
		if (myLocation.equals(null)) {
			myLocation = new Location("");
			myLocation.setLatitude(0.0);
			myLocation.setLongitude(0.0);
		}
		
		lmanager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 5000, 30,
				new MyLocationListener());
	}

	private class MyLocationListener implements LocationListener {

		@Override
		public void onLocationChanged(Location location) {
			// TODO Auto-generated method stub
			double distance = location.distanceTo(myLocation);
			Intent locationIntent = new Intent("Location");
			locationIntent.putExtra("Distance", distance);
			locationIntent.putExtra("Latitude", location.getLatitude());
			locationIntent.putExtra("Longitude", location.getLongitude());
			Log.d("Distance", distance+"");
			Log.d("Latitude", location.getLatitude()+"");
			Log.d("Longtitude", location.getLongitude()+"");
			sendBroadcast(locationIntent);
		}

		@Override
		public void onProviderDisabled(String arg0) {
			// TODO Auto-generated method stub

		}

		@Override
		public void onProviderEnabled(String arg0) {
			// TODO Auto-generated method stub

		}

		@Override
		public void onStatusChanged(String arg0, int arg1, Bundle arg2) {
			// TODO Auto-generated method stub

		}
	}
}