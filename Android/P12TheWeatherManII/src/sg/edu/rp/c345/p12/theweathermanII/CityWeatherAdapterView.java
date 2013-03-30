package sg.edu.rp.c345.p12.theweathermanII;

import android.content.Context;
import android.view.View;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class CityWeatherAdapterView extends RelativeLayout {

	public CityWeatherAdapterView(Context context, City city) {
		super(context);
		View v = inflate(context, R.layout.individual_city, null);
		
		TextView countryTV = (TextView)v.findViewById(R.id.countryTV);
		TextView contentTV = (TextView)v.findViewById(R.id.descriptionTV);
		ImageView weatherIV = (ImageView)v.findViewById(R.id.weatherIV);
		
		countryTV.setText(city.getCity());
		contentTV.setText(city.toString());
		weatherIV.setImageDrawable(city.getIcon());
		addView(v);
	}
}
