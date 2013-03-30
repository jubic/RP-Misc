public class MotorBike extends Vehicle {

	int capacity;

	public MotorBike(String aLicensePlate, int aCapacity){
		super(aLicensePlate);
		capacity = aCapacity;
	}
	public void show() {
		super.show();
		System.out.println("MotorBike Engine Capacity is "+capacity);
	}

}