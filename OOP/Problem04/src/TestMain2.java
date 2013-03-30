// Question 4F
import java.util.Scanner;

public class TestMain2 {
  public static void main(String[] args) {

		Scanner userInput = new Scanner(System.in);

		String[] month = { "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
				"Aug", "Sep", "Oct", "Nov", "Dec" };

		int userNum = 0;
		int count = 0;
	
		try {
		while (userNum != 999) {
			System.out.println("Enter Month No.: 1 to 12 (999 to exit) -");
			userNum = userInput.nextInt();

			if (userNum == 999) {
				break;  //exits While loop
			}	
			System.out.println("You chose - " + month[userNum - 1]);
			count++;
		}
	} 	catch (Exception ex) {
			System.out.println("Please enter only integers");
			 //ex.printStackTrace();	
		}
		System.out.println("Total no. of user input: " + count);
  }
}