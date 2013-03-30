public class Movies {
	public String title;
	public int rentCount;

	public Movies(String cTitle, int cRentCount) {
		title = cTitle;
		rentCount = cRentCount;
	}

	public void updateCount() {
		rentCount++;
	}

	public double currentEarnings(int rentCount) {
		return rentCount * 2.1;
	}
}
