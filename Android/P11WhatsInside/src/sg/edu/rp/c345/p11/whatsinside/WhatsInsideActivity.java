package sg.edu.rp.c345.p11.whatsinside;

import android.app.Activity;
import android.content.ContentResolver;
import android.database.Cursor;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;

public class WhatsInsideActivity extends Activity {

	ContentResolver audioResolver, imageResolver;
	int audioCount, imageCount, videoCount;
	String audioTitle, audioArtist, audioSize, imageTitle, imageDate,
			imageSize, videoTitle, videoDate, videoSize;

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);
		loadMediaInfo();
	}

	public void loadMediaInfo() {
		/*
		 * Do a query of the Content Resolver, where you query from the
		 * EXTERNAL_CONTENT (external storage), to get the AUDIO content. In
		 * this example, you will be extracting the TITLE of the AUDIO Content.
		 * The FILE SIZE and other information about the AUDIO file are
		 * available in AudioColumns.
		 */
		ContentResolver audioResolver = getBaseContext().getContentResolver();
		ContentResolver imageResolver = getBaseContext().getContentResolver();
		ContentResolver videoResolver = getBaseContext().getContentResolver();

		// Query files in ContentProvider
		Cursor audioCursor = audioResolver.query(
				MediaStore.Audio.Media.EXTERNAL_CONTENT_URI, new String[] {
						MediaStore.Audio.AudioColumns.TITLE,
						MediaStore.Audio.AudioColumns.ARTIST,
						MediaStore.Audio.AudioColumns.SIZE }, null, null, null);
		Cursor imageCursor = imageResolver
				.query(MediaStore.Images.Media.EXTERNAL_CONTENT_URI,
						new String[] { MediaStore.Images.ImageColumns.TITLE,
								MediaStore.Images.ImageColumns.DATE_TAKEN,
								MediaStore.Images.ImageColumns.SIZE }, null,
						null, null);
		Cursor videoCursor = videoResolver.query(
				MediaStore.Video.Media.EXTERNAL_CONTENT_URI, new String[] {
						MediaStore.Video.VideoColumns.TITLE,
						MediaStore.Video.VideoColumns.DATE_TAKEN,
						MediaStore.Video.VideoColumns.SIZE }, null, null, null);

		// Gets the number of rows returned in the query
		audioCount = audioCursor.getCount();
		imageCount = imageCursor.getCount();
		videoCount = videoCursor.getCount();

		if (audioCursor.moveToFirst()) {
			audioTitle = "";
			audioArtist = "";
			audioSize = "";
			do {
				// Check your DDMS whether the Song Title is being logged in Log
				// Cat.
				audioTitle = audioCursor.getString(0);
				audioArtist = audioCursor.getString(1);
				audioSize = audioCursor.getString(2);
				Log.d("Song Title", audioTitle);
				Log.d("Song Artist", audioArtist);
				Log.d("Song Size", audioSize);
			} while (audioCursor.moveToNext());
		}

		// Close the cursor once action completed
		audioCursor.close();

		if (imageCursor.moveToFirst()) {
			imageTitle = "";
			imageDate = "";
			imageSize = "";
			do {
				// Check your DDMS whether the Song Title is being logged in Log
				// Cat.
				imageTitle = imageCursor.getString(0);
				imageDate = imageCursor.getString(1);
				imageSize = imageCursor.getString(2);
				Log.d("Image Title", imageTitle);
				Log.d("Image Date", imageDate);
				Log.d("Image Size", imageSize);
			} while (imageCursor.moveToNext());
		}

		// Close the cursor once action completed
		imageCursor.close();
		
		if (videoCursor.moveToFirst()) {
			videoTitle = "";
			videoDate = "";
			videoSize = "";
			do {
				// Check your DDMS whether the Song Title is being logged in Log
				// Cat.
				videoTitle = videoCursor.getString(0);
				videoDate = videoCursor.getString(1);
				videoSize = videoCursor.getString(2);
				Log.d("Video Title", videoTitle);
				Log.d("Video Date", videoDate);
				Log.d("Video Size", videoSize);
			} while (videoCursor.moveToNext());
		}

		// Close the cursor once action completed
		videoCursor.close();
	}
}