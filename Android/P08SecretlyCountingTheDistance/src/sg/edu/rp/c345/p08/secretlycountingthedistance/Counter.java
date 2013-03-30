package sg.edu.rp.c345.p08.secretlycountingthedistance;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.widget.TextView;

public class Counter extends Activity {
	
	//Declarations
	TextView counterTV;
	CounterReceiver cReceiver;
	IntentFilter cValue;
	int counterValue;
	
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        //counterTV = (TextView) findViewById(R.id.counterTV);
        
        Intent startCounter = new Intent(getBaseContext(), SvcCounter.class);
        startService(startCounter);
    }
    
    private class CounterReceiver extends BroadcastReceiver {

		@Override
		public void onReceive(Context context, Intent intent) {
			// TODO Auto-generated method stub
			Bundle counterExtras = intent.getExtras();
			counterValue = counterExtras.getInt("cValue");
			counterTV.setText(String.valueOf(counterValue));
		}
    }
    
    public void onResume() {
		super.onResume();
		IntentFilter cValue = new IntentFilter("CounterValue");
		cReceiver = new CounterReceiver();
		registerReceiver(cReceiver, cValue);
	}
    
    public void onPause() {
    	super.onPause();
    	unregisterReceiver(cReceiver);
    }
}