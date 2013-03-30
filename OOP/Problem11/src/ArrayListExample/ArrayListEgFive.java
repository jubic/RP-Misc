package ArrayListExample;

import java.util.ArrayList;

public class ArrayListEgFive {

	public static void main(String[] args) {
		// Create an ArrayList that holds references to String
		ArrayList<String> names = new ArrayList<String>();

		// Add three Object references and two nulls
		names.add("Amy");
		names.add(null);
		names.add("Bob");
		names.add(null);
		names.add("Cindy");
		System.out.println("size: " + names.size());

		// Access and print out the Objects
		for (int j = 0; j < names.size(); j++)
			System.out.println("element " + j + ": " + names.get(j));
	}
}