package sg.edu.rp.c345.p06.worldofshoes;

public class Shoe {
	//Attributes
	String ShoeModel;
	String ShoeModelNo;
	double Price;
	String Address;
	String url;
	String email;
	int phoneNumber;
	double openingHrs;
	double closingHrs;
	
	//Constructor
	public Shoe(String shoeModel, String shoeModelNo, double price,
			String address, String url, String email, int phoneNumber,
			double openingHrs, double closingHrs) {
		super();
		ShoeModel = shoeModel;
		ShoeModelNo = shoeModelNo;
		Price = price;
		Address = address;
		this.url = url;
		this.email = email;
		this.phoneNumber = phoneNumber;
		this.openingHrs = openingHrs;
		this.closingHrs = closingHrs;
	}

	//Getters/Setters/toString!
	public String getShoeModel() {
		return ShoeModel;
	}

	public String getShoeModelNo() {
		return ShoeModelNo;
	}

	public double getPrice() {
		return Price;
	}

	public String getAddress() {
		return Address;
	}

	public String getUrl() {
		return url;
	}

	public String getEmail() {
		return email;
	}

	public int getPhoneNumber() {
		return phoneNumber;
	}

	public double getOpeningHrs() {
		return openingHrs;
	}

	public double getClosingHrs() {
		return closingHrs;
	}

	@Override
	public String toString() {
		return "Shoe [Address=" + Address + ", Price=" + Price + ", ShoeModel="
				+ ShoeModel + ", ShoeModelNo=" + ShoeModelNo + ", closingHrs="
				+ closingHrs + ", email=" + email + ", openingHrs="
				+ openingHrs + ", phoneNumber=" + phoneNumber + ", url=" + url
				+ "]";
	}
}
