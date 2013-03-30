import java.util.ArrayList;

public class Outlet {
	//Fields
	public String location;
	public boolean premium;
	public double charge;
	ArrayList<Car> carList = new ArrayList <Car>();
	
	//Constructor
	public Outlet(String location, boolean premium, double charge) {
		super();
		this.location = location;
		this.premium = premium;
		this.charge = charge;
	}

	//Methods
	public String getLocation() {
		return location;
	}

	public void setLocation(String location) {
		this.location = location;
	}

	public boolean isPremium() {
		return premium;
	}

	public void setPremium(boolean premium) {
		this.premium = premium;
	}

	public double getCharge() {
		return charge;
	}

	public void setCharge(double charge) {
		this.charge = charge;
	}
	
	public void show() {
		System.out.println(this);
		for (Car car : carList) {
			car.show();
		}
	}
	
	public String toString() {
		return "Location: " + location + "\n-----------------------------------";
	}
}