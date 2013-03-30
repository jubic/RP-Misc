package sg.edu.rp.c345.p09.whatshoulIdoII;

import java.util.List;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public class TaskAdapter extends BaseAdapter {
	
	private List<TaskItem> tasks;
	private LayoutInflater layoutInflater;
	
	public TaskAdapter(Context context, List<TaskItem> tasks) {
		layoutInflater = LayoutInflater.from(context);		
		this.tasks = tasks;
	}
	
	public int getCount() {
		return tasks.size();
	}

	public Object getItem(int position) {
		return position;
	}

	public long getItemId(int position) {
		return position;
	}
	
	static class ViewHolder {
		TextView name;
		TextView date;
	}

	public View getView(int position, View convertView, ViewGroup parent) {
		// A ViewHolder keeps references to children views to avoid unneccessary calls
		// to findViewById() on each row.
		ViewHolder holder;

		// When convertView is not null, we can reuse it directly, there is no need
		// to reinflate it. We only inflate a new View when the convertView supplied
		// by ListView is null.
		if (convertView == null) {
			convertView = layoutInflater.inflate(R.layout.taskitem, null);

			// Creates a ViewHolder and store references to the two children views
			// we want to bind data to.
			holder = new ViewHolder();
			holder.name = (TextView) convertView.findViewById(R.id.taskName);
			holder.date = (TextView) convertView.findViewById(R.id.taskDate);
			convertView.setTag(holder);
		
		} else {
			// Get the ViewHolder back to get fast access to the TextView
			// and the ImageView.
			holder = (ViewHolder) convertView.getTag();
		}

		// Bind the data efficiently with the holder.
		TaskItem task = tasks.get(position);
		holder.name.setText(task.getName());
		holder.date.setText(task.getDateCreated().toString());
		
		return convertView;
	}

}
