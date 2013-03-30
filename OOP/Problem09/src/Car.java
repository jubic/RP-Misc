public class Car {
	// data
	int startMiles; // Starting odometer reading
	int endMiles; // Ending odometer reading
	double gallons; // Gallons of gas used between the readings

	// constructor
	Car(int first, int last, double gals) {
		startMiles = first;
		endMiles = last;
		gallons = gals;
	}

	// methods
	double calculateMPG() {
		return (endMiles - startMiles) / gallons;
	}

	void fillUp(int newOdo, double fillUpGals) {
		startMiles = endMiles;
		endMiles = newOdo;
		gallons = fillUpGals;
	}
}