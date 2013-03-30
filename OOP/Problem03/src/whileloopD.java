import java.util.Scanner;
public class whileloopD {
	public static void main(String[] args) {
		Scanner userInput = new Scanner(System.in);
		int num = 0;
		boolean askAgain = true;
		
		System.out.println("Enter your desired maximum number: ");
		int max = userInput.nextInt();
		
		while (askAgain) {
			System.out.println("Enter a number between 1 to "+max+": ");
			num = userInput.nextInt();
			
			if (num <= max && num>0) {
				askAgain = false;
			}
		}
System.out.println("You entered " + num);
	}

}
