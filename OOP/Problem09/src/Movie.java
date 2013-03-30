public class Movie extends Video {
	String director; // name of the director
	String rating; // G, PG, R, or X

	// constructor
	public Movie(String ttl, int lngth, String dir, String rtng) {
		super(ttl, lngth); // use the super class's constructor
		director = dir;
		rating = rtng; // initialize what's new to Movie
	}

}