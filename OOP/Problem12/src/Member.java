public abstract class Member {
	public int idNumber;
	public String name;
	public String email;
	
	//constructor
	public Member(int idNumber, String name, String email) {
		this.idNumber = idNumber;
		this.name = name;
		this.email = email;	
	}
	
	//methods
	public abstract double getGPA();
	public abstract String getOccupation();
	public abstract String getClassGroup();
	public abstract int getYOG();
	public abstract String editClassGroup(String editClass);
	public abstract String editOccupation(String occupation);
	
	public void show() {
		System.out.println(this);
	}
	public String toString() {
		return "ID NO: " + idNumber + "\t" + "NAME: " + name + "\tEMAIL: " + email;
	}	
}