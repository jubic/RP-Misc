import java.util.Scanner;

public class MovieMenuMain {
	public static void main(String[] args) {
		int rentChoice = 0;
		double earnings = 0;
		Scanner scan = new Scanner(System.in);

		Movies movie1 = new Movies("Forrest Gump                ", 4);
		Movies movie2 = new Movies("The Sting                   ", 3);
		Movies movie3 = new Movies("Star Wars                   ", 5);
		Movies movie4 = new Movies("LOTR: The Return of the King", 12);
		Movies movie5 = new Movies("Raiders of the Lost Ark     ", 3);
		Movies movie6 = new Movies("The Matrix                  ", 7);
		Movies[] movieList = { movie1, movie2, movie3, movie4, movie5, movie6 };

		while (true) {
			// Current Earnings
			for (int i = 0; i < movieList.length; i++) {
				earnings += movieList[i].currentEarnings(movieList[i].rentCount);
			}
			System.out.println("Current Earnings = $" + earnings);
			earnings = 0;

			// Print info
			for (int i = 0; i < movieList.length; i++) {
				System.out.println("\tMovie ID: " + (i + 1) + "\tTitle: " + movieList[i].title + "\tRent Count: " + movieList[i].rentCount);
			}
			
			// Rent count update
			scan = new Scanner(System.in);
			System.out.println("Please enter MovieID to rent: ");
			rentChoice = scan.nextInt();
			movieList[rentChoice - 1].updateCount();
		}
	}
}