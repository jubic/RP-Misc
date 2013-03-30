import java.util.Random;
import java.util.Scanner;
//import java.util.InputMismatchException;

public class Solution {
	public static void main(String args[]) {
		Scanner userInput = new Scanner(System.in);
		Random generator = new Random();
		int[] arrayRandomNumber = new int[5];

		for (int i = 0; i < arrayRandomNumber.length; i++) {
			arrayRandomNumber[i] = generator.nextInt(50) + 1;
		}

		// sets default score results as zero
		int gameScore = 0;

		// Display the hidden number
		for (int i = 0; i < arrayRandomNumber.length; i++) {
			System.out.print(arrayRandomNumber[i] + " ");
		}

		// Game instructions
		System.out.print("\n");
		System.out.print("\nFive numbers has been created!");
		System.out.print("\nNumbers are from 1 to 50");
		System.out.print("\nYou have 3 tries to guess the numbers.");
		System.out.print("\n");

		// player enters letters 3 times
		for (int i = 0; i < 3; i++) {
			boolean needToLoop = true;
			// continue to next try only after input is accepted
			while (needToLoop) {
				try {
					System.out.println("\nEnter a number (INTEGER ONLY):");
					int userNumGuess = userInput.nextInt();

					if (userNumGuess >= 1 && userNumGuess <= 50) {

						// compare the entered number with the random numbers
						for (int j = 0; j < arrayRandomNumber.length; j++) {
							if (userNumGuess == arrayRandomNumber[j]) {
								// number match so calculate score
								gameScore = gameScore + 1;
							}
							needToLoop = false;
						}
						
					} else {
						System.out.println(" ** Error! Only enter number 1 to 50 ** ");
						System.out.println(" ** Please try again ** ");
					}

				} catch (Exception e) {
					// } catch (InputMismatchException e) {
					// catch \n of the scan error exception
					@SuppressWarnings("unused")
					String junk = userInput.nextLine();
					System.out.println(" ** Error! You have not enter a correct number ** ");
					System.out.println(" ** Please try again ** ");
				}
			}
		}

		// prints out the message of success or failure to match
		if (gameScore > 0) {
			System.out.print("\n");
			System.out.println("** The number match! You WIN!! ** ");
			System.out.println("** Total score = " + gameScore);
		} else {
			System.out.print("\n");
			System.out.println("** None of the number matches!");
		}

	}
}
