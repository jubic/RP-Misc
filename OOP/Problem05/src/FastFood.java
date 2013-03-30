import java.util.Scanner;

public class FastFood {
	public static void main(String[] args) {
		int choice = 0;
		
		Scanner userInput = new Scanner(System.in);
		
		double total = 0;

		while (choice != 9) {
			try {
				System.out.println("Welcome to CK's");
				System.out.println("Menu :");
				System.out.println("\t1 - Hamburger <$2.50>");
				System.out.println("\t2 - French Fries <$1.80>");
				System.out.println("\t3 - Soft Drink <$1.40>");
				System.out.println("\t4 - Ice Cream <$0.50>");
				System.out.println("\t9 - Exit");

				System.out.println("Please enter your order : ");
				choice = userInput.nextInt();

				if (choice == 1) {
					// Option 1 actions here
					System.out.println("You have ordered Hamburger");
					// Add $2.50
					total = total + 2.50;
					}
				else if (choice == 2) {
					// Option 2 actions here
					System.out.println("You have ordered French Fries");
					// Add $1.80
					total = total + 1.80;
					} 
				else if (choice == 3) {
					// Option 3 actions here
					System.out.println("You have ordered Soft Drink");
					// Add $1.40
					total = total + 1.40;
					} 
				else if (choice == 4) {
					// Option 4 actions here
					System.out.println("You have ordered Ice Cream");
					// Add $0.50
					total = total + 0.50;
					}
				else if (choice == 9) {
					// Option 'Exit' actions here
					System.out.println("You have chosen to Exit.\nProgram will exit now.");
					System.out.println("Total cost:" + " " + total);					
					} 
				else {
					// Unknown option
					System.out.println("Unknown option, please choose again.");
					}
				
			} catch (Exception e) {
				// catch \n of the scan error exception
				//String junk = userInput.nextLine();
				System.out.println(" ** Error! Unknown option. ** ");
				System.out.println(" ** Please try again ** ");
			}

		}
	}
}