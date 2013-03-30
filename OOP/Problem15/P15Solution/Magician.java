public class Magician extends Hero 
{
	String gender;
	
	public Magician(String nName, String nGender, int nPower) 
	{
		super(nName, nPower);
		gender = nGender;
	}

	public double calPowerInFighting()
	{
		return power*randomGenerator.nextDouble();
	
	}
	
	public void printInfo() 
	{
		super.printInfo();
		System.out.println("Gender: " +gender);
		System.out.println("I am a Magician!");
	}
}
