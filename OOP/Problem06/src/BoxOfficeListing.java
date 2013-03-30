import java.util.Scanner;

public class BoxOfficeListing {
	public static void main(String[] args) {
		//Scanner for inputing data
		Scanner userInput = new Scanner(System.in);

	int counter = 0;
	int counter2 = 0;
	int choice = 0;
	double totalSales = 0;
	double totalSales2 = 0;
	String title = null;
	int year = 0;
	double sales = 0;
	int oscars = 0;
	
	//Create Array for the Movies
	BoxOffice[] movieArray = new BoxOffice[99999];
		
	for (int i = 0; i <movieArray.length; i++){
		movieArray[i] = new BoxOffice();
	}
	
	//Inserting elements into the empty attributes
	movieArray[0].title = "Forrest Gump";
	movieArray[0].year = 1994;
	movieArray[0].sales = 679.4;
	movieArray[0].oscars = 6;
	
	movieArray[1].title = "The Sting";
	movieArray[1].year = 1973;
	movieArray[1].sales = 159.6;
	movieArray[1].oscars = 7;
	
	movieArray[2].title = "Star Wars";
	movieArray[2].year = 1977;
	movieArray[2].sales = 797.9;
	movieArray[2].oscars = 6;
	
	movieArray[3].title = "LOTR: The Return of the King";
	movieArray[3].year = 2003;
	movieArray[3].sales = 1133.0;
	movieArray[3].oscars = 11;
	
	movieArray[4].title = "Raiders of the Lost Ark";
	movieArray[4].year = 1981;
	movieArray[4].sales = 368.8;
	movieArray[4].oscars = 4;
	
	System.out.println("=================================================");
	System.out.println("|.-.   .-.      .-.                             |");                             
	System.out.println("|: :.-.: :      : :                             |");                             
	System.out.println("|: :: :: : .--. : :   .--.  .--. ,-.,-.,-. .--. |"); 
	System.out.println("|: `' `' ;' '_.': :_ '  ..'' .; :: ,. ,. :' '_.'|");
	System.out.println("| `.,`.,' `.__.'`.__;`.__.'`.__.':_;:_;:_;`.__.'|");
	System.out.println("=================================================");
	System.out.println("");
	
	while (choice != 9) {
		//Ask user to select an option. 1/2/9.
		System.out.println("=================================================================");
			System.out.println("Please select as follow:");
			System.out.println("\t1 - Print A Report");
			System.out.println("\t2 - Add New Movie");
			System.out.println("\t9 - To exit the system");
			
			System.out.print("Please enter your choice : ");
			choice = userInput.nextInt();
			System.out.println("=================================================================");
			System.out.println("");
			
			if (choice == 1) {
				// if option 1 is chosen, present all information
				// Adding totalSales for movies
				for (int i = 0; i < movieArray.length; i++){
					totalSales = totalSales + movieArray[i].sales;
					// Adding totalSales for movies > 750million
					if (movieArray[i].sales >= 750){
						totalSales2 = totalSales2 + movieArray[i].sales;
						counter2 = counter2 + 1;
					}
					// Checking how many sales are there
					if (movieArray[i].sales != 0){
						counter = counter + 1;
					}
				}
				
				System.out.println("=====================================");
				System.out.println("                                _");
				System.out.println(".----.-----.-----.-----.----. _| |_"); 
				System.out.println("|   _|  -__|  _  |  _  |   _||_   _|");
				System.out.println("|__| |_____|   __|_____|__|    |_|");
		        System.out.println("           |__|                    ");                    
				System.out.println("=====================================");
				System.out.println("");
	
				// Finding avgSales
				double avgSales = totalSales /counter;
				// Finding avgSales2 for sales >750 million
				double avgSales2 = totalSales2/ counter2;
				System.out.println("=================================================================");
				System.out.println("Average worldwide sale for all the box office movies :");
				System.out.println(" $" + avgSales + " million");
				System.out.println("=================================================================");
				System.out.println("");
				System.out.println("=================================================================");
				System.out.println("Average sales for movies that sold more than $750 million :");
				System.out.println(" $" + avgSales2 + " million");
				System.out.println("=================================================================");
				System.out.println("");
				System.out.println("=================================================================");
				System.out.println("Movies sales sold more than $750 million");
				System.out.println("=================================================================");
				
				// Checking which movie > 750 million and print the title
				for (int i =0; i <movieArray.length; i++){
					if (movieArray[i].sales > 750.0){
						System.out.println("Movie Title: " + movieArray[i].title + " with $" + movieArray[i].sales + " million of sales");
					}
				}
	
				int mostOscars = -9999;
				int leastOscars = 9999;
				
				System.out.println("");
				System.out.println("=================================================================");
				System.out.println("Movies movie with the most Oscar won");
				System.out.println("=================================================================");
				
				// Find the movie(s) that has the most awards
				for (int i = 0; i < movieArray.length; i++){
					if(movieArray[i].oscars != 0){
						if (movieArray[i].oscars > mostOscars){
						mostOscars = movieArray[i].oscars;
					}
				}
			}

				for (int i = 0; i <movieArray.length; i++){
					if (movieArray[i].oscars == mostOscars){
						System.out.println("Movie Title: " + movieArray[i].title + " with " + movieArray[i].oscars + " Oscar awards");
					}
				}
				
				System.out.println("");
				System.out.println("=================================================================");
				System.out.println("Movies movie with the least Oscar won");
				System.out.println("=================================================================");
				
				// Find the movie(s) that has the least awards
				for (int i = 0; i < movieArray.length; i++){
					if (movieArray[i].oscars != 0){
						if (movieArray[i].oscars < leastOscars){
							leastOscars = movieArray[i].oscars;
						}
					}
				}
				
				for (int i = 0; i <movieArray.length; i++){
					if (movieArray[i].oscars == leastOscars){
							System.out.println("Movie Title: " + movieArray[i].title + " with " + movieArray[i].oscars + " Oscar awards");
					}
				}
				System.out.println("");
			}
			
			else if (choice == 2) {
				//If option 2 is chosen, add a movie
				System.out.println("Please enter the Movie's Title: ");
				title = userInput.nextLine();
				
				System.out.println("Please enter the Movie Release Year: ");
				year = userInput.nextInt();
				
				System.out.println("Please enter the Movie Worldwide Sales (million): ");
				sales = userInput.nextDouble();
				
				System.out.println("Please enter the number of times the movie won in Oscar: ");
				oscars = userInput.nextInt();
				
				// If a slot in the array is empty, fill it with the above attributes
				for (int i = 0; i < movieArray.length;i++){
					if (movieArray[i].title == null) {
						movieArray[i].title = title;
						movieArray[i].year = year;
						movieArray[i].sales = sales;
						movieArray[i].oscars = oscars;
						
						System.out.println("===========================================");
						System.out.println("This movie has been added successfully!");
						System.out.println("===========================================");
						System.out.println("Movie's Title: " + movieArray[i].title);
						System.out.println("Movie Released Year: " + movieArray[i].year);
						System.out.println("Movie Worldwide Sales (million): " + movieArray[i].sales);
						System.out.println("Number of times the movie won in Oscar: " + movieArray[i].oscars);
						System.out.println("");
						break;
					}	
				}
			}
			
			else if (choice == 9) { 
				// Option 'Exit' actions here
				System.out.println("You're now exiting the Box Office System");
				System.out.println("Good Bye!");
				System.out.println("Hope to see you again!");
				break;
			}
			
			else {
				// Unknown option
				System.out.println("Unknown option, please choose again.");
			}
		}	
	}
}