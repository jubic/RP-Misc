package ArrayListExample;

import java.util.ArrayList;

public class ArrayListEgThree {

	public static void main(String[] args) {
		// Create an ArrayList that holds references to String
		ArrayList<String> names = new ArrayList<String>();

		// Add three String references
		names.add("Amy");
		names.add("Bob");
		names.add("Cindy");

		// Access and print out the Objects
		for (int j = 0; j < names.size(); j++)
			System.out.println("element " + j + ": " + names.get(j));

		// Replace "Amy" with "Zoe"
		names.set(0, "Zoe");
		System.out.println();

		// Access and print out the Objects
		for (int j = 0; j < names.size(); j++)
			System.out.println("element " + j + ": " + names.get(j));

	}
}