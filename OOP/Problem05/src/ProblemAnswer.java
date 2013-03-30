import java.util.*;
public class ProblemAnswer {
	public static void main(String[] args) {
		int choice = 0;
		int studentid = 0;
		String studentphonenumber = " ";
		String studentname = " ";
		String studentclass = " ";
		int numberofstudents = 200;
		int[] studentidArray = new int[numberofstudents];
		String[] studentnameArray = new String[numberofstudents];
		String[] studentclassArray = new String[numberofstudents];
		String[] studentphonenumberArray = new String[numberofstudents];
				
		Scanner userInput1 = new Scanner(System.in); // Scan string
		Scanner userInput2 = new Scanner(System.in); // Scan integer
		
		while (choice != 9) {
			try {
				System.out.println("===========================================");
				System.out.println("Welcome to IG Registry System");
				System.out.println("===========================================");
				System.out.println("\t1 - Display all members' profile");
				System.out.println("\t2 - Add a new member");
				System.out.println("\t3 - Edit an existing member");
				System.out.println("\t4 - Delete an existing member");
				System.out.println("\t5 - Increase maximum number of students in IG");
				System.out.println("\t9 - Exit");

				System.out.println("Please enter your preferred action: ");
				choice = userInput2.nextInt();

				if (choice == 1) {
					// Display details
					System.out.println("===========================================");
					System.out.println("You have chosen to display all members' profile");
					System.out.println("===========================================");
					
					for (int i =0; i < numberofstudents; i++)
					{
						if (studentidArray[i] != 0)
						{
							System.out.println("Students' Name: " + studentnameArray[i]);
							System.out.println("Students' ID: " + studentidArray[i]);
							System.out.println("Students' Class: " + studentclassArray[i]);
							System.out.println("Students' Phone Number: " + studentphonenumberArray[i]);
							System.out.println("===========================================");
							}
					}
					System.out.println("\n===== End of Displaying =====");
				}
				else if (choice == 2) {
					// Add new member
					System.out.println("===========================================");
					System.out.println("You have chosen to add a new member");
					System.out.println("===========================================");
					
					System.out.println("Please enter the Member's ID: ");
					studentid = userInput2.nextInt();
					
					System.out.println("Please enter the Member's Name: ");
					studentname = userInput1.nextLine();
					
					System.out.println("Please enter the Member's Class: ");
					studentclass = userInput1.nextLine();
					
					System.out.println("Please enter the Member's Phone Number: ");
					studentphonenumber = userInput1.nextLine();
					
					for (int i = 0; i < numberofstudents; i++)
					{
						if (studentidArray[i] == 0)
						{
							studentidArray[i] = studentid;
							studentnameArray[i] = studentname;
							studentclassArray[i] = studentclass;
							studentphonenumberArray[i] = studentphonenumber;
							System.out.println("===========================================");
							System.out.println("This member has been added successfully!");
							System.out.println("===========================================");
							System.out.println("Member's ID: " + studentidArray[i]);
							System.out.println("Member's Name: " + studentnameArray[i]);
							System.out.println("Student's Class: " + studentclassArray[i]);
							System.out.println("Member's Phone Number: " + studentphonenumberArray[i]);
							break;
							}
						}
					}
				else if (choice == 3) {
					// Edit member
					System.out.println("===========================================");
					System.out.println("You have chosen to edit an existing member");
					System.out.println("===========================================");
					
					System.out.println("Please enter the student ID you want to edit : ");
					studentid = userInput2.nextInt();
					
					System.out.println("Please enter the Member's name: ");
					studentname = userInput1.nextLine();
					
					System.out.println("Please enter the Member's Class: ");
					studentclass = userInput1.nextLine();
					
					System.out.println("Please enter the Member's phone number: ");
					studentphonenumber = userInput1.nextLine();
					
					for (int i = 0; i < numberofstudents; i++)
					{
						if (studentidArray[i] == studentid)
						{
							studentnameArray[i] = studentname;
							studentclassArray[i] = studentclass;
							studentphonenumberArray[i] = studentphonenumber;
							System.out.println("===========================================");
							System.out.println("This member has been edited successfully!");
							System.out.println("===========================================");
							System.out.println("Member's ID: " + studentidArray[i]);
							System.out.println("Member's Name: " + studentnameArray[i]);
							System.out.println("Student's Class: " + studentclassArray[i]);
							System.out.println("Member's Phone Number: " + studentphonenumberArray[i]);
							break;
							}
						}
					}
				
					
				else if (choice == 4) 
				{
					// Delete member
					System.out.println("===========================================");
					System.out.println("You have chosen to delete an existing member");
					System.out.println("===========================================");
					
					System.out.println("Please enter the student ID you want to delete");
					studentid = userInput2.nextInt();
						
					for (int i = 0; i < numberofstudents; i++)
					{
						if (studentidArray[i] == studentid)
						{
							studentidArray[i] = 0;
							studentnameArray[i] = " ";
							studentclassArray[i] = " ";
							studentphonenumberArray[i] = " ";
							System.out.println("=============================================");
							System.out.println("This member has been deleted successfully!");
							System.out.println("=============================================");
							System.out.println("Member's ID: " + studentidArray[i]);
							System.out.println("Member's Name: " + studentnameArray[i]);
							System.out.println("Student's Class: " + studentclassArray[i]);
							System.out.println("Member's Phone Number: " + studentphonenumberArray[i]);
							break;
							}
						}
				}
				else if (choice == 5)
				{ //Exceed maximum number of students
					System.out.println("=============================================");
					System.out.println("You have chosen to increase the maximum number of students in the registry");
					System.out.println("=============================================");
					numberofstudents = numberofstudents + 1;
					System.out.println("The maximum number of students the IG can have now is " + numberofstudents);
				}
				else if (choice == 9)
				{
					// Exit program
					System.out.println("You have chosen to Exit.\nProgram will exit now.");
					System.exit(0);
					} 
				else {
					// Unknown option
					System.out.println("Unknown option, please choose again.");
					}
					}
			catch (Exception e) {
				// catch \n of the scan error exception
				@SuppressWarnings("unused")
				String junk = userInput1.nextLine();
				System.out.println(" ** Error! Unknown option. ** ");
				System.out.println(" ** Please try again ** ");
			}
		}
	}
}