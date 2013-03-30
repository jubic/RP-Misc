public class Array3 {
	public static void main(String[] args) {
		String[] daysOfWeek = new String[7];
		
		daysOfWeek[0] = "Monday";
		daysOfWeek[1] = "Tuesday";
		daysOfWeek[2] = "Wednesday";
		daysOfWeek[3] = "Thursday";
		daysOfWeek[4] = "Friday";
		daysOfWeek[5] = "Saturday";
		daysOfWeek[6] = "Sunday";
		
		//For loop
		for(int i=0; i<daysOfWeek.length; i++) {
			System.out.println(daysOfWeek[i]);
		}
		System.out.println("The size of the array is = " + daysOfWeek.length); 
	}

}
