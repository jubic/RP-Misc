import java.util.Scanner;

public class DrivingSchool {
	public static void main(String[] args) {
		AutoCar autoCars[] = new AutoCar[10];
		ManualCar manualCars[] = new ManualCar[10];
		MotorBike motorbikes[] = new MotorBike[10];
		Student students[] = new Student[30];
		manualCars[0] = new ManualCar("LM1", 4, 5);
		manualCars[1] = new ManualCar("LM2", 4, 5);
		manualCars[2] = new ManualCar("LM3", 4, 5);
		manualCars[3] = new ManualCar("LM4", 4, 5);
		manualCars[4] = new ManualCar("LM5", 4, 5);

		autoCars[0]= new AutoCar("LA1", 4);
		autoCars[1]= new AutoCar("LA2", 4);
		autoCars[2]= new AutoCar("LA3", 4);
		autoCars[3]= new AutoCar("LA4", 4);
		autoCars[4]= new AutoCar("LA5", 4);

		int choice = -1;
		Scanner scan = new Scanner(System.in);

		while (choice != 0) {
			System.out.println("\n=====================================");
			System.out.println("1. Display all vehicles");
			System.out.println("2. Display all students");
			System.out.println("3. Register a new student");
			System.out.println("4. Assign student an auto car");
			System.out.println("5. Assign student a manual car");
			System.out.println("6. Assign student a motorbike");
			System.out.println("7. Deregister a student");
			System.out.println("0. Exit");

			System.out.println("Please enter your choice: ");
			choice = scan.nextInt();


			if (choice == 1) {
				for (int i = 0; i < manualCars.length; i++) {
					ManualCar manualCar = manualCars[i];
					if (manualCar != null) {
						manualCar.show();
					}
				}

				for (int i = 0; i < motorbikes.length; i++) {
					MotorBike motorbike = motorbikes[i];
					if (motorbike != null) {
						motorbike.show();
					}
				}

				for (int i = 0; i < autoCars.length; i++) {
					AutoCar autoCar = autoCars[i];
					if (autoCar != null) {
						autoCar.show();
					}
				}
			} else if (choice == 2) {
				boolean hasStudents = false;
				for (int i = 0; i < students.length; i++) {
					Student student = students[i];
					if (student != null) {
						student.show();
						hasStudents = true;
					}
				}
				if(!hasStudents) {
					System.out.println("No students registered");
				}
			} else if (choice == 3) {
				int foundIndex = -1;
				for (int i = 0; i < students.length; i++) {
					Student student = students[i];
					if (student == null) {
						foundIndex = i;
						break;
					}
				}
				if (foundIndex != -1) {
					scan = new Scanner(System.in);
					System.out.println("Enter student id: ");
					String id = scan.nextLine();

					for (int i = 0; i < students.length; i++) {
						Student student = students[i];
						if (student!=null && id.equals(student.Id)) {
							System.out.println("Student with this id already exists");
							return;
						}
					}

					System.out.println("Enter student name: ");
					String name = scan.nextLine();

					students[foundIndex] = new Student(id, name);
					System.out.println("A new student is added.");
				} else {
					System.out.println("The student array is full.");
				}
			} else if (choice == 4) {
				scan = new Scanner(System.in);
				System.out.println("Enter student id:");
				String id = scan.nextLine();

				Student selectedStudent = null;
				for (int i = 0; i < students.length; i++) {
					Student student = students[i];
					if (student!=null && id.trim().equals(student.Id.trim())) {
						selectedStudent = student;
						break;
					}
				}
				// assign car only if student is found and no autocars has been allocated to him
				if (selectedStudent != null && selectedStudent.autoCar == null) {
					for (int i = 0; i < autoCars.length; i++) {
						AutoCar autoCar = autoCars[i];
						if (autoCar.isVehicleAvailable()) {
							autoCar.setAvail(false);
							selectedStudent.autoCar = autoCar;
							System.out.println("AutoCar "+autoCar.licensePlate+" is assigned to Student "+selectedStudent.Id);
							break;
						}
					}

				}
			} else if (choice == 5) {
				System.out.println("All manual cars already allocated");

			} else if (choice == 6) {
				System.out.println("All motorbikes already allocated");
			} else if (choice == 7) {
				scan = new Scanner(System.in);
				System.out.println("Enter student id:");
				String id = scan.nextLine();

				Student selectedStudent = null;
				for (int i = 0; i < students.length; i++) {
					Student student = students[i];
					if (student!=null && id.equals(student.Id)) {
						selectedStudent = student;

						if (selectedStudent.autoCar != null) {
							selectedStudent.autoCar.setAvail(true);
							selectedStudent.autoCar = null;
						}
						if (selectedStudent.manCar != null) {
							selectedStudent.autoCar.setAvail(true);
							selectedStudent.manCar = null;
						}
						if (selectedStudent.bike != null) {
							selectedStudent.autoCar.setAvail(true);
							selectedStudent.bike = null;
						}
						students[i] = null;
						System.out.println("Student deregistered");
						break;
					}
				}//end for

				if(selectedStudent==null) {
					System.out.println("Error, no student with given id");
				}


			} else if (choice == 0) {
				break;
			} else {
				System.out.println("Invalid choice, please enter again.");
			}
		}
	}

}
