package ContactBook2Solution;

import java.util.ArrayList;
import java.util.Scanner;

public class ContactBook {
	ArrayList<RegularMember> regMemArray = new ArrayList<RegularMember>();
	ArrayList<AlumniMember> aluMemArray = new ArrayList<AlumniMember>();
	Scanner scan = new Scanner(System.in);

	public ContactBook() {
		regMemArray.add(new RegularMember(80111, "Jane", "80111@myrp.sg",
				Diploma.DBIS, School.STA, "W46J", 1.6));

		regMemArray.add(new RegularMember(80222, "Peter", "8022@myrp.sg",
				Diploma.DIT, School.SIT, "W46K", 1.7));

		aluMemArray.add(new AlumniMember(40111, "Tom", "40111@myrp.sg", 2007,
				"Sales Person"));

		aluMemArray.add(new AlumniMember(60123, "Cindy", "60123@myrp.sg", 2009,
				"Teacher"));
		aluMemArray.add(new AlumniMember(60234, "Lena", "60234@myrp.sg", 2009,
				"Biotechnician"));
	}

	public void printAllMemInfo() {
		System.out.println("Personal Particulars of all regular members :");
		System.out.println("");
		for (RegularMember regularMember : regMemArray) {
			regularMember.printMemberInfo();
		}
		System.out.println("");
		System.out.println("Personal Particulars of all alumni members :");
		System.out.println("");
		for (AlumniMember alumniMember : aluMemArray) {
			alumniMember.printMemberInfo();
		}
	}

	public void printHighestGpaInfo() {
		System.out.println("");
		System.out.println("Personal Particulars of the regular member/s with the highest GPA :");
		double highest = 0;
		for (RegularMember regularMember : regMemArray) {
			if (regularMember.getGpa() > highest) {
				highest = regularMember.getGpa();
			}
		}
		for (RegularMember regularMember : regMemArray) {
			if (regularMember.getGpa() == highest) {
				regularMember.printMemberInfo();
			}
		}
	}

	public void printSameOccInfo() {
		System.out.println("");
		System.out.println("Enter an occupation: ");
		String occupation = scan.nextLine();
		System.out.println("Personal Particulars of alumni member/s who are " + occupation + 's');
		for (AlumniMember alumniMember : aluMemArray) {
			if (alumniMember.getOccupation().equalsIgnoreCase(occupation)) {
				alumniMember.printMemberInfo();
			}
		}
	}

	public static void main(String[] args) {
		ContactBook contactbook = new ContactBook();

		contactbook.printAllMemInfo();
		contactbook.printHighestGpaInfo();
		contactbook.printSameOccInfo();
	}
}