public class Staff {
	private int grade, age;
	private String name;
	private double basicSalary;

	public Staff(int grade, int age, String name, double basicSalary) {
		this.grade = grade;
		this.age = age;
		this.name = name;
		this.basicSalary = basicSalary;
	}

	public int getGrade() {
		return grade;
	}

	public int getAge() {
		return age;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getBasicSalary() {
		return basicSalary;
	}

	public void printStaffInfo() {
		String output = "Staff [age=" + age + ", basicSalary=" + basicSalary
				+ ", grade=" + grade + ", name=" + name + "]";
		System.out.println(output);
	}

}
