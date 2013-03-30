public class Rectangle {
	public double length;
	public double width;
	
	//constructor
	public Rectangle(double len, double wid) {
	length = len;
	width = wid;
	}
	
	public double calculateArea() {
		double area =  length * width;
		return area;
	}
	
	public double calculatePerimeter(){
		double perimeter = 2*(length + width);
		return perimeter;
	}
	
	public double calculateVolume(double height) {
		double volume = length * width * height ;
		return volume;
	}
	
	public void printBoxSurfaceArea(double height) {
		//Surface Area of a Rectangular Prism = 2wl + 2wh + 2hl
		double surfaceArea = (2*(width*length)) + (2*(width*height)) + (2*(height*length)) ;
		System.out.println("Box Surface Area is = " + surfaceArea);
	}
}
