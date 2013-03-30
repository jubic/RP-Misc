package sg.edu.rp.c345.p09.whatshoulIdoII;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;

import android.app.AlertDialog;
import android.app.ListActivity;
import android.content.DialogInterface;
import android.database.Cursor;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.View.OnKeyListener;
import android.widget.AdapterView;
// import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

public class toDoList extends ListActivity {

	// Constants for context menu
	static final private int SORT_TASKS = Menu.FIRST;
	static final private int REMOVE_TASKS = Menu.FIRST + 1;
	static final private int EDIT_TASKS = Menu.FIRST + 2;
	static final private int FILTER_TASKS = Menu.FIRST + 3;

	// Declarations related to list
	ArrayList<TaskItem> tasks = new ArrayList<TaskItem>();
	TaskAdapter taskAdapter;

	// Database Adapter
	DbAdapter mDbAdapter;

	// Views
	Button btnNewItem;
	TextView tbNewItem;

	// Keep track of which item we are modifying/filtering
	int indexModifying = -1;
	String taskNameFilter = "";

	/** Called when the activity is first created. */
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		// Get Views
		ListView listView = getListView();
		btnNewItem = (Button) findViewById(R.id.btnNewItem);
		tbNewItem = (EditText) findViewById(R.id.tbNewItem);

		// Create DbAdapter
		mDbAdapter = new DbAdapter(this);

		// Get database tasks
		getTasks();

		// Instantiate ArrayAdapter and bind to ListView
		// tasksAdapter = new ArrayAdapter<Task>(this,
		// android.R.layout.simple_list_item_1, tasks);
		taskAdapter = new TaskAdapter(this, tasks);
		listView.setAdapter(taskAdapter);

		// Enabled context menu for ListView
		registerForContextMenu(listView);

