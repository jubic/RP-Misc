import java.util.ArrayList;
import java.util.Random;

public class Hero 
{
	String name;
	int power;

	ArrayList<Item> itemList;
	Random randomGenerator;

	public Hero(String nName,int nPower) 
	{
		name = nName;
	    power = nPower;
	    
	    itemList = new ArrayList<Item>();
	    randomGenerator = new Random();
	}
	
	public double calPowerInFighting()
	{
		return power*randomGenerator.nextDouble();
	}
	
	public void printInfo() 
	{
		System.out.println("I have " +itemList.size() + " items.");
		for (int i=0; i<itemList.size(); i++) 
		{
			Item myItem = itemList.get(i);
	    	myItem.printItemInfo();
	    }
		System.out.println("Name: " +name);
	}
	
	public void gainPowers()
	{
		power += 10;
	}

	public void losePowers()
	{
		power -= 15;
	}

	public void pickUpItem (Item newItem) 
	{
		itemList.add(newItem);
		power += newItem.power;

		System.out.println("Item "+newItem.name +" is picked up by " +name);
		
	}

	public void attackHero(Hero defender)
	{
		boolean result = false;

		String attackerType = getClass().getName();
		String defenderType = defender.getClass().getName();
	    System.out.println(name +"(A " +attackerType +") is attacking " +defender.name +"(A " +defenderType +")");

	    if (calPowerInFighting() > defender.calPowerInFighting())
	    {
	    	result = true;
	    } 

	    if(result)
	    {
	    	System.out.println("Attack succeeded!");
	    	gainPowers();
	    	defender.losePowers();
	    }
	    else 
	    {
	    	System.out.println("Attack failed!");
	    	losePowers();
	    	defender.gainPowers();
	    }
	}
}


