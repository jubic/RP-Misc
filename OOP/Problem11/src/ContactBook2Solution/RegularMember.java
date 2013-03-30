package ContactBook2Solution;

public class RegularMember extends Member {
	private Diploma diploma;
	private School school;
	private String classGroup;
	private double gpa;

	public RegularMember(int id, String name, String email, Diploma diploma,
			School school, String classGroup, double gpa) {
		super(id, name, email);
		this.diploma = diploma;
		this.school = school;
		this.classGroup = classGroup;
		this.gpa = gpa;
	}

	public double getGpa() {
		return gpa;
	}
	
	public void printMemberInfo() {
		super.printMemberInfo();
		String output = "Diploma: " + this.diploma + "\tSchool: " + this.school
					+ "\tClass: " + this.classGroup + "\tGPA: " + this.gpa;
		System.out.println(output);
	}
}