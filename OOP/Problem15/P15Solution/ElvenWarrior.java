public class ElvenWarrior extends Hero 
{
	int age;
	String gender;
	
	public ElvenWarrior(String nName, int nAge, String nGender, int nPower) 
	{
		super(nName, nPower);
		age = nAge;
		gender = nGender;
	}

	public double calPowerInFighting()
	{
		return (power+50)*randomGenerator.nextDouble();
	}
	
	public void printInfo() 
	{
		super.printInfo();
		System.out.println("Age: " +age);
		System.out.println("Gender: " +gender);
		System.out.println("I am an Elven Warrior!");
	}
}
