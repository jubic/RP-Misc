public class Array2 {
	public static void main(String[] args) {
		String[] myPets = new String[3];
		myPets[0] = "Cat";
		myPets[1] = "Dog";
		myPets[2] = "Hamster";
		
		//While loop
		int count = 0;
		while(count<myPets.length) {
			System.out.println(myPets[count]);
			count = count + 1;
		}
		
		//For loop
		for(int i=0; i<myPets.length; i++) {
			System.out.println(myPets[i]);
		}
	}

}
