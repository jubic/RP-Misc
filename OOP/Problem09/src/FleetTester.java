public class FleetTester {
	public static void main(String[] args) {
		Fleet myCars = new Fleet(1000, 1234, 10, 777, 999, 20);
		System.out.println("Fleet average MPG= " + myCars.calculateMPG());

		myCars.fillUp(1434, 10, 1099, 10);
		System.out.println("new average MPG= " + myCars.calculateMPG());
	}
}