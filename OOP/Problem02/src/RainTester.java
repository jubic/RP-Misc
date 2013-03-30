import java.util.Scanner;

public class RainTester {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String answer;
		
		System.out.println("Is it raining? (Y or N): ");
		answer = scan.nextLine();
		
		if (answer.equals("Y")) {
			System.out.println("Wipers On");
		} else {
			System.out.println("Wipers Off");
		}
	}
}