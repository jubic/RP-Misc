package ContactBook2Solution;

public class Member {
	private int id;
	private String name;
	private String email;

	public Member(int id, String name, String email) {
		this.id = id;
		this.name = name;
		this.email = email;
	}
	
	public void printMemberInfo() {
		String output = "ID: " + this.id + "\tName: " + this.name
				+ "\tEmail: " + this.email;
		System.out.println(output);
	}
}