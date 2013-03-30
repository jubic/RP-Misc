package sg.edu.rp.c345.p10.theweatherman;

import android.graphics.drawable.Drawable;

public class City {

	// Declarations
	long id;
	String city;
	String temperature;
	String condition;
	Drawable icon;
	
	// Constructor
	public City(long id, String city, String temperature, String condition, Drawable icon) {
		super();
		this.id = id;
		this.city = city;
		this.temperature = temperature;
		this.condition = condition;
		this.icon = icon;
	}
	
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}
	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getWeather() {
		return temperature;
	}

	public void setWeather(String weather) {
		this.temperature = weather;
	}

	public String getCondition() {
		return condition;
	}

	public void setCondition(String condition) {
		this.condition = condition;
	}

	public Drawable getIcon() {
		return icon;
	}

	public void setIcon(Drawable icon) {
		this.icon = icon;
	}

	@Override
	public String toString() {
		return "Current Temperature:" + temperature + "\n" + condition;
	}
}
