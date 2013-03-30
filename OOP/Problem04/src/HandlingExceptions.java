// Question 3
public class HandlingExceptions {
	public static void main(String[] args) {
		int[] numbers = { 10, 5, 4, 2, 0, 1, 0 };
		
		System.out.println(numbers);

		try {
			for (int i = 0; i < numbers.length; i++) {
				System.out.println(100 / numbers[i]);
			}
		} catch (Exception ex) {
			System.out.println("Error here!");
			// ex.printStackTrace();
		}
	}
}