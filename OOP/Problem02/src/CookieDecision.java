import java.util.Scanner;

public class CookieDecision {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int hunger, look, smell;
		
		System.out.println("How hungry are you? (1-10): ");
		hunger = scan.nextInt();
		System.out.println("You entered " + hunger);
		
		if (hunger >= 1 && hunger <= 10) {
			System.out.println("Number is within the range of 1-10");
		}	else {
			System.out.println("Number is not within the range of 1-10");
			System.exit(0);
		}
		System.out.println("How nice do the cookies look? (1-10): ");
		look = scan.nextInt();
		System.out.println("You entered " + look);
		
		if (look >= 1 && look <= 10) {
			System.out.println("Number is within the range of 1-10");
		}	else {
			System.out.println("Number is not within the range of 1-10");
			System.exit(0);
		}
		
		System.out.println("How nice do the cookies smell? (1-10): ");
		smell = scan.nextInt();
		System.out.println("You entered " + smell);
		
		if (smell >= 1 && smell <= 10) {
			System.out.println("Number is within the range of 1-10");
		}	else {
			System.out.println("Number is not within the range of 1-10");
			System.exit(0);
		}
		
		if (( hunger + look + smell) > 15) {
			System.out.println("Buy cookies!");
		}
		System.out.println("Continue down the Mall.");
	}

}
