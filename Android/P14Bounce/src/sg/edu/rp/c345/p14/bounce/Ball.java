package sg.edu.rp.c345.p14.bounce;

import android.graphics.Paint;

public class Ball {

	// Variables
	float x; //The position of the ball in X axis
	float y; //The position of the ball in Y axis
	float radius; //The radius of the ball
	float xSpeed; //The speed of the ball horizontally
	float ySpeed; //The speed of the ball vertically
	float canvasWidth; //Width of the phone/emulator
	float canvasHeight; //Height of the phone/emulator
	Paint paint;
	int point;
	
	// Constructor
	public Ball(float x, float y, float radius, float xSpeed, float ySpeed, Paint paint) {
		super();
		this.x = x;
		this.y = y;
		this.radius = radius;
		this.xSpeed = xSpeed;
		this.ySpeed = ySpeed;
		this.paint = paint;
	}

	public void setRegion(int width, int height) {
		this.canvasWidth = width;
		this.canvasHeight = height;
	}
	
	public void update() {
		this.x = (float) (this.x + this.xSpeed);
		this.y = (float) (this.y + this.ySpeed);
		
		if ((this.x + this.radius) > this.canvasWidth) {
			this.x -= this.xSpeed;
			xSpeed = -xSpeed;
		}
		
		if ((this.x - this.radius) < 0) {
			this.x = this.radius;
			xSpeed = -xSpeed;
		}
		
		if ((this.y + this.radius) > this.canvasHeight) {
			this.y -= this.ySpeed;
			ySpeed = -ySpeed;
		}
		
		if ((this.y - this.radius) < 0) {
			this.y = this.radius;
			ySpeed = -ySpeed;
		}
	}

	public float getX() {
		return x;
	}

	public void setX(float x) {
		this.x = x;
	}

	public float getY() {
		return y;
	}

	public void setY(float y) {
		this.y = y;
	}

	public float getxSpeed() {
		return xSpeed;
	}

	public void setxSpeed(float xSpeed) {
		this.xSpeed = xSpeed;
	}

	public float getySpeed() {
		return ySpeed;
	}

	public void setySpeed(float ySpeed) {
		this.ySpeed = ySpeed;
	}

	public float getRadius() {
		return radius;
	}

	public void setRadius(int radius) {
		this.radius = radius;
	}

	public Paint getPaint() {
		return paint;
	}

	public void setPaint(Paint paint) {
		this.paint = paint;
	}
	
	public int getPoint() {
		return point;
	}

	public void setPoint(int point) {
		this.point = point;
	}
}
