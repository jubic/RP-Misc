package sg.edu.rp.c345.p09.whatshoulIdoII;
 
import java.util.Date;

public class TaskItem implements Comparable<TaskItem> {

	private long id;
	private String name;
	private Date dateCreated;

	public TaskItem(String name) {
		this.name = name;
		this.dateCreated = new Date(System.currentTimeMillis());
	}
	public TaskItem(String name, Date dateCreated) {
		this.name = name;
		this.dateCreated = dateCreated;
	}
	public TaskItem(long id, String name, Date dateCreated) {
		this.id = id;
		this.name = name;
		this.dateCreated = dateCreated;
	}
	
	public long getId() {
		return id;
	}
	public String getName() {
		return name;
	}
	public Date getDateCreated() {
		return dateCreated;
	}

	public void setId(long id) {
		this.id = id;
	}
	public void setName(String name) {
		this.name = name;
	}
	public void setDateCreated(Date dateCreated) {
		this.dateCreated = dateCreated;
	}

	public String toString() {
		return name + "\n" + dateCreated;
	}

	// Comparator
	public int compareTo(TaskItem another) {
		char myName = this.getName().charAt(0);
		char urName = another.getName().charAt(0);
		if (myName < urName) {
			return -1; // Less than
		} else if (myName > urName) {
			return 1; // Greater than
		}
		return 0; // Equal to
	}

}
