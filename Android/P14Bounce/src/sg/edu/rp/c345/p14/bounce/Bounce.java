package sg.edu.rp.c345.p14.bounce;

import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.CopyOnWriteArrayList;

import android.app.Activity;
import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;

public class Bounce extends Activity {

	// Variables
	CopyOnWriteArrayList<Ball> ballList = new CopyOnWriteArrayList<Ball>();
	Ball ball;
	Handler ballHandler;
	int r = 0, g = 0, b = 0;
	Paint paint;
	float radius, x, y, xSpeed, ySpeed;
	SoundManager mSoundManager;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		// Specify no title on the screen, and to be full screen
		getWindow().requestFeature(Window.FEATURE_NO_TITLE);
		getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
				WindowManager.LayoutParams.FLAG_FULLSCREEN);
		setContentView(R.layout.main);

		// Initialize SoundManager and add the sound
		mSoundManager = new SoundManager();
		mSoundManager.initSounds(getBaseContext());
		mSoundManager.addSound(1, R.raw.shoot);
		mSoundManager.addSound(2, R.raw.win);

		// Get the emulator/phone's dimensions
		x = getWindowManager().getDefaultDisplay().getWidth();
		y = getWindowManager().getDefaultDisplay().getHeight();

		for (int i = 0; i <= 5; i++) {
			paint = new Paint();

			// Ball's variables
			radius = (float) (Math.random() * 200);
			xSpeed = (int) (Math.random() * 10);
			ySpeed = (int) (Math.random() * 10);
			r = (int) (Math.random() * 255);
			g = (int) (Math.random() * 255);
			b = (int) (Math.random() * 255);
			paint.setARGB(255, r, g, b);

			// Create Ball object out of variables above
			ball = new Ball((float) Math.random() * x, (float) Math.random()
					* y, radius, xSpeed, ySpeed, paint);

			/*
			 * Set the region where the balls will be contained, so it will
			 * reverse it's directions when it reaches the edges and add into
			 * ArrayList
			 */
			ball.setRegion((int) x, (int) y);
			ballList.add(ball);
		}

		// View to contain Ball
		class DrawView extends View {
			public DrawView(Context context) {
				super(context);
			}

			// Draw the Ball on the canvas.
			protected void onDraw(Canvas canvas) {
				super.onDraw(canvas);

				for (Ball b : ballList) {
					canvas.drawCircle(b.getX(), b.getY(), b.getRadius(),
							b.getPaint());
				}
			}

			@Override
			public boolean onTouchEvent(MotionEvent event) {
				// TODO Auto-generated method stub
				Log.d("X coordinate of Motion Touch Location",
						"X: " + event.getX());
				Log.d("Y coordinate of Motion Touch Location",
						"Y: " + event.getY());

				// Get the area the circle. If user touch is within area of
				// circle, remove.
				for (Ball b : ballList) {
					if (b.getX() + b.getRadius() > event.getX()
							&& b.getX() - b.getRadius() < event.getX()
							&& b.getY() + b.getRadius() > event.getY()
							&& b.getY() - b.getRadius() < event.getY()) {

						// b.setxSpeed(-b.getxSpeed());
						// b.setySpeed(-b.getySpeed());
						//mSoundManager.playSound(1);
						ballList.remove(b);
					}
				}

				while (ballList.size() == 0 || ballList.size() < 1) {
					mSoundManager.playSound(2);
					for (int i = 0; i <= 5; i++) {
						paint = new Paint();

						// Ball's variables
						radius = (float) (Math.random() * 150);
						xSpeed = (int) (Math.random() * 10);
						ySpeed = (int) (Math.random() * 10);
						r = (int) (Math.random() * 255);
						g = (int) (Math.random() * 255);
						b = (int) (Math.random() * 255);
						paint.setARGB(255, r, g, b);

						// Create Ball object out of variables above
						ball = new Ball((float) Math.random() * x,
								(float) Math.random() * y, radius, xSpeed,
								ySpeed, paint);

						/*
						 * Set the region where the balls will be contained, so
						 * it will reverse it's directions when it reaches the
						 * edges and add into ArrayList
						 */
						ball.setRegion((int) x, (int) y);
						ballList.add(ball);
					}
				}
				return super.onTouchEvent(event);
			}
		}

		// Initialize View and set as ContentView
		final DrawView myView = new DrawView(this);
		setContentView(myView);

		// Handler to handle the message sent by the TimerTask thread
		ballHandler = new Handler() {
			public void handleMessage(Message msg) {

				myView.invalidate();

			}
		};

		/*
		 * Create a thread that updates the new position of the ball based on
		 * the mathematical calculation in the Ball update() method
		 */
		TimerTask ballUpdate = new TimerTask() {
			public void run() {

				for (Ball b : ballList) {
					b.update();
					ballHandler.sendEmptyMessage(0);
				}

			}
		};

		Timer t = new Timer();
		/*
		 * Schedule the Timer to run every (1000/30=33) miliseconds to achieve
		 * 30 fps
		 */
		t.schedule(ballUpdate, 0, 33);
	}
}