public class StoringInformationInArray {
	public static void main(String[] args) {
		int[] numArray = new int[10];
		numArray[0] = 60108;
		numArray[1] = 60121;
		
		for (int i=0; i< numArray.length; i++){
			System.out.println(numArray[i]);
		}
		
		System.out.println("---------");
		for (int i=0; i<numArray.length; i++)
		{
			if (numArray[i]==0)
			{
				numArray[i]=60128;
				break;
				
			}
		}
		
		for (int i=0; i< numArray.length; i++){
			System.out.println(numArray[i]);
		}
		
		System.out.println("---------");
		for (int i=0; i<numArray.length; i++)
		{
			if (numArray[i]==60121)
			{
				numArray[i]=0;
				break;
			}
			}
		for (int i=0; i< numArray.length;i++){
			System.out.println(numArray[i]);
		}
	}
}
