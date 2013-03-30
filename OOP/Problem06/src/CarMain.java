public class CarMain {
	public static void main(String[] args) {
		Car myCar = new Car();
		myCar.brand = "Honda";
		myCar.model = "CR-V";
		myCar.capacity = 2400;
		myCar.licensePlate = "SJH1097A";
		myCar.price = 103000.0;
		myCar.insured = false;
		
		Car dadCar = new Car();
		dadCar.brand = "Toyota";
		dadCar.model = "Camry";
		dadCar.capacity = 2000.5;
		dadCar.licensePlate = "SGA411B";
		dadCar.price = 92000.0;
		dadCar.insured = true;
		
		
		Car momCar = new Car();
		momCar.brand = "Nissan";
		momCar.model = "Murano";
		momCar.capacity = 3500;
		momCar.licensePlate = "EA5Y";
		momCar.price = 132000.0;
		momCar.insured = true;
		
		System.out.println("Mom's car is = " + momCar.model);
		System.out.println("My " +myCar.brand+ " is insured? " + myCar.insured);
		double CarPriceDifference = (myCar.price - dadCar.price);
		System.out.println("My " +myCar.brand+ " is $" + CarPriceDifference + " more expensive than my Dad's " +dadCar.brand);
		
		double totalPrice = 0.0;
		double avePrice;
		
		//Create array "carArray"
		Car[] carArray = {myCar, dadCar, momCar};
		
		for (int i = 0; i<carArray.length; i++){
			totalPrice+=carArray[i].price;
		}
		avePrice = totalPrice/carArray.length;
		
		System.out.println("Average Price = $" + avePrice);
		
		double CarPriceDifference2 = (carArray[2].price - carArray[0].price);
		
		System.out.println("Mom " +carArray[2].model+ " is " +CarPriceDifference2+ " more expensive than my " +carArray[0].brand);
}
}
