import java.util.Scanner;

public class SportsTrainingCalculator2 {
	
	public static void main(String[] args)	{
		//Ask Name
		String name;
		Scanner scan = new Scanner(System.in);
		
		System.out.println("What is your name? ");
		name = scan.nextLine();
		
		System.out.println("Your name is " + name);
		
		//Ask Gender
		String gender;
		
		System.out.println("What is your gender? (Male or Female) ");
		gender = scan.nextLine();
		
		//Validate Gender
		if (gender.equalsIgnoreCase("Male")) {
			System.out.println("You're a " + gender);
		} else if(gender.equalsIgnoreCase("Female")) {
			System.out.println("You're a " + gender);
		} else
		{System.out.println("You're neither a male nor female? Gosh");
		System.exit(0);
		}
		
		//Ask Sport
		String sport;
		
		System.out.println("What is your favorite sport? ");
		sport = scan.nextLine();
		
		System.out.println("Your sport is " + sport);
		
		//Ask Age
		int age;
		
		System.out.println("What is your age? ");
		age = scan.nextInt();
		
		//Validate Age
		if (age >= 18 && age <= 30) {
			System.out.println("Your age is within the allowed range of 18-30");
		}	else {
			System.out.println("Your age is not within the allowed range of 18-30");
			System.exit(0);
		}
		
		//Ask Resting Heart Rate
		int rhr;
		
		System.out.println("What is your Resting Heart Rate? ");
		rhr = scan.nextInt();
		
		if (rhr<0)
		{System.out.println("You entered a wrong value");
			System.exit(0);
		}
		//Calculate Maximum Heart Rate
		int mhr = 220 - age;
		
		//Calculate Training Heart Rate
		int thr = (int) (0.8 * mhr);
		System.out.println("Your Training Heart Rate is " + thr);
		
		//Calculate V02Max
		int v02max = 15 * mhr / rhr;
		
		if (v02max >= 40 && v02max <= 60) { // Male
			System.out.println("You are suitable for this sport as your V02Max is " + v02max);
		}	else if ( v02max >= 43 && v02max <=60) { // Female
			System.out.println("You are suitable for this sport as your V02Max is " + v02max);
		}
		else {
			System.out.println("You are unsuitable for this sport as your V02Max is " + v02max);
		}
		System.exit(0);
			}
}