// To save the hassle of importing of both Random & Scanner modules separately
import java.util.*;

public class ProblemAnswer {
	public static void main(String[] args) {
		// Create Scanner
		Scanner scan = new Scanner(System.in);
		
		int numberGuess = 0;
		int numbersMatched = 0;
		
		// Create a "Random Number" generator
		@SuppressWarnings("unused")
		Random generator = new Random();
		int[] arrayRandomNumber = new int[5];
		
		//Quoted to hide the random numbers from player
		/* Prints out the numbers
		for (int i = 0; i < arrayRandomNumber.length; i++) {
			arrayRandomNumber[i] = generator.nextInt(50) + 1;
			System.out.println(arrayRandomNumber[i]);
		}*/
		
		// Limiting the number of tries to maximum of 3 even though there's 5 random numbers
		for (int x=0; x< 3; x++){
			while(true){
				try {
					// Ask player for his guess.
					System.out.println("Enter an integer:");
					numberGuess = scan.nextInt();
					if (numberGuess >=1 && numberGuess <= 50){
						// exits loops if userInput is within the above range and go to Line 37
						break;
					}
					else{
						System.out.println("*ERROR! Please try again");
					}
				}
				// Tell player that he cannot enter characters, only integers
				catch (InputMismatchException ex) { 
					System.out.println("You can only enter integers");
					scan.nextLine();
					//ex.printStackTrace(); // ignores the Exception
					}
				}
			for (int i=0; i<arrayRandomNumber.length; i++){
				// If guess = random number that was generated, points + 1
				if (numberGuess == arrayRandomNumber[i]){
					numbersMatched += 1;
				}
			}
		}
		//Prints out the total result 
		System.out.println("You scored " + numbersMatched + " points for this round!");
	}
}