		// Assign listener for new task Button & EditText
		btnNewItem.setOnClickListener(saveItemClick);
		tbNewItem.setOnKeyListener(saveItemKey);

	}

	// Separate the button methods out... save space
	private OnClickListener saveItemClick = new OnClickListener() {
		public void onClick(View v) {

			// Get EditText & Read the value inside
			String newTaskName = tbNewItem.getText().toString();

			// Don't proceed if EditText is empty
			if (newTaskName.compareTo("") == 0)
				return;

			// DbAdapter Open

			if (btnNewItem.getText() == getResources().getText(
					R.string.new_item_btn)) {
				addTask(new TaskItem(newTaskName));
			} else {

				// Modify the item based on remembered position
				updateTask(indexModifying, newTaskName);

				// Reset views
				btnNewItem.setText(R.string.new_item_btn);
			}

			tbNewItem.setText("");
			// Notify ListView that data has changed
			taskAdapter.notifyDataSetChanged();
		}
	};
	private OnKeyListener saveItemKey = new OnKeyListener() {
		public boolean onKey(View v, int keyCode, KeyEvent event) {
			if (event.getAction() == KeyEvent.ACTION_DOWN
					&& (keyCode == KeyEvent.KEYCODE_DPAD_CENTER || keyCode == KeyEvent.KEYCODE_ENTER)) {
				saveItemClick.onClick(v);
				return true;
			} else {
				return false;
			}
		}
	};

	// Create options menu (triggered by Menu key)
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		super.onCreateOptionsMenu(menu);

		// Create and add new menu items.
		MenuItem itemSort = menu.add(0, SORT_TASKS, Menu.NONE,
				R.string.sort_all);
		MenuItem itemRem = menu.add(0, REMOVE_TASKS, Menu.NONE,
				R.string.remove_all);
		MenuItem itemFilter = menu.add(0, FILTER_TASKS, Menu.NONE,
				R.string.filter);
		itemSort.setIcon(R.drawable.sort_btn);
		itemRem.setIcon(R.drawable.remove_btn);
		itemFilter.setIcon(android.R.drawable.ic_menu_search);
		return true;
	}

	// Handle options menu
	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		super.onOptionsItemSelected(item);
		switch (item.getItemId()) {
		case (SORT_TASKS):
			// Sort todoTasks
			Collections.sort(tasks);
			taskAdapter.notifyDataSetChanged();
			break;
		case (REMOVE_TASKS):
			// Clear todoTasks
			removeAllTasks();
			taskAdapter.notifyDataSetChanged();
			break;
		case (FILTER_TASKS):
			filterTasks();
			taskAdapter.notifyDataSetChanged();
		}

		// Prevent bug: Update to reflect "Add" if the original item was cleared
		// Get Add button
		btnNewItem.setText(R.string.new_item_btn);

		return true;
	}

	// Create context menu (press and hold)
	@Override
	public void onCreateContextMenu(ContextMenu menu, View v,
			ContextMenu.ContextMenuInfo menuInfo) {
		super.onCreateContextMenu(menu, v, menuInfo);
		menu.setHeaderTitle("Actions");
		menu.add(0, EDIT_TASKS, Menu.NONE, R.string.edit_item);
		menu.add(0, REMOVE_TASKS, Menu.NONE, R.string.remove_item);
	}

	// Handle context menu
	@Override
	public boolean onContextItemSelected(MenuItem item) {
		super.onContextItemSelected(item);

		// Get selected index
		AdapterView.AdapterContextMenuInfo menuInfo;
		menuInfo = (AdapterView.AdapterContextMenuInfo) item.getMenuInfo();
		int index = menuInfo.position;

		switch (item.getItemId()) {
		case (EDIT_TASKS):
			// Get EditText
			tbNewItem.setText(tasks.get(index).getName());

			// Get Button
			btnNewItem.setText(R.string.edit_item_btn);

			// Remember editing position
			indexModifying = index;
			return true;

		case (REMOVE_TASKS):
			// Perform the necessary actions to remove the selected tasks in
			removeTask(index);
			taskAdapter.notifyDataSetChanged();
			return true;
		}

		return false;
	}

	private void getTasks() {
		ArrayList<TaskItem> newTasks = new ArrayList<TaskItem>();
		mDbAdapter.open();

		Cursor c;
		if (taskNameFilter.length() > 0) {
			c = mDbAdapter.getAllTasksSearchName(taskNameFilter);
		} else {
			c = mDbAdapter.getAllTasks();
		}

		if (c.moveToFirst()) {
			do {
				int columnId = c.getColumnIndex(DbAdapter.KEY_TASK_ID);
				int columnName = c.getColumnIndex(DbAdapter.KEY_TASK_NAME);
				int columnDateCreated = c
						.getColumnIndex(DbAdapter.KEY_TASK_TIMESTAMP);

				// Get data, create Task, add to tasks
				int id = c.getInt(columnId);
				String name = c.getString(columnName);
				Date date = new Date(c.getLong(columnDateCreated));
				newTasks.add(new TaskItem(id, name, date));
			} while (c.moveToNext());
		}
		c.close();
		mDbAdapter.close();
		tasks.clear();
		tasks.addAll(newTasks);
	}

	private void addTask(TaskItem task) {
		tasks.add(task);
		mDbAdapter.open();
		long id = mDbAdapter.insertTask(task.getName(),
				Long.toString(task.getDateCreated().getTime()));
		task.setId(id);
		mDbAdapter.close();
	}

	private void updateTask(int location, String newName) {
		TaskItem task = tasks.get(location);
		task.setName(newName);
		mDbAdapter.open();
		mDbAdapter.updateTask(task.getId(), task.getName(),
				Long.toString(task.getDateCreated().getTime()));
		mDbAdapter.close();
	}

	private void removeTask(int location) {
		mDbAdapter.open();
		mDbAdapter.removeTask(tasks.get(location).getName());
		mDbAdapter.close();
		tasks.remove(location);
	}

	private void removeAllTasks() {
		mDbAdapter.open();
		mDbAdapter.removeAllTasks();
		mDbAdapter.close();
		tasks.clear();
	}

	private void filterTasks() {
		AlertDialog.Builder alert = new AlertDialog.Builder(this);
		alert.setTitle(R.string.filter);
		alert.setMessage("Enter the text to search for:");

		// Set an EditText view to get user input
		final EditText input = new EditText(this);
		input.setSingleLine();
		input.setText(taskNameFilter);
		alert.setView(input);

		alert.setPositiveButton("Ok", new DialogInterface.OnClickListener() {
			public void onClick(DialogInterface dialog, int whichButton) {
				taskNameFilter = input.getText().toString();
				getTasks();
				taskAdapter.notifyDataSetChanged();
			}
		});

		alert.setNegativeButton("Cancel",
				new DialogInterface.OnClickListener() {
					public void onClick(DialogInterface dialog, int whichButton) {
						dialog.cancel();
					}
				});

		alert.show();
	}

}