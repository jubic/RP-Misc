package sg.edu.rp.c345.p08.secretlycountingthedistance;

import java.util.Timer;
import java.util.TimerTask;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public class SvcCounter extends Service {

	// Declarations
	int counter;
	Timer timer;
	TimerTask timerTask;
	long delay;
	long period;

	@Override
	public IBinder onBind(Intent arg0) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void onCreate() {
		// TODO Auto-generated method stub
		counter = 0;
		TimerTask timerTask = new TimerTask() {
			public void run() {
				counter = counter + 1;
				Log.d("SvcCounter", Integer.toString(counter));
				Intent counterValue = new Intent("CounterValue");

				counterValue.putExtra("cValue", counter);
				sendBroadcast(counterValue);
			}
		};
		Timer timer = new Timer();
		timer.schedule(timerTask, delay = 2000, period = 5000);
		super.onCreate();
	}

	@Override
	public void onDestroy() {
		// TODO Auto-generated method stub
		timer.cancel();
		super.onDestroy();
	}

	@Override
	public int onStartCommand(Intent intent, int flags, int startId) {
		// TODO Auto-generated method stub
		return super.onStartCommand(intent, flags, startId);
	}

}