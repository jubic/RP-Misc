import java.util.Scanner;

public class Menu {
	public static void main(String[] args) {
		int choice = 0;
		Scanner userInput = new Scanner(System.in);

		while (choice != 9) {
			try {

				System.out.println("Menu :");
				System.out.println("\t1 - Option 1");
				System.out.println("\t2 - Option 2");
				System.out.println("\t3 - Option 3");
				System.out.println("\t4 - Option 4");
				System.out.println("\t9 - Exit");

				System.out.println("Please enter your order : ");
				choice = userInput.nextInt();

				if (choice == 1) {
					// Option 1 actions here
					System.out.println("You have chosen Option 1.");
					System.exit(0);
				} else if (choice == 2) {
					// Option 2 actions here
					System.out.println("You have chosen Option 2.");
					System.exit(0);
				} else if (choice == 3) {
					// Option 3 actions here
					System.out.println("You have chosen Option 3.");
					System.exit(0);
				} else if (choice == 4) {
					// Option 4 actions here
					System.out.println("You have chosen Option 4.");
					System.exit(0);
				} else if (choice == 9) {
					// Option 'Exit' actions here
					System.out.println("You have chosen to Exit.\nProgram will exit now.");
				} else {
					// Unknown option
					System.out.println("Unknown option, please choose again.");
				}
				
			} catch (Exception e) {
				// catch \n of the scan error exception
				@SuppressWarnings("unused")
				String junk = userInput.nextLine();
				System.out.println(" ** Error! Unknown option. ** ");
				System.out.println(" ** Please try again ** ");
			}
		}
	}
}