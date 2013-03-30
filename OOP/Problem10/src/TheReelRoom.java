public class TheReelRoom {
	public static void main(String[] args) {
		Cook paul = new Cook(2, 20, "Paul Jon", 2034.3, 40, "Raffles City");
		paul.printStaffInfo();

		// Trying to access private properties directly
		// paul.name = "Jean";
		// System.out.println(paul.numCustomers);

		// Correct way: use the public getters/setters
		paul.setName("Jean");
		System.out.println(paul.getNumCustomers());

		System.out.println(paul.calculSalary(0.1));

	}

}
