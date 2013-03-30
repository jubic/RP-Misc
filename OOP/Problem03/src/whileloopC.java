import java.util.Scanner;
public class whileloopC {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		System.out.println("How many months are you entering? ");
		int month = scan.nextInt();
		int count = 1;
		while (count<=month) {
			System.out.println("The is Month " + count);
			count = count + 1;
		}
	}
}
