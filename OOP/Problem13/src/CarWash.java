public class CarWash {
	//Fields
	public String carWashType;
	public boolean coupon;
	public Car car;
	public Outlet outlet;
	
	//Constructor
	public CarWash(String carWashType, boolean coupon, Car car, Outlet outlet) {
		super();
		this.carWashType = carWashType;
		this.coupon = coupon;
		this.car = car;
		this.outlet = outlet;
	}

	//Methods
	public void setCarWashType(String carWashType) {
		this.carWashType = carWashType;
	}
	
	public double calculateCharge() {
		double cost = car.carWashPrice;
		
		if (outlet.premium == true) {
			cost = cost + 1;
		}
		
		if (coupon == true) {
			cost = cost - 0.55;
		}
		
		if (carWashType.equals("Bubble Car Wash")) {
			cost = cost + 0.3;
		}
		
		else if (carWashType.equals("Snow Car Wash")) {
			cost = cost + 0.8;
		}
		
		else if (carWashType.equals("Polish Car Wash")) {
			cost = cost + 2;
		}
		
		else if (carWashType.equals("Wax")) {
			cost = cost + 5;
		}
		return cost;
	}

	public boolean isCoupon() {
		return coupon;
	}

	public void setCoupon(boolean coupon) {
		this.coupon = coupon;
	}

	public Car getCar() {
		return car;
	}

	public void setCar(Car car) {
		this.car = car;
	}

	public Outlet getOutlet() {
		return outlet;
	}

	public void setOutlet(Outlet outlet) {
		this.outlet = outlet;
	}
	
	public void show() {
		System.out.println(this);
	}
	
	public String toString() {
		return "\nCar Wash: " + carWashType + "\nCharges: " + calculateCharge();
	}
}