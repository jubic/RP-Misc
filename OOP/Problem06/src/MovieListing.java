public class MovieListing {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Movie movie1 = new Movie();
		movie1.title = "Forrest Gump";
		movie1.year = 1994;
		movie1.gross = 679.4;
		movie1.oscar = 6;

		Movie movie2 = new Movie();
		movie2.title = "The Sting";
		movie2.year = 1973;
		movie2.gross = 159.6;
		movie2.oscar = 7;

		Movie movie3 = new Movie();
		movie3.title = "Star Wars";
		movie3.year = 1977;
		movie3.gross = 797.9;
		movie3.oscar = 6;

		Movie movie4 = new Movie();
		movie4.title = "LOTR: The Return of the King";
		movie4.year = 2003;
		movie4.gross = 1133;
		movie4.oscar = 11;

		Movie movie5 = new Movie();
		movie5.title = "Raiders of the Lost Ark";
		movie5.year = 1981;
		movie5.gross = 386.8;
		movie5.oscar = 4;

		Movie movie6 = new Movie();
		movie6.title = "The Matrix";
		movie6.year = 1999;
		movie6.gross = 460.3;
		movie6.oscar = 4;

		// put all the movie objects into an array
		Movie[] movieList = { movie1, movie2, movie3, movie4, movie5, movie6 };

		// Part 1: Average Gross of all movies
		double totalGross = 0.0;

		for (int i = 0; i < movieList.length; i++) {
			totalGross = totalGross + movieList[i].gross;
		}
		double averageGross = totalGross / movieList.length;

		System.out.println("Average Gross of all movies = \t\t$" + averageGross
				+ " million\n");

		// Part 2: Movie with >$750 million gross
		for (int i = 0; i < movieList.length; i++) {
			if (movieList[i].gross > 750) {
				System.out.println("Movie exceeding $750 million gross = \t"
						+ movieList[i].title);
			}
		}

		// Part 3: Most Oscar win
		int mostOscar = 0;
		int mostOscarIndex = 0;

		for (int i = 0; i < movieList.length; i++) {
			if (movieList[i].oscar > mostOscar) {
				mostOscar = movieList[i].oscar;
				mostOscarIndex = i;
			}
		}
		System.out.println("\nMovie with most Oscar won = \t\t'"
				+ movieList[mostOscarIndex].title + "' with "
				+ movieList[mostOscarIndex].oscar + " Oscars!");
	}
}
