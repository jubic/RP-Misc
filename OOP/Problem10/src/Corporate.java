public class Corporate extends Staff {
	private int yearSvc;
	private String email;

	public Corporate(int grade, int age, String name, double basicSalary,
			int yearSvc, String email) {
		super(grade, age, name, basicSalary);
		this.yearSvc = yearSvc;
		this.email = email;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String eml) {
		this.email = eml;
	}

	public int getYearSvc() {
		return yearSvc;
	}

	public void setYearSvc(int years) {
		this.yearSvc = years;
	}

}
