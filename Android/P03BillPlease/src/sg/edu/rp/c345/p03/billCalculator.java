package sg.edu.rp.c345.p03;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.text.DecimalFormat;

public class billCalculator extends Activity {
	TextView billTextView, paxTextView, discountTextView, resultTextView;
	EditText billEditText, discountEditText;
	Spinner paxSpinner;
	CheckBox serviceChargeCheckBox, gstChargeCheckBox, cessChargeCheckBox;
	Button calculateButton, resetButton;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.main);

		// Get views from layout
		billTextView = (TextView) findViewById(R.id.billTextView);
		billEditText = (EditText) findViewById(R.id.billEditText);
		paxTextView = (TextView) findViewById(R.id.paxTextView);
		paxSpinner = (Spinner) findViewById(R.id.paxSpinner);
		discountTextView = (TextView) findViewById(R.id.discountTextView);
		discountEditText = (EditText) findViewById(R.id.discountEditText);
		serviceChargeCheckBox = (CheckBox) findViewById(R.id.serviceChargeCheckBox);
		gstChargeCheckBox = (CheckBox) findViewById(R.id.gstChargeCheckBox);
		cessChargeCheckBox = (CheckBox) findViewById(R.id.cessChargeCheckBox);
		calculateButton = (Button) findViewById(R.id.calculateButton);
		resetButton = (Button) findViewById(R.id.resetButton);
		resultTextView = (TextView) findViewById(R.id.resultTextView);

		// Set ArrayAdapter for paxSpinner
		ArrayAdapter<CharSequence> paxAdapter = ArrayAdapter
				.createFromResource(this, R.array.pax,
						android.R.layout.simple_spinner_item);
		paxAdapter
				.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
		paxSpinner.setAdapter(paxAdapter);

		// Set splitBill() function for calculateButton
		calculateButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				splitBill();
			}
		});

		// Set clearBill() function for resetButton
		resetButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				clearBill();
			}
		});
	}

	public void splitBill() {
		if (billEditText.getText().toString().length() == 0) {
			Context context = getApplicationContext();
			CharSequence text = "Please enter bill amount";
			int duration = Toast.LENGTH_SHORT;
			Toast toast = Toast.makeText(context, text, duration);
			toast.show();
			return;
		}
		if (discountEditText.getText().toString().length() == 0) {
			discountEditText.setText("0");
		}

		// Get numbers from widgets
		double totalBill;
		double bill = Double.parseDouble(billEditText.getText().toString());
		ArrayAdapter<?> getPaxSpinnerAdapter = (ArrayAdapter<?>) paxSpinner
				.getAdapter();
		String noPax = (String) getPaxSpinnerAdapter.getItem(paxSpinner
				.getSelectedItemPosition());
		int pax = Integer.parseInt(noPax.toString());
		double discountPercentage = Double.parseDouble(discountEditText
				.getText().toString());
		/*
		 * Calculation
		 * bill = 10, pax = 2, discount = 10, Include SC, GST, CESS (10, 7, 1
		 * respectively) bill = 10 - (10 * (10/100)) = 9 If all checkboxes are
		 * checked, totalBill = bill + (bill * (0.1+0.07+0.01)) = 10.62 Since
		 * pax = 2, totalBill/2 = 5.31
		 */
		totalBill = bill = bill - (bill * (discountPercentage / 100));
		if (serviceChargeCheckBox.isChecked()) {
			totalBill += bill * 0.1;
		}
		if (gstChargeCheckBox.isChecked()) {
			totalBill += bill * 0.07;
		}
		if (cessChargeCheckBox.isChecked()) {
			totalBill += bill * 0.01;
		}

		double perPax = totalBill / pax;

		// Decimal Formatting
		DecimalFormat moneyFormat = new DecimalFormat("###,###.##");

		resultTextView.setText("Total Bill Amount is: S$"
				+ moneyFormat.format(totalBill) + "\nNumber of Pax Sharing: "
				+ pax + "\nEach has to pay: S$" + moneyFormat.format(perPax));
	}

	public void clearBill() {
		billEditText.setText("");
		discountEditText.setText("");
		paxSpinner.setSelection(0);
		serviceChargeCheckBox.setChecked(false);
		gstChargeCheckBox.setChecked(false);
		cessChargeCheckBox.setChecked(false);
		resultTextView.setText("");
		return;
	}
}