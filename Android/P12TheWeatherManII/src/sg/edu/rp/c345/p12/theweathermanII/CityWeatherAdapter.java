package sg.edu.rp.c345.p12.theweathermanII;

import java.util.ArrayList;

import android.content.Context;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;

public class CityWeatherAdapter extends BaseAdapter {

	private Context context;
	private ArrayList<City> cityList;
	
	public CityWeatherAdapter(Context context, ArrayList<City> cityList) {
		// TODO Auto-generated constructor stub
		this.context = context;
		this.cityList = cityList;
	}

	public int getCount() {
		// TODO Auto-generated method stub
		return cityList.size();
	}

	public Object getItem(int index) {
		// TODO Auto-generated method stub
		return cityList.get(index);
	}

	public long getItemId(int index) {
		// TODO Auto-generated method stub
		return cityList.get(index).getId();
	}

	public View getView(int index, View arg1, ViewGroup arg2) {
		City entry = cityList.get(index);
		return new CityWeatherAdapterView(context, entry);
	}
}
