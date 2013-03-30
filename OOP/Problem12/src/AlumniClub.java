public class AlumniClub extends Member {
	public int yearOfGraduation;
	public String occupation;
	
	//constructor
	public AlumniClub(int idNumber, String name, String email, int yearOfGraduation, String occupation) {
		super(idNumber, name, email);
		this.yearOfGraduation = yearOfGraduation;
		this.occupation = occupation;
	}
	
	//method
	public double getGPA() {
		return 0;
	}
	
	public String getOccupation() {
		return occupation;
	}
	
	public String editOccupation(String occupation2) {
		occupation = occupation2;
		return occupation;
	}
	
	public String getClassGroup() {
		return null;
	}
	
	public String editClassGroup(String editClass){
		return null;
	}
	
	public int getYOG() {
		return yearOfGraduation;
	}

	public String toString() {
		return super.toString() + "\tYEAR OF GRADUATION: "  + yearOfGraduation + "\tOCCUPATION: " + occupation;
	}	
}