package sg.edu.rp.c345.p06.worldofshoes;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class ViewShoe extends Activity {

	// Declarations
	TextView modelNameTV;
	TextView modelNoTV;
	TextView priceTV;
	TextView urlTV;
	TextView emailTV;
	TextView addressTV;
	TextView phoneNoTV;
	TextView openingHrTV;
	TextView closingHrTV;
	Button callBtn;
	Button urlBtn;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.shoe_view);
		setElements();
	}

	// Get Intents from ViewShoeList and Views from layout
	private void setElements() {

		String modelName = getIntent().getStringExtra("modelName");
		String modelNo = getIntent().getStringExtra("modelNo");
		double price = getIntent().getDoubleExtra("price", 0);
		String address = getIntent().getStringExtra("address");
		String url = getIntent().getStringExtra("url");
		String email = getIntent().getStringExtra("email");
		final int phoneNo = getIntent().getIntExtra("phoneNo", 0);
		double openHr = getIntent().getDoubleExtra("openHr", 0);
		double closeHr = getIntent().getDoubleExtra("closeHr", 0);

		modelNameTV = (TextView) findViewById(R.id.shoeModelTV);
		modelNoTV = (TextView) findViewById(R.id.shoeModelNoTV);
		priceTV = (TextView) findViewById(R.id.priceTV);
		urlTV = (TextView) findViewById(R.id.urlTV);
		emailTV = (TextView) findViewById(R.id.emailTV);
		addressTV = (TextView) findViewById(R.id.addressTV);
		phoneNoTV = (TextView) findViewById(R.id.phoneNoTV);
		openingHrTV = (TextView) findViewById(R.id.openHrTV);
		closingHrTV = (TextView) findViewById(R.id.closingHrTV);
		callBtn = (Button) findViewById(R.id.callBtn);
		urlBtn = (Button) findViewById(R.id.urlBtn);

		modelNameTV.setText(modelName);
		modelNoTV.setText(modelNo);
		priceTV.setText("" + price);
		addressTV.setText(address);
		urlTV.setText(url);
		emailTV.setText(email);
		phoneNoTV.setText("" + phoneNo);
		openingHrTV.setText("" + openHr);
		closingHrTV.setText("" + closeHr);

		callBtn.setOnClickListener(new OnClickListener() {

			public void onClick(View v) {
				// TODO Auto-generated method stub
				// Toast.makeText(getApplicationContext(),
				// "Testing: You are calling now", Toast.LENGTH_LONG).show();
				// Intent intent = new Intent(Intent.ACTION_ALL_APPS);

				Toast.makeText(getApplicationContext(),
						"Testing: You are calling now", Toast.LENGTH_LONG)
						.show();
				Intent intent = new Intent(Intent.ACTION_CALL, Uri.parse("tel:"
						+ phoneNo));

				// Toast.makeText(getApplicationContext(),
				// "Testing: You have dialed the phone number, ready to call now",
				// Toast.LENGTH_LONG).show();
				// Intent intent = new Intent(Intent.ACTION_DIAL,
				// Uri.parse("tel:"+phoneNo));
				startActivity(intent);
			}
		});

		urlBtn.setOnClickListener(new OnClickListener() {

			public void onClick(View v) {
				// TODO Auto-generated method stub
				pop_out_dialog();
			}
		});
	}

	private void pop_out_dialog() {

		AlertDialog.Builder alertbox = new AlertDialog.Builder(this);
		alertbox.setMessage("Do you want to exit?");
		alertbox.setPositiveButton("Yes",
				new DialogInterface.OnClickListener() {
					public void onClick(DialogInterface arg0, int arg1) {
						moveTaskToBack(true);
					}
				});
		alertbox.setNegativeButton("No", new DialogInterface.OnClickListener() {
			public void onClick(DialogInterface dialog, int which) {
				// TODO Auto-generated method stub
				Toast.makeText(getApplicationContext(), "Back to shoes",
						Toast.LENGTH_LONG).show();
			}
		});

		// show the alert box
		alertbox.show();

	}

}
