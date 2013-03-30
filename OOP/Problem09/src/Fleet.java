public class Fleet {
	// data
	Car town;
	Car suv;

	// constructor
	Fleet(int start1, int end1, double gal1, int start2, int end2, double gal2) {
		town = new Car(start1, end1, gal1);
		suv = new Car(start2, end2, gal2);
	}

	// method
	double calculateMPG() {
		double sumMPG;

		sumMPG = town.calculateMPG() + suv.calculateMPG();

		return sumMPG / 2.0;
	}

	void fillUp(int townOdo, double townGal, int suvOdo, double suvGal) {

		town.fillUp(townOdo, townGal);

		suv.fillUp(suvOdo, suvGal);
	}
}