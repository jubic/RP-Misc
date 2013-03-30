package sg.edu.rp.c345.p11.whatsinside;

import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.ComponentName;
import android.content.ContentResolver;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.provider.MediaStore;
import android.util.Log;
import android.widget.RemoteViews;

public class WidgetProvider extends AppWidgetProvider {
	// Declarations
	ContentResolver audioResolver, imageResolver;
	int audioCount, imageCount, videoCount;
	String audioTitle, audioArtist, imageTitle, imageDate, videoTitle,
			videoDate;
	int audioSize, imageSize, videoSize, totalImageSize, totalAudioSize,
			totalVideoSize;

	@Override
	public void onEnabled(Context context) {
		// TODO Auto-generated method stub
		audioTitle = "";
		audioArtist = "";
		audioSize = 0;
		imageTitle = "";
		imageDate = "";
		imageSize = 0;
		videoTitle = "";
		videoDate = "";
		videoSize = 0;
		totalImageSize = 0;
		totalAudioSize = 0;
		totalVideoSize = 0;

		super.onEnabled(context);
	}

	@Override
	public void onUpdate(Context context, AppWidgetManager appWidgetManager,
			int[] appWidgetIds) {
		final int N = appWidgetIds.length;

		// Perform this loop procedure for each App Widget that
		// belongs to this provider
		for (int i = 0; i < N; i++) {

			int appWidgetId = appWidgetIds[i];
			Log.d("WidgetID", String.valueOf(appWidgetId));
			RemoteViews view = new RemoteViews(context.getPackageName(),
					R.layout.widgetlayout);
			view.setTextViewText(R.id.tvCounter, "Total no. of images: "
					+ imageCount + "\nTotal size of images: " + totalImageSize
					+ " bytes" + "\nTotal no. of audio: " + audioCount
					+ "\nTotal size of audio: " + totalAudioSize + " bytes"
					+ "\nTotal no. of video: " + videoCount
					+ "\nTotal size of video: " + totalVideoSize + " bytes");

			appWidgetManager.updateAppWidget(appWidgetId, view);
		}

		super.onUpdate(context, appWidgetManager, appWidgetIds);
	}

	@Override
	public void onReceive(Context context, Intent intent) {
		Log.d("RECEIVER", intent.getAction());

		AppWidgetManager appWidgetManager = AppWidgetManager
				.getInstance(context);
		ComponentName thisAppWidget = new ComponentName(
				context.getPackageName(), WidgetProvider.class.getName());
		int[] appWidgetIds = appWidgetManager.getAppWidgetIds(thisAppWidget);
		loadMediaInfo(context);
		onUpdate(context, appWidgetManager, appWidgetIds);

		super.onReceive(context, intent);

	}

	public void loadMediaInfo(Context context) {
		/*
		 * Do a query of the Content Resolver, where you query from the
		 * EXTERNAL_CONTENT (external storage), to get the AUDIO content. In
		 * this example, you will be extracting the TITLE of the AUDIO Content.
		 * The FILE SIZE and other information about the AUDIO file are
		 * available in AudioColumns.
		 */
		ContentResolver audioResolver = context.getContentResolver();
		ContentResolver imageResolver = context.getContentResolver();
		ContentResolver videoResolver = context.getContentResolver();

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
			do {
				// Check your DDMS whether the Song Title is being logged in Log
				// Cat.
				audioTitle = audioCursor.getString(0);
				audioArtist = audioCursor.getString(1);
				audioSize = audioCursor.getInt(2);
				totalAudioSize += audioSize;
				Log.d("Song Title", audioTitle);
				Log.d("Song Artist", audioArtist);
				Log.d("Song Size", Integer.toString(audioSize));
				Log.d("Total Song Size", Integer.toString(totalAudioSize));
			} while (audioCursor.moveToNext());
		}

		// Close the cursor once action completed
		audioCursor.close();

		if (imageCursor.moveToFirst()) {
			do {
				// Check your DDMS whether the Song Title is being logged in Log
				// Cat.
				imageTitle = imageCursor.getString(0);
				imageDate = imageCursor.getString(1);
				imageSize = imageCursor.getInt(2);
				totalImageSize += imageSize;
				Log.d("Image Title", imageTitle);
				Log.d("Image Date", imageDate);
				Log.d("Image Size", Integer.toString(imageSize));
				Log.d("Total Image Size", Integer.toString(totalImageSize));
			} while (imageCursor.moveToNext());
		}

		// Close the cursor once action completed
		imageCursor.close();
		
		if (videoCursor.moveToFirst()) {
			do {
				// Check your DDMS whether the Song Title is being logged in Log
				// Cat.
				videoTitle = videoCursor.getString(0);
				videoDate = videoCursor.getString(1);
				videoSize = videoCursor.getInt(2);
				totalVideoSize += videoSize;
				Log.d("Video Title", videoTitle);
				Log.d("Video Date", videoDate);
				Log.d("Video Size", Integer.toString(videoSize));
				Log.d("Total Video Size", Integer.toString(totalVideoSize));
			} while (videoCursor.moveToNext());
		}

		// Close the cursor once action completed
		videoCursor.close();
	}
}
