package ArrayListExample;

import java.util.ArrayList;

public class ArrayListEg {

	public static void main(String[] args) {
		// Create an ArrayList that holds references to String
		ArrayList<String> names = new ArrayList<String>();

		// Add three String references
		names.add("Amy");
		names.add("Bob");
		names.add("Cindy");

		// Access and print out the three String Objects
		System.out.println("element 0: " + names.get(0));
		System.out.println("element 1: " + names.get(1));
		System.out.println("element 2: " + names.get(2));
	}
}
