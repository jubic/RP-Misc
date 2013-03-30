public class AutoCar extends Vehicle {
	
	int numPassengers;
	
	public AutoCar(String aLicensePlate, int aNumPass){
		super(aLicensePlate);
		numPassengers = aNumPass;
	}
	public void show() {
		super.show();
		System.out.println("AutoCar numPassengers is "+numPassengers);
		
	}//end show
}
