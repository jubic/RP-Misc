import java.util.Scanner;

public class Solution {
	public static void main(String[] args) {
		int[] studentArray = new int[100];
		String[] nameArray = new String[100];
		String[] telephoneArray = new String[100];
		Scanner scan = new Scanner(System.in);
		int choice = 0;

		while (choice != 9) {
			try {
				System.out.println("****IG Member App****");
				System.out.println("Menu:");
				System.out.println("\t1 - Display all members");
				System.out.println("\t2 - Add a new member");
				System.out.println("\t3 - Edit an existing member");
				System.out.println("\t4 - Delete an existing member");
				System.out.println("\t9 - Exit");

				System.out.println("Please enter your selection : ");
				choice = scan.nextInt();

				// Display all members
				if (choice == 1) {
					System.out.println("===== Displaying ALL Members =====");
					for (int i = 0; i < studentArray.length; i++) {
						if (studentArray[i] != 0) {
							System.out.println("==============================");
							System.out.println("Student ID: " + studentArray[i]);
							System.out.println("Name: " + nameArray[i]);
							System.out.println("Telephone:" + telephoneArray[i]);
							System.out.println("==============================");
						}
					}
					System.out.println("===== End of Displaying =====\n\n");
				}

				// Add a new member
				else if (choice == 2) {
					int foundIndex = -1;
					for (int i = 0; i < studentArray.length; i++) {
						if (studentArray[i] == 0) {
							foundIndex = i;
							break;
						}
					}

					if (foundIndex != -1) {
						scan = new Scanner(System.in);
						System.out.println("Enter student ID : ");
						studentArray[foundIndex] = scan.nextInt();

						scan = new Scanner(System.in);
						System.out.println("Enter name : ");
						nameArray[foundIndex] = scan.nextLine();

						scan = new Scanner(System.in);
						System.out.println("Enter telephone : ");
						telephoneArray[foundIndex] = scan.nextLine();

					} else {
						System.out.println("Contact book is full.\n");
					}
				}

				// Edit an existing member
				else if (choice == 3) {
					scan = new Scanner(System.in);
					System.out.println("Enter student ID : ");
					int studentID = scan.nextInt();

					int foundIndex = -1;
					for (int i = 0; i < studentArray.length; i++) {
						if (studentArray[i] == studentID) {
							foundIndex = i;
							break;
						}
					}

					if (foundIndex != -1) {
						System.out.println("Current name is : " + nameArray[foundIndex]);
						scan = new Scanner(System.in);
						System.out.println("Enter amended name : ");
						nameArray[foundIndex] = scan.nextLine();
						
						System.out.println("Current telephone is : " + telephoneArray[foundIndex]);
						scan = new Scanner(System.in);
						System.out.println("Enter new telephone number : ");
						telephoneArray[foundIndex] = scan.nextLine();
						
						System.out.println("Entry has been edited.\n");
					} else {
						System.out.println("Invalid student ID.\n");
					}

				}

				// Delete an existing member
				else if (choice == 4) {
					scan = new Scanner(System.in);
					System.out.println("Enter student ID : ");
					int studentID = scan.nextInt();

					int foundIndex = -1;
					for (int i = 0; i < studentArray.length; i++) {
						if (studentArray[i] == studentID) {
							foundIndex = i;
							break;
						}
					}

					if (foundIndex != -1) {
						studentArray[foundIndex] = 0;
						nameArray[foundIndex] = null; // optional
						telephoneArray[foundIndex] = null; // optional
						System.out.println("Entry has been deleted.\n");
					} else {
						System.out.println("Invalid student ID.\n");
					}

				}

				// Option 'Exit' actions here
				else if (choice == 9) {
					System.out.println("You have chosen to Exit.\nProgram will exit now.");
				}

				// Unknown option
				else {
					System.out.println("Unknown option, please choose again.\n");
				}

			} catch (Exception e) {
				// catch \n of the scan error exception 
				@SuppressWarnings("unused")
				String junk = scan.nextLine();
				System.out.println("** Error! Input not recognised. **");
				System.out.println(" ** Please try again ** \n\n");
			}
		}
	}
}