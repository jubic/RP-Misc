public class Item 
{
	String name;
	int power;
  
	public Item(String nName, int nPower) 
	{
		name = nName;
		power = nPower;
	}
	
	public void printItemInfo()
	{
		System.out.print("Item name: " +name);
		System.out.print(" Additional Power: " +power);
		System.out.println();
	}
}