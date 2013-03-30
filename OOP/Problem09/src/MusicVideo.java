public class MusicVideo extends Video {
	String artist;
	String category;

	// constructor
	public MusicVideo(String ttl, int len, String art, String cat) {
		super(ttl, len);
		artist = art;
		category = cat;
	}

	public void show() {
		super.show();
		System.out.println("artist:" + artist + " style: " + category);
	}
}