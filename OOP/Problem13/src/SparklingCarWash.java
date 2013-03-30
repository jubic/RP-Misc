import java.util.*;
public class SparklingCarWash {
	public static void main(String[] args) {
		
		ArrayList<Outlet> outletList = new ArrayList<Outlet>();
		
		outletList.add(new Outlet("Orchard Sparkling CarWash", true, 1));
		outletList.add(new Outlet("Novena Sparkling CarWash", false, 0));
		outletList.add(new Outlet("Woodlands Sparkling CarWash", true, 1));

		//Orchard Oulet

		//String carType, String licensePlate, double carWashPrice
		Car car1 = new Car("SUV", "EX123Z", 7.55);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash1 = new CarWash("Normal Wash", true, car1, outletList.get(0));
		car1.services.add(wash1);
		outletList.get(0).carList.add(car1);
		
		//String carType, String licensePlate, double carWashPrice
		Car car3 = new Car("Sedan", "SBY278G", 6.55);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash3 = new CarWash("Normal Wash", true, car3, outletList.get(0));
		car3.services.add(wash3);
		outletList.get(0).carList.add(car3);
		
		//String carType, String licensePlate, double carWashPrice
		Car car5 = new Car("Minibus", "ABC123D", 9.55);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash5 = new CarWash("Polish Wash", true, car5, outletList.get(0));
		car5.services.add(wash5);
		outletList.get(0).carList.add(car5);
		
		//String carType, String licensePlate, double carWashPrice
		Car car7 = new Car("MotorBike", "ABC123D", 11.55);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash7 = new CarWash("Wax", true, car7, outletList.get(0));
		car7.services.add(wash7);
		outletList.get(0).carList.add(car7);
		
		//Novena Outlet
		
		//String carType, String licensePlate, double carWashPrice
		Car car2 = new Car("SUV", "SBB123Z", 7.55);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash2 = new CarWash("Normal", true, car2, outletList.get(1));
		car2.services.add(wash2);
		outletList.get(1).carList.add(car2);
		
		//String carType, String licensePlate, double carWashPrice
		Car car4 = new Car("SUV", "SBB123Z", 7.35);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash4 = new CarWash("Normal", true, car4, outletList.get(1));
		car4.services.add(wash4);
		outletList.get(1).carList.add(car4);
		
		//String carType, String licensePlate, double carWashPrice
		Car car6 = new Car("Minibus", "EFG456H", 12.0);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash6 = new CarWash("Normal", true, car6, outletList.get(1));
		car6.services.add(wash6);
		outletList.get(1).carList.add(car6);
		
		//Woodlands Outlet
		
		//String carType, String licensePlate, double carWashPrice
		Car car8 = new Car("Minibus", "SCV9922D", 13.0);
		//String carWashType, boolean coupon, Car car, Outlet outlet
		CarWash wash8 = new CarWash("Normal", true, car8, outletList.get(2));
		car8.services.add(wash8);
		outletList.get(2).carList.add(car8);
		
		System.out.println("Sparkling Carwash Pte Ltd");
		System.out.println("*************************");
		for (Outlet outlet : outletList) {
			outlet.show();
		}
	}
}