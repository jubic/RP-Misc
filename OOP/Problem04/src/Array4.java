public class Array4 {
	public static void main(String[] args) {
		// array of numbers
		int[] numberArray = { 10, 33, 21, 42, 57, 34, 78, 21, 34, 95, 34 };

		int matchCount = 0;
				
		for (int i = 0; i < numberArray.length; i++) {

			// write code here
			if (numberArray[i] == 34) {
				matchCount = matchCount + 1;
				}
		}
		System.out.println(matchCount);
	}
}
