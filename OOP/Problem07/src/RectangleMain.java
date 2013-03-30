public class RectangleMain {
	public static void main(String[] args) {
		Rectangle myWritingPad = new Rectangle(50.1, 20.2);
		System.out.println("Rectangle length is = " + myWritingPad.length);
		System.out.println("Rectangle width is = " + myWritingPad.width);
		System.out.println("Rectangle area is = " + myWritingPad.calculateArea());
		System.out.println("Box volume is = " + myWritingPad.calculateVolume(33.3));
		myWritingPad.printBoxSurfaceArea(9.8);
		System.out.println("------------------------------------------------------");
		Rectangle yourWritingPad = new Rectangle(77.2, 23.6);
		System.out.println("Rectangle length is = " + yourWritingPad.length);
		System.out.println("Rectangle width is = " + yourWritingPad.width);
		System.out.println("Rectangle area is = " + yourWritingPad.calculateArea());
		System.out.println("Box volume is = " + yourWritingPad.calculateVolume(9.8));
		yourWritingPad.printBoxSurfaceArea(33.3);
		System.out.println("------------------------------------------------------");
		Rectangle box = new Rectangle(47.1, 21.3);
		System.out.println("Box length is = " + box.length);
		System.out.println("Box width is = " + box.width);
		System.out.println("Box area is = " + box.calculateArea());
		System.out.println("Box volume is = " + box.calculateVolume(9.8));
		box.printBoxSurfaceArea(33.3);
	}
}