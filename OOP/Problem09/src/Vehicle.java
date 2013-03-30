public class Vehicle {

	String licensePlate;
	boolean avail;
	
	public Vehicle(String aLicensePlate) {
		licensePlate = aLicensePlate;
		avail = true;
	}//end constructor
	
	// display vehicle info
	public void show() {
		System.out.print("Vehicle licensePlate is "+licensePlate + " avail is "+avail+" ");
	}//end show
	
	// set avail to false to assign vehicle to student
	public boolean isVehicleAvailable() {
		return avail;
	}//assignVehicle
	
	// set avail to false to assign vehicle to student
	public void setAvail(boolean aAvail) {
		avail = aAvail;
	}//assignVehicle
	
}//end class
