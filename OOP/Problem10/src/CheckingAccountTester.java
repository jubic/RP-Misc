public class CheckingAccountTester {
	public static void main(String[] args) {
		CheckingAccount bobsAccount = new CheckingAccount("999", "Bob", 100);
		CheckingAccount jillsAccount = new CheckingAccount("111", "Jill", 500);

		bobsAccount.processCheck(50);
		bobsAccount.processDeposit(200, 25);
		System.out.println(bobsAccount.toString());

		jillsAccount.processDeposit(500);
		jillsAccount.processCheck(100);
		jillsAccount.processCheck(100);
		jillsAccount.processDeposit(100);

		System.out.println(jillsAccount.toString());
	}
}