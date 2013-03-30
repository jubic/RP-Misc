import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Athlete's name:");
        String name = scan.nextLine();
        
        System.out.println("Athlete's gender:");
        String gender = scan.nextLine();
       
        System.out.println("Athlete's age:");
        int age = scan.nextInt();
        
        System.out.println("Athlete's resting heart rate:");
        int restingHeartRate = scan.nextInt();
		int maxHeartRate = 220 - age;

		double trainingHeartRate = 0.8 * maxHeartRate;
		double v02max = 15 * maxHeartRate / restingHeartRate;

		System.out.println(name + ", " + gender + ", " + age);
		System.out.println("The maximum heart rate of " + name + " is " + maxHeartRate);
        System.out.println("The training heart rate of " + name + " is " + trainingHeartRate);
        System.out.println("The V02Max of " + name + " is " + v02max);
    }
}
