import java.util.Scanner;

public class SportsTrainingCalculator {
	
	public static void main(String[] args)	{
		//Ask Name
		String name;
		Scanner scan = new Scanner(System.in);
		
		System.out.println("What is your name? ");
		name = scan.nextLine();
		
		//Ask Gender
		String gender;
		
		System.out.println("What is your gender? ");
		gender = scan.nextLine();
		
		//Ask Age
		int age;
		
		System.out.println("What is your age? ");
		age = scan.nextInt();
		
		while (age<0)
		{System.exit(0);
		}
		//Ask Resting Heart Rate
		int rhr;
		
		System.out.println("What is your Resting Heart Rate? ");
		rhr = scan.nextInt();
		
		while (rhr<0)
		{System.exit(0);
		}
		//Calculate Maximum Heart Rate
		int mhr = 220 - age;
		
		//Calculate Training Heart Rate
		int thr = (int) (0.8 * mhr);
		
		//Calculate V02Max
		int v02max = 15 * mhr / rhr;
		
		//Printing all the data
		System.out.println(" ");
		System.out.println("Your name is " + name);
		System.out.println("Your gender is " + gender);
		System.out.println("Your age is " + age);
		System.out.println("Your Resting Heart Rate is " + rhr);
		System.out.println("Your Calculated Maximum Heart Rate is " + mhr);
		System.out.println("Your Calculated Training Heart Rate is " + thr);
		System.out.println("Your Calculated V02Max is " + v02max);
		System.out.println("Please confirm that the above datas are correct. Have a nice day.");
		System.exit(0);
			}
}
