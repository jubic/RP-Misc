public class CommitteeClub extends Member {
	public String officialPosition;
	
	//Constructor
	public CommitteeClub(int idNumber, String name, String email, String officialPosition) {
		super(idNumber, name, email);
		this.officialPosition = officialPosition;
	}
	
	//Methods
	public String getOfficialPosition(){
		return officialPosition;
	}
	
	public String toString() {
		return super.toString() + "\tOfficial Position: " + officialPosition;
	}

	public double getGPA() {
		return 0;
	}

	public String getOccupation() {
		return null;
	}

	public String getClassGroup() {
		return null;
	}

	public int getYOG() {
		return 0;
	}

	public String editClassGroup(String editClass) {
		return null;
	}

	public String editOccupation(String occupation) {
		return null;
	}
}