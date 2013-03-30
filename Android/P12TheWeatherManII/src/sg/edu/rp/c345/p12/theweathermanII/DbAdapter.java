package sg.edu.rp.c345.p12.theweathermanII;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.SQLException;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.database.sqlite.SQLiteDatabase.CursorFactory;
import android.util.Log;

public class DbAdapter {

	// Database properties
	private static final String DATABASE_NAME = "weatherman.db";
	private static final String DATABASE_TABLE_NAME = "cities";
	private static final int DATABASE_VERSION = 1;
	
	public static final String KEY_CITY_ID = "_id";
	public static final String KEY_CITY_NAME = "cityname";
	public static final String KEY_CITY_TIMESTAMP = "timestamp";

	// Create script
	private static final String DATABASE_CREATE_FAV = "create table "
			+ DATABASE_TABLE_NAME + " (" + KEY_CITY_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
			+ KEY_CITY_NAME + " text not null" + ");";  
	
	private SQLiteDatabase db;
	private final Context context;
	private MyDbHelper myDbHelper;
	
	// constructor create the wrapper to open and close the db
	public DbAdapter(Context _context) {
		context = _context;
		myDbHelper = new MyDbHelper(context, DATABASE_NAME, null,
				DATABASE_VERSION);
	}

	public DbAdapter open() throws SQLException {
		db = myDbHelper.getWritableDatabase();
		return this;
	}

	public void close() {
		db.close();
	}
	
	//Insert new entry to the database or update if the task exist in the database

	public long insertCity(String _name) {
		Cursor c = db.query(DATABASE_TABLE_NAME, new String[] { KEY_CITY_ID,
				KEY_CITY_NAME}, KEY_CITY_NAME + "=\""
				+ _name + "\"", null, null, null, null);

		int count = c.getCount();
		Log.d("CityList Size", Integer.toString(count));
		if (count > 0) {
			c.moveToFirst();
			int idColumn = c.getColumnIndex(KEY_CITY_ID);
			long id = c.getLong(idColumn);
			c.close();
			return updateCity(id, _name);
		} else {
			c.close();
			ContentValues contentValues = new ContentValues();
			contentValues.put(KEY_CITY_NAME, _name);
			
			Long test = db.insert(DATABASE_TABLE_NAME, null, contentValues);

			return test;
		}
	}

	//remove entry from the database based on the task name
	public boolean removeCity(String _name) {
		return db.delete(DATABASE_TABLE_NAME, KEY_CITY_NAME + "='" + _name+"'", null) > 0;
	}

	//retrieve all the entries in the database
	public Cursor getAllCities() {
		return db.query(DATABASE_TABLE_NAME, new String[] { KEY_CITY_ID,
				KEY_CITY_NAME}, null, null, null,
				null, null);
	}

	public int updateCity(long _id, String _name) {
		ContentValues contentValues = new ContentValues();
		contentValues.put(KEY_CITY_NAME, _name);
		
		return db.update(DATABASE_TABLE_NAME, contentValues, KEY_CITY_ID
				+ "=" + _id, null);
	}

	public boolean removeAllCities() {
		return db.delete(DATABASE_TABLE_NAME, null, null) > 0;
	}
	
	private static class MyDbHelper extends SQLiteOpenHelper {

		public MyDbHelper(Context context, String name, CursorFactory factory,
				int version) {
			super(context, name, factory, version);
		}

		@Override
		// Only gets called if the database does not exist on the phone
		public void onCreate(SQLiteDatabase _db) {
			_db.execSQL(DATABASE_CREATE_FAV);

		}

		public void onUpgrade(SQLiteDatabase _db, int _oldVersion,
				int _newVersion) {
			// Drop old one
			_db.execSQL("DROP TABLE IF EXISTS " + DATABASE_CREATE_FAV);
			// Create new one
			onCreate(_db);
		}
	}
}
