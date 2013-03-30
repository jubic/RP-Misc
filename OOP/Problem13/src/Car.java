import java.util.ArrayList;

public class Car {
	//Fields
	public String carType;
	public String licensePlate;
	public double carWashPrice;
	public int coupons;
	ArrayList<CarWash> services;
	
	//Constructor
	public Car(String carType, String licensePlate, double carWashPrice) {
		super();
		this.carType = carType;
		this.licensePlate = licensePlate;
		this.carWashPrice = carWashPrice;
		this.services = new ArrayList<CarWash>();
	}

	//Method
	public String getCarType() {
		return carType;
	}

	public void setCarType(String carType) {
		this.carType = carType;
	}

	public String getLicensePlate() {
		return licensePlate;
	}

	public void setLicensePlate(String licensePlate) {
		this.licensePlate = licensePlate;
	}

	public double getCarPrice() {
		return carWashPrice;
	}

	public void setCarPrice(double carWashPrice) {
		this.carWashPrice = carWashPrice;
	}
	
	public double getCarWashPrice() {
		return carWashPrice;
	}

	public void setCarWashPrice(double carWashPrice) {
		this.carWashPrice = carWashPrice;
	}
	
	public int getCoupons() {
		return coupons;
	}

	public void setCoupons(int coupons) {
		this.coupons = coupons;
	}

	public void show() {
		System.out.println(this);
	}
	
	public String toString() {
		return "License Plate: " + licensePlate + "\nCar Type: " + carType + services + "\n";
	}
}