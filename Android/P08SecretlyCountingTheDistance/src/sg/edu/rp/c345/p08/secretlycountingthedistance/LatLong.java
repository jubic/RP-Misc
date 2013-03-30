package sg.edu.rp.c345.p08.secretlycountingthedistance;

import java.text.DecimalFormat;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.widget.TextView;

public class LatLong extends Activity {
	
	//Declarations
	TextView distanceTV, latTV, longTV;
	CounterReceiver lReceiver;
	IntentFilter lValue;
	int locationValue;
	
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        distanceTV = (TextView) findViewById(R.id.distanceTV);
        latTV = (TextView) findViewById(R.id.latitudeTV);
        longTV = (TextView) findViewById(R.id.longitudeTV);
        
        Intent latLongService = new Intent(getBaseContext(), SvcLatLong.class);
        startService(latLongService);
    }
    
    private class CounterReceiver extends BroadcastReceiver {

		@Override
		public void onReceive(Context context, Intent intent) {
			// TODO Auto-generated method stub
			double counter = intent.getDoubleExtra("Distance", 0);
			DecimalFormat distanceBetweenFormat = new DecimalFormat("#0.00");
			distanceTV.setText("Distance from previous location: " +distanceBetweenFormat.format(counter/1000) + " km");
			latTV.setText("Latitude"+intent.getDoubleExtra("Latitude", 0) + "");
			longTV.setText("Longitude"+intent.getDoubleExtra("Longitude", 0) + "");
		}
    }
    
    public void onResume() {
		super.onResume();
		IntentFilter lValue = new IntentFilter("Location");
		lReceiver = new CounterReceiver();
		registerReceiver(lReceiver, lValue);
	}
    
    public void onPause() {
    	super.onPause();
    	unregisterReceiver(lReceiver);
    }
}