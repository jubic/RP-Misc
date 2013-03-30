package sg.edu.rp.c345.p04.whatshoulIdo;

import java.util.ArrayList;
import java.util.Collections;

import sg.edu.rp.c345.p04.R;

import android.app.AlertDialog;
import android.app.ListActivity;
import android.content.Context;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.Window;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

public class ToDoListActivity extends ListActivity {
	/** Called when the activity is first created. */
	EditText toDoEditText;
	Button submitButton;
	ListView toDoListView;

	ArrayList<String> toDoTasks;
	ArrayAdapter<String> taskArrayAdapter;

	static final private int SORT_TASKS = Menu.FIRST;
	static final private int REVERSE_SORT_TASKS = Menu.FIRST + 1;
	static final private int REMOVE_TASKS = Menu.FIRST + 2;
	static final private int EDIT_TASKS = Menu.FIRST + 3;

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.main);

		// Get views from layout
		toDoEditText = (EditText) findViewById(R.id.toDoEditText);
		submitButton = (Button) findViewById(R.id.submitButton);
		toDoListView = getListView();
		
		// Define String ArrayList to contain toDoTasks
		toDoTasks = new ArrayList<String>();
		taskArrayAdapter = new ArrayAdapter<String>(this,
				android.R.layout.simple_list_item_1, toDoTasks);

		// Set list view to adapter
		toDoListView.setAdapter(taskArrayAdapter);

		// Define Context Menu to list view
		registerForContextMenu(toDoListView);

		// Add Task
		submitButton.setOnClickListener(new OnClickListener() {
			public void onClick(View v) {
				addTask();
			}
		});
	}

	// Create Options menu
	@Override
	public boolean onCreateOptionsMenu(Menu optionsMenu) {
		super.onCreateOptionsMenu(optionsMenu);
		// Create and add new menu items.
		MenuItem itemSort = optionsMenu.add(0, SORT_TASKS, Menu.NONE,
				R.string.sortAll);
		MenuItem itemReverseSort = optionsMenu.add(0, REVERSE_SORT_TASKS,
				Menu.NONE, R.string.sortReverse);
		MenuItem itemRem = optionsMenu.add(0, REMOVE_TASKS, Menu.NONE,
				R.string.removeAll);
		itemSort.setIcon(R.drawable.sort_btn);
		itemReverseSort.setIcon(R.drawable.reverse_sort_btn);
		itemRem.setIcon(R.drawable.remove_btn);
		return true;
	}

	// Execute option's action based on user click.
	@Override
	public boolean onOptionsItemSelected(MenuItem optionItem) {
		super.onOptionsItemSelected(optionItem);
		switch (optionItem.getItemId()) {
		case (SORT_TASKS): {

			// Sort the items in the ArrayList ascendingly
			Collections.sort(toDoTasks);
			taskArrayAdapter.notifyDataSetChanged();

			return true;
		}
		case (REVERSE_SORT_TASKS): {

			// Sort the items in the ArrayList descendingly
			Collections.reverse(toDoTasks);
			taskArrayAdapter.notifyDataSetChanged();

			return true;
		}
		case (REMOVE_TASKS): {

			// Delete all tasks
			toDoTasks.clear();
			taskArrayAdapter.notifyDataSetChanged();
			Context context = getApplicationContext();
			CharSequence text = "All tasks have been removed";
			int duration = Toast.LENGTH_SHORT;
			Toast toast = Toast.makeText(context, text, duration);
			toast.show();

			return true;
		}
		}
		return false;
	}

	// Create Context Menu
	@Override
	public void onCreateContextMenu(ContextMenu menu, View v,
			ContextMenu.ContextMenuInfo menuInfo) {
		super.onCreateContextMenu(menu, v, menuInfo);
		menu.setHeaderTitle("Choose your action");
		menu.add(0, REMOVE_TASKS, Menu.NONE, R.string.removeItem);
		menu.add(0, EDIT_TASKS, Menu.NONE, R.string.editItem);
	}

	// Execute Context Item Action based on user long-click.
	@Override
	public boolean onContextItemSelected(MenuItem item) {
		super.onContextItemSelected(item);
		switch (item.getItemId()) {
		case (REMOVE_TASKS): {
			// Remove the task that user long-clicked
			AdapterView.AdapterContextMenuInfo menuInfo;
			menuInfo = (AdapterView.AdapterContextMenuInfo) item.getMenuInfo();
			final int removeIndex = menuInfo.position;
			toDoTasks.remove(removeIndex);
			Context context = getApplicationContext();
			CharSequence text = "Task has been removed";
			int duration = Toast.LENGTH_SHORT;
			Toast toast = Toast.makeText(context, text, duration);
			toast.show();
			taskArrayAdapter.notifyDataSetChanged();
			return true;
		}
		case (EDIT_TASKS): {
			// Edit the task that user long-clicked
			AdapterView.AdapterContextMenuInfo menuInfo;
			menuInfo = (AdapterView.AdapterContextMenuInfo) item.getMenuInfo();
			final int editIndex = menuInfo.position;
			String editText = toDoTasks.get(editIndex);

			AlertDialog.Builder alert = new AlertDialog.Builder(this);

			alert.setTitle("Edit Task");

			// Set an EditText view to get user input
			final EditText editInput = new EditText(this);
			alert.setView(editInput);
			editInput.setText(editText);

			alert.setPositiveButton("Edit",
					new DialogInterface.OnClickListener() {
						public void onClick(DialogInterface dialog,
								int whichButton) {
							String editTask = editInput.getText().toString();
							// Do something with value!
							toDoTasks.set(editIndex, editTask);
							Context context = getApplicationContext();
							CharSequence text = "Task has been edited";
							int duration = Toast.LENGTH_SHORT;
							Toast toast = Toast.makeText(context, text,
									duration);
							toast.show();
							taskArrayAdapter.notifyDataSetChanged();
						}
					});

			alert.setNegativeButton("Cancel",
					new DialogInterface.OnClickListener() {
						public void onClick(DialogInterface dialog,
								int whichButton) {
							// Canceled.
						}
					});

			alert.show();
		}
		}
		return false;
	}

	// Function for adding tasks
	public void addTask() {
		if (toDoEditText.getText().toString().length() == 0) {
			Context context = getApplicationContext();
			CharSequence text = "Field is empty";
			int duration = Toast.LENGTH_SHORT;
			Toast toast = Toast.makeText(context, text, duration);
			toast.show();
			return;
		}
		String task = toDoEditText.getText().toString();
		toDoTasks.add(task);
		taskArrayAdapter.notifyDataSetChanged();
		toDoEditText.setText("");
		Context context = getApplicationContext();
		CharSequence text = "Task has been added";
		int duration = Toast.LENGTH_SHORT;
		Toast toast = Toast.makeText(context, text, duration);
		toast.show();
	}
}