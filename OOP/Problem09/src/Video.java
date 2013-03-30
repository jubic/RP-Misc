public class Video {
	String title; // name of the item
	int length; // number of minutes
	boolean avail; // is the video in the store?

	// constructor
	public Video(String ttl, int lngth) {
		title = ttl;
		length = lngth;
		avail = true;
	}

	public void show() {
		System.out.println(title + ", " + length + " min. available:" + avail);
	}
}
