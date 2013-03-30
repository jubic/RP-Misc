package ArrayListExample;

import java.util.ArrayList;

public class ArrayListEgFour {

	public static void main(String[] args) {
		ArrayList<String> names = new ArrayList<String>();

		names.add("Amy");
		names.add("Bob");
		names.add("Chris");

		// Print original arrangement
		System.out.println("Before adding at index 1:");
		for (int j = 0; j < names.size(); j++)
			System.out.println(j + ": " + names.get(j));

		// Insert an element
		names.add(1, "Valerie");

		// Print new arrangement
		System.out.println("\nAfter adding at index 1:");
		for (int j = 0; j < names.size(); j++)
			System.out.println(j + ": " + names.get(j));

	}
}