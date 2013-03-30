public class Cook extends Staff {
	private int numCustomers; // number of customers served
	private String branchLocation; // branch location

	public Cook(int grade, int age, String name, double basicSalary,
			int numCustomers, String branchLocation) {
		super(grade, age, name, basicSalary);
		this.numCustomers = numCustomers;
		this.branchLocation = branchLocation;
	}

	public int getNumCustomers() {
		return numCustomers;
	}

	public String getBranchLocation() {
		return branchLocation;
	}

	@Override
	public String toString() {
		return "Cook [branchLocation=" + branchLocation + ", numCustomers="
				+ numCustomers + "]";
	}

	/**
	 * Method to print Cook information Overrides the printStaffInfo method of
	 * the superclass
	 */
	public void printStaffInfo() {
		super.printStaffInfo(); // print the grade, name, age, basic salary by
		// calling the printStaffInfo method from the
		// superclass

		// Print the other information
		System.out.println("Number of Customers Served: " + numCustomers);
		System.out.println("Branch Location: " + branchLocation);
	}

	/**
	 * Method to calculate the salary payable Salary payable = (basic salary +
	 * bonus) - tax contributions The bonus and tax contributions are calculated
	 * by 2 other private methods
	 * 
	 * @param tax
	 *            the tax percentage
	 * @return the salary payable
	 */
	public double calculSalary(double tax) {

		double taxContrib = calculTax(tax); // tax contributions
		double bonus = calculBonus();

		/*
		 * Note: basicSalary is private in the superclassTo access it, use its
		 * public getter method: getBasicSalary
		 */
		return (getBasicSalary() + bonus) - taxContrib;

		/**
		 * OR return return (getBasicSalary() + calculBonus()) - calculTax(tax);
		 */
	}

	/**
	 * Private method to calculate the tax contributions Tax contribution = tax
	 * rate * basic salary
	 * 
	 * @param tax
	 *            the tax percentage
	 * @return the tax to be paid
	 */
	private double calculTax(double tax) {
		/*
		 * Note: basicSalary is private in the superclassTo access it, use its
		 * public getter method: getBasicSalary
		 */
		return (tax * getBasicSalary());
	}

	/**
	 * Private method to calculate bonus For cooks, bonus = number of customers
	 * served/basic salary
	 * 
	 * @return the bonus
	 */
	private double calculBonus() {
		/*
		 * Now: we can access numCustomers directly since it is in this class
		 */
		return numCustomers / getBasicSalary();
	}

}
