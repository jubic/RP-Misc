public class Barbarian extends Hero 
{
	int age;
	
	public Barbarian(String nName, int nAge, int nPower) 
	{
		super(nName, nPower);
		age = nAge;
	}

	public double calPowerInFighting()
	{
		return (power+10)*randomGenerator.nextDouble();
	}
	
	public void printInfo() 
	{
		super.printInfo();
		System.out.println("Age: " +age);
		System.out.println("I am a Magician!");
	}
}