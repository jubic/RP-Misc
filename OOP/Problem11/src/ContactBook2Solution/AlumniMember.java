package ContactBook2Solution;

public class AlumniMember extends Member {
	int yearOfGraduation;
	String occupation;

	public AlumniMember(int id, String name, String email,
			int yearOfGraduation, String occupation) {
		super(id, name, email);
		this.yearOfGraduation = yearOfGraduation;
		this.occupation = occupation;
	}

	public String getOccupation() {
		return occupation;
	}
	
	public void printMemberInfo() {
		super.printMemberInfo();
		String output = "Year of Graduation: " + this.yearOfGraduation
					+ "\tOccupation=" + this.occupation;
		System.out.println(output);
	}
}