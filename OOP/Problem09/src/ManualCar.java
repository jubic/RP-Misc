public class ManualCar extends Vehicle{
	
	int numPassengers;
	int numGears;
	
	public ManualCar(String aLicensePlate, int aNumPass, int aNumGears) {
		super(aLicensePlate);
		numPassengers = aNumPass;
		numGears = aNumGears;
	}//end constructor
	
	public void show() {
		super.show();
		System.out.println("ManualCar numPassengers is "+numPassengers+" numGears = "+numGears);
		
	}//end show

}//end class
