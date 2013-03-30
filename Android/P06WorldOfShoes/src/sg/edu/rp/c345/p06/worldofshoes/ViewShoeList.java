package sg.edu.rp.c345.p06.worldofshoes;

import java.util.ArrayList;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class ViewShoeList extends ListActivity {
	// Declarations
	private ListView shoeListView;
	private ArrayList<Shoe> shoeList = new ArrayList<Shoe>();
	private ArrayList<String> shoeModelName = new ArrayList<String>();
	private ArrayAdapter<String> shoeAdapter;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.shoe_list_view);
		setShoes();
		setElements();
	}

	// Create onListItemClick method
	@Override
	protected void onListItemClick(ListView l, View v, int position, long id) {
		// TODO Auto-generated method stub
		super.onListItemClick(l, v, position, id);
		Intent viewShoe = new Intent(getBaseContext(), ViewShoe.class);
		viewShoe.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP);

		viewShoe.putExtra("modelName", shoeList.get(position).getShoeModel());
		viewShoe.putExtra("modelNo", shoeList.get(position).getShoeModelNo());
		viewShoe.putExtra("email", shoeList.get(position).getEmail());
		viewShoe.putExtra("url", shoeList.get(position).getUrl());
		viewShoe.putExtra("phoneNo", shoeList.get(position).getPhoneNumber());
		viewShoe.putExtra("price", shoeList.get(position).getPrice());
		viewShoe.putExtra("address", shoeList.get(position).getAddress());
		viewShoe.putExtra("openHr", shoeList.get(position).getOpeningHrs());
		viewShoe.putExtra("closeHr", shoeList.get(position).getClosingHrs());
		startActivity(viewShoe);
	}

	// Populate list
	private void setElements() {
		shoeListView = getListView();
		registerForContextMenu(shoeListView);
		shoeAdapter = new ArrayAdapter<String>(this,
				android.R.layout.simple_list_item_1, shoeModelName);
		shoeListView.setAdapter(shoeAdapter);
	}

	private void setShoes() {
		shoeList.add(new Shoe(
				"Yohji Star High",
				"u42815",
				50.00,
				"Basement One, Unit #B1-78, Jurong Point Shopping Centre",
				"http://pid.adidas.com/catalogue/sg/product/U42815/Yohji-Star-High",
				"contact@adidas.com", 62386388, 11.00, 22.00));
		shoeModelName.add("Yohji Star High");
	}
}
