import java.util.Scanner;

public class Solution {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		System.out.print("Athlete's name:");
		String name = scan.nextLine();

		System.out.print("Athlete's age:");
		int age = scan.nextInt();

		System.out.print("Athlete's resting heart rate:");
		int restingHeartRate = scan.nextInt();
		scan.nextLine();

		System.out.println("Athlete's sport:");
		String sport = scan.nextLine();

		System.out.println("Athlete's gender:");
		String gender = scan.nextLine();
		int maxHeartRate = 220 - age;

		double trainingHeartRate = 0.8 * maxHeartRate;	
		double v02max = 15 * maxHeartRate / restingHeartRate;
	
		boolean acceptable = true;
		if (sport.equals("Basketball")) {
			if (age >= 18 && age <= 32) {
				if (gender.equals("Male")) {
					if (v02max < 40 || v02max > 60) {
						acceptable = false;
					}
				} else { // female case
					if (v02max < 43 || v02max > 60) {
						acceptable = false;
					}
				}
			} else {
				acceptable = false;
			}
		}

		System.out.println("The training heart rate of " + name + " is "
				+ trainingHeartRate);
		System.out.println("The V02Max of " + name + " is " + v02max);
		if (acceptable) {
			System.out.println("You're within the guidelines for your sport");
		} else {
			System.out.println("You're out of the guidelines for your sport");
		}
	}
}
