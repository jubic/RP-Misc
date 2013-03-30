public class RegularClub extends Member{
	public String diploma;
	public String school;
	public String classGroup;
	public double gpa;
	
	//constructor
	public RegularClub(int idNumber, String name, String email, String diploma, String school, String classGroup, double gpa) {
		super(idNumber, name, email);
		this.diploma = diploma;
		this.school = school;
		this.classGroup = classGroup;
		this.gpa = gpa;
	}
	
	//methods
	public String getClassGroup() {
		return classGroup;
	}
	
	public double getGPA() {
		return gpa;
	}
	public String getOccupation() {
		return null;
	}
	
	public String editClassGroup(String editClass){
		classGroup = editClass;
		return classGroup;
	}
	
	public String editOccupation(String occupation2) {
		return null;
	}
	
	public int getYOG(){
		return 0;
	}
	
	public String toString() {
		return super.toString() + "\tDIPLOMA: " + diploma + "\tSCHOOL: " + school + "\t" + "CLASSGROUP: " + classGroup + "\t" + "GPA: " + gpa;  
	}
}