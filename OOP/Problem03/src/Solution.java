import java.util.Scanner;

public class Solution {

	public static void main(String args[]) {
		double savingInPiggyBank = 0.0;
		double totalSpending = 0.0;
		Scanner userInput = new Scanner(System.in);
		double earnings = 1000.0;
		double[] arraySpending = new double[12];
		int counter = 1;

		System.out.println("Enter Bank's Interest Rate: ");
		double interest = userInput.nextDouble();

		while (counter <= 12) {
			System.out.println("\n ====== MONTH " + counter + " =====");
			System.out.println("Earnings for the month = $" + earnings);
			System.out.println("Total cash on hand = $"
					+ (savingInPiggyBank + earnings));

			System.out.println("Enter amount $ spent for this month : ");
			arraySpending[counter - 1] = userInput.nextDouble();

			while (arraySpending[counter - 1] > savingInPiggyBank + earnings) {
				System.out
						.println(" ** Error! You cannot spend more than you have on hand! ** ");
				System.out.println("Enter amount $ spent for this month : ");
				arraySpending[counter - 1] = userInput.nextDouble();
			}

			savingInPiggyBank = savingInPiggyBank * ((100.0 + interest) / 100)
					+ (earnings - arraySpending[counter - 1]);
			System.out.println(">> Piggy Bank Report for Month " + counter);
			System.out.println(">> Total Savings after Interest = $"
					+ savingInPiggyBank);

			counter = counter + 1;
		}

		counter = 1;
		System.out.println("\n\n>>> END OF YEAR REPORT ");

		while (counter <= 12) {
			System.out.println("\tMonth" + counter + ": Earnings=$" + earnings
					+ "\tSpending=$" + arraySpending[counter - 1]);
			totalSpending = totalSpending + arraySpending[counter - 1];
			counter = counter + 1;
		}

		System.out.println(">>> TOTAL EARNINGS = $" + (earnings * 12));
		System.out.println(">>> TOTAL SPENDING = $" + totalSpending);
		System.out.println(">>> AVERAGE MONTHLY SPENDING = $"
				+ (totalSpending / 12.0));
		System.out.println(">>> END OF YEAR SAVINGS = $" + savingInPiggyBank);
	}
}