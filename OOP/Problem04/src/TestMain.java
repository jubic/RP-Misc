// Question 4b
import java.util.Scanner;

public class TestMain {
  public static void main(String[] args) {

		Scanner userInput = new Scanner(System.in);

		String[] month = { "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
				"Aug", "Sep", "Oct", "Nov", "Dec" };

		int userNum = 0;
		int count = 0;

		while (userNum != 999) {
			System.out.println("Enter Month No.: 1 to 12 (999 to exit) -");
			userNum = userInput.nextInt();

			if (userNum == 999) {
				break;  //exits While loop
			}

			System.out.println("You chose - " + month[userNum - 1]);
			count++;
		}

		System.out.println("Total no. of user input: " + count);
  }
}