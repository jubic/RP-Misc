import java.util.*;
public class ContactBook {
	public static void main(String[] args) {
		Scanner userInputI = new Scanner(System.in);
		Scanner userInputS = new Scanner(System.in);

		ArrayList<Member> memberList = new ArrayList<Member>();
		
		memberList.add(new AlumniClub(91100, "Johnny", "johnny@hotmail.com", 2008, "Programmer"));
		memberList.add(new AlumniClub(91400, "Tom", "Tommmy@hotmail.com", 2008, "Freelancer"));
		memberList.add(new AlumniClub(92100, "Paul", "Pauly@hotmail.com", 2008, "Programmer"));
		memberList.add(new RegularClub(93000, "Cat", "Cat@gmail.com", "DIT", "SIT", "E66D", 3.00));
		memberList.add(new RegularClub(91101, "Andy", "andy@hotmail.com", "DBIS", "SIT", "E65L", 3.80));
		memberList.add(new CommitteeClub(92807, "CK", "CK@CK.com", "Bartender"));

	
		while(true){
			System.out.println("------------ CHOOSE YOUR OPTION ------------");
			System.out.println("1. Display all members information");
			System.out.println("2. Display Regular Member With Best GPA");
			System.out.println("3. Display Alumni Members By Occupation");
			System.out.println("4. Add a new club member (Regular/Alumni)");
			System.out.println("5. Edit the class group of a regular club member)");
			System.out.println("6. Edit the occupation of an alumni club member)");
			System.out.println("7. Display the personal information of all regular club members based on a class location)");
			System.out.println("8. Display the personal information of all alumni club members based on an year of graduation)");
			System.out.print("\nEnter your choice :  ");
			int choice = userInputI.nextInt();
			
			if(choice==1){
				
				System.out.println("\nMEMBERS' INFORMATION");
				System.out.println("=======================================================================================================================");
				for (Member member : memberList) { 
					member.show();
				}
				System.out.println("=======================================================================================================================");


			}else if (choice ==2){
				
				double bestGPA = 0;
				for (Member member : memberList) { 
					if(member.getGPA() > bestGPA){
						bestGPA=member.getGPA();
					}
				}
				
				System.out.println("\nMembers with Best GPA");
				System.out.println("=======================================================================================================================");

				for (Member member : memberList) { 
					if (member.getGPA() == bestGPA) {
						member.show();
					}
				}	
				System.out.println("=======================================================================================================================");
			
			} else if (choice == 3){
				
				System.out.print("Enter occupation :  ");
				
				String occupation=userInputS.nextLine();
				
				System.out.println("Alumni's Members by Occupation");
				System.out.println("=======================================================================================================================");

				for (Member member : memberList) { 
					if (member.getOccupation().equalsIgnoreCase(occupation)) {
						member.show();
					}
				}
				System.out.println("=======================================================================================================================");
				
			} else if (choice ==4){
				
				System.out.println("1. To add new Regular Club");
				System.out.println("2. To add new Alumni Club");
				System.out.print("\nEnter your choice :  ");
				int choice2 = userInputI.nextInt();
				
				while (choice2 != 1 && choice2 !=2){
					System.out.println("Please enter again! Invalid option!");
					System.out.println("1. To add new Regular Club Member");
					System.out.println("2. To add new Alumni Club Member");
					System.out.print("\nEnter your choice :  ");
					choice2 = userInputI.nextInt();
				}
				
				
				if (choice2 == 1){
					
					System.out.println("REGULAR MEMBER REGISTRATION");
					System.out.print("Enter ID	  : ");
					int idNum = userInputI.nextInt();

					System.out.print("Enter name  : ");
					String name= userInputS.nextLine();
					

					System.out.print("Enter email : ");
					String email= userInputS.nextLine();

					System.out.print("Enter diploma     : ");
					String diploma= userInputS.nextLine();
					
					System.out.print("Enter school      : ");
					String school= userInputS.nextLine();

					System.out.print("Enter class group : ");
					String classGroup= userInputS.nextLine();

					System.out.print("Enter GPA		    : ");
					double gpa= userInputI.nextDouble();

					memberList.add(new RegularClub (idNum,name,email,diploma,school, classGroup, gpa));

					
				} else if (choice2 == 2){
					
					System.out.println("ALUMNI MEMBER REGISTRATION");
					System.out.print("Enter ID	  : ");
					int idNum = userInputI.nextInt();

					System.out.print("Enter name  : ");
					String name= userInputS.nextLine();
					
					System.out.print("Enter email : ");
					String email= userInputS.nextLine();

					System.out.print("Enter year of graduation : ");
					int year = userInputS.nextInt();
					
					System.out.print("Enter occupation         : ");
					String job= userInputS.nextLine();
					
					memberList.add(new AlumniClub (idNum,name,email,year, job));

				}
			} else if (choice ==5){
				
				System.out.print("Enter Regular Member ID which you would like to edit :  ");
				int idNum = userInputI.nextInt();
				
				System.out.print("Enter the new class group for the Regular Member: ");
				String classGroup= userInputS.nextLine();
				
				for (Member member : memberList) { 
					if(member.idNumber==(idNum)){
						 member.editClassGroup(classGroup);
						break;
					}
				}
			} else if (choice ==6){
				
				System.out.print("Enter Regular Member ID which you would like to edit :  ");
				int idNum = userInputI.nextInt();
				
				System.out.print("Enter the new occupation for the Alumni Member: ");
				String occupation= userInputS.nextLine();
				
				for (Member member : memberList) { 
					if(member.idNumber==(idNum)){
						member.editOccupation(occupation) ;
						break;
					}
				}
			
			} else if (choice ==7){
				
				System.out.print("\nEnter the class location :  ");
				
				String classGroup = userInputS.nextLine();
				
				System.out.println("Regular's Members by Class Location");
				System.out.println("=======================================================================================================================");

				for (Member member : memberList) { 
					if(member.getClassGroup().equalsIgnoreCase(classGroup)){
						member.show();
					}
				}
				System.out.println("=======================================================================================================================");
			
			} else if (choice == 8){
				
				System.out.print("\nEnter the Year Of Graduation :  ");
				
				int yearOfGraduation = userInputI.nextInt();
				
				System.out.println("Alumni's Members by Year Of Graduation");
				System.out.println("=======================================================================================================================");

				for (Member member : memberList) { 
					if(member.getYOG()==yearOfGraduation){
						member.show();
					}
				}
				System.out.println("=======================================================================================================================");
			} 
		}
	}
}