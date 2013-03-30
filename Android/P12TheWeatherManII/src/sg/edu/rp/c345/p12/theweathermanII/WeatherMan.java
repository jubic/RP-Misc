package sg.edu.rp.c345.p12.theweathermanII;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;
import java.util.ArrayList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import android.app.AlertDialog;
import android.app.ListActivity;
import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;

public class WeatherMan extends ListActivity {

	// Declarations
	DbAdapter db;
	ArrayList<City> cityList = new ArrayList<City>();
	CityWeatherAdapter cwAdapter = new CityWeatherAdapter(this, cityList);
	ListView lv;
	EditText cityEditText;
	Button submitBtn;
	Runnable getWeather;
	Handler weatherHandler;

	static final private int REMOVE_CITIES = Menu.FIRST;
	static final private int REFRESH_CITIES = Menu.FIRST + 1;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		
		setElements();
		
		SharedPreferences sf = PreferenceManager
				.getDefaultSharedPreferences(this);
		final SharedPreferences.Editor sfEdit = sf.edit();

		if (!sf.contains("hasRun")) {
			sfEdit.putBoolean("hasRun", false);

			AlertDialog.Builder eulaAlert = new AlertDialog.Builder(this);
			eulaAlert.setTitle("EULA");

			eulaAlert.setPositiveButton("Agree",
					new DialogInterface.OnClickListener() {

						@Override
						public void onClick(DialogInterface dialog,
								int whichButton) {

							sfEdit.putBoolean("hasRun", true);
							sfEdit.commit();

							getCities();
							submitBtn.setOnClickListener(saveItemClick);
						}

					});
			eulaAlert.setNegativeButton("Disagree",
					new DialogInterface.OnClickListener() {

						@Override
						public void onClick(DialogInterface dialog,
								int whichButton) {

							System.exit(0);

						}

					});
			eulaAlert.show();
		}
		
		else if(sf.contains("hasRun")) {
			// Do nothing.
		}
		
