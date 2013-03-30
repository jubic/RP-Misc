


public class Student {

	String Id;
	String Name;
	
	ManualCar manCar = null;
	AutoCar autoCar = null;
	MotorBike bike = null;
		
	public Student(String aId, String aName){
		Id = aId;
		Name = aName;
	}
	public void show() {
		System.out.println("Student Name & Id = "+ Name+ Id);
		if(manCar != null) {
			manCar.show();
		}
		if(autoCar != null) {
			autoCar.show();
		}
		if(bike != null) {
			bike.show();
		}
		
	}

}