		else {
			AlertDialog.Builder eulaAlert = new AlertDialog.Builder(this);
			eulaAlert.setTitle("EULA");

			eulaAlert.setPositiveButton("Agree",
					new DialogInterface.OnClickListener() {

						@Override
						public void onClick(DialogInterface dialog,
								int whichButton) {

							sfEdit.putBoolean("hasRun", true);
							sfEdit.commit();

							getCities();
							submitBtn.setOnClickListener(saveItemClick);
						}

					});
			eulaAlert.setNegativeButton("Disagree",
					new DialogInterface.OnClickListener() {

						@Override
						public void onClick(DialogInterface dialog,
								int whichButton) {

							System.exit(0);

						}

					});
			eulaAlert.show();
		}
	}

	@Override
	protected void onResume() {
		// TODO Auto-generated method stub
		super.onResume();

		getWeather = new Runnable() {
			@Override
			public void run() {
				/*
				 * This is where you place the method or codes that does your
				 * ‘work’ In this run messages can be sent to the handler to
				 * update the UI using either sendEmptyMessage() or
				 * sendMessage() methods.
				 */

				for (int i = 0; i < cityList.size(); i++) {
					
					XMLParser(cityList.get(i).getCity());
					
					weatherHandler.sendEmptyMessage(0);
					
				}
			}
		};

		weatherHandler = new Handler() {
			public void handleMessage(Message msg) {
				cwAdapter.notifyDataSetChanged();
			}
		};

		Thread t = new Thread(getWeather, "Weather");
		t.start();

	}

	private OnClickListener saveItemClick = new OnClickListener() {
		public void onClick(View v) {
			insertCity();
		}
	};

	private void setElements() {
		db = new DbAdapter(this);
		cityEditText = (EditText) findViewById(R.id.cityEditText);
		submitBtn = (Button) findViewById(R.id.submitBtn);

		lv = getListView();
		lv.setAdapter(cwAdapter);

		// register it for the context menu
		registerForContextMenu(lv);
	}

	private void insertCity() {
		// Get EditText & Read the value inside
		String newCityName = cityEditText.getText().toString();

		// Don't proceed if EditText is empty
		if (newCityName.compareTo("") == 0) {
			return;
		}

		XMLParser(newCityName);
		cwAdapter.notifyDataSetChanged();
		db.open();
		db.insertCity(newCityName);
		db.close();
	}

	public void getCities() {
		db.open();

		Cursor c = db.getAllCities();

		if (c.moveToFirst()) {
			do {
				String city = c.getString(c
						.getColumnIndex(DbAdapter.KEY_CITY_NAME));
				XMLParser(city);
				Log.d("City inserted", city);
			} while (c.moveToNext());
		}
		c.close();

		db.close();
	}

	private void removeCity(int location) {
		db.open();
		db.removeCity(cityList.get(location).getCity());
		db.close();
		cityList.remove(location);
	}

	private void removeAllCities() {
		db.open();
		db.removeAllCities();
		db.close();
		cityList.clear();
	}

	private void refreshCities() {
		getCities();
	}

	// Create options menu (triggered by Menu key)
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		super.onCreateOptionsMenu(menu);

		// Create and add new menu items.
		MenuItem itemRem = menu.add(0, REMOVE_CITIES, Menu.NONE,
				R.string.remove_all);
		MenuItem itemRefresh = menu.add(0, REFRESH_CITIES, Menu.NONE,
				R.string.refresh);
		itemRem.setIcon(android.R.drawable.ic_menu_delete);
		itemRefresh.setIcon(R.drawable.ic_menu_refresh);
		return true;

	}

	// Handle options menu
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		super.onOptionsItemSelected(item);
		switch (item.getItemId()) {
		case (REMOVE_CITIES):
			// Clear cityList
			removeAllCities();
			cwAdapter.notifyDataSetChanged();
			break;
		case (REFRESH_CITIES):
			/*
			 * Refresh cityList (Kinda redundant since the server only updates
			 * every half hour, not real time).
			 */
			refreshCities();
			break;
		}
		return true;
	}

	// Create context menu (Press and hold on List item)
	@Override
	public void onCreateContextMenu(ContextMenu menu, View v,
			ContextMenu.ContextMenuInfo menuInfo) {
		super.onCreateContextMenu(menu, v, menuInfo);
		menu.setHeaderTitle("Actions");
		menu.add(0, REMOVE_CITIES, Menu.NONE, R.string.remove);
	}

	// Handle context menu
	@Override
	public boolean onContextItemSelected(MenuItem item) {
		super.onContextItemSelected(item);

		// Get selected index
		AdapterView.AdapterContextMenuInfo menuInfo;
		menuInfo = (AdapterView.AdapterContextMenuInfo) item.getMenuInfo();
		int index = menuInfo.position;

		switch (item.getItemId()) {
		case (REMOVE_CITIES):
			removeCity(index);
			cwAdapter.notifyDataSetChanged();
			return true;
		}
		return false;
	}

	private void XMLParser(String cityname) {
		// Get the XML
		URL url;

		try {

			String encodedCityName = URLEncoder.encode(cityname);
			// Get the city name and construct the full URL to get the XML file
			String StringUrl = "http://www.google.com/ig/api?weather="
					+ encodedCityName;

			Log.d("URL encoded", encodedCityName);
			url = new URL(StringUrl);

			URLConnection connection;
			connection = url.openConnection();

			// Starts a HTTP connection
			HttpURLConnection httpConnection = (HttpURLConnection) connection;
			int responseCode = httpConnection.getResponseCode();

			// Standard response for successful HTTP requests
			if (responseCode == HttpURLConnection.HTTP_OK) {
				InputStream in = httpConnection.getInputStream();

				// A factory API that enables applications to obtain a parser
				// that produces DOM object trees from XML documents
				DocumentBuilderFactory dbf = DocumentBuilderFactory
						.newInstance();
				DocumentBuilder db = dbf.newDocumentBuilder();

				// Parse the RSS feed
				Document dom = db.parse(in);
				Element docEle = dom.getDocumentElement();

				// Get the current weather condition by the Tag Name -
				// current_conditions
				NodeList nl = docEle.getElementsByTagName("current_conditions");

				// Retrieve the child elements in *current_conditions*
				if (nl != null && nl.getLength() > 0) {

					// If there are more than 1 *current_conditions*, it will go
					// through each of the XML tree of *current_conditions* and
					// retrieve the content from there. This will be more
					// applicable for *weather_forecase*

					for (int i = 0; i < nl.getLength(); i++) {
						Element entry = (Element) nl.item(i);

						// Retrieve the child elements by its various tag
						// name - Complete the following to obtain all the
						// necessary information

						Element condition_data = (Element) entry
								.getElementsByTagName("condition").item(0);
						Element temp_data = (Element) entry
								.getElementsByTagName("temp_c").item(0);

						// Extract the String content of the child elements
						String temperature = temp_data.getAttributeNode("data")
								.getValue();
						String condition = condition_data.getAttributeNode(
								"data").getValue();

						// Prepares the string format the full URL of the image
						Element imageSrc = (Element) entry
								.getElementsByTagName("icon").item(0);
						String img = "http://www.google.com"
								+ imageSrc.getAttributeNode("data").getValue();

						// Get the image from the URL above
						InputStream is = (InputStream) new URL(img)
								.getContent();
						Drawable imgDrawable = Drawable.createFromStream(is,
								img);
						// weatherIV.setImageDrawable(imgDrawable);
						Log.d("Country loaded in xml", cityname);
						City cityObj = new City(0, cityname, temperature,
								condition, imgDrawable);
						cityList.add(cityObj);
					}
				}
			}
		} catch (MalformedURLException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		} catch (SAXException e) {
			e.printStackTrace();
		}
	}
}