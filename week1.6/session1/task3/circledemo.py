# Week 1.6, Session 1: Task 3


from point import Point
from shapes import Circle

def main():
	# Create a Circle object
	c = Circle(2.5, Point(0.0, 0.0))
	print(c)
	print(f"Area = {c.area():.3f}")
	print(f"Perimeter = {c.perimeter():.3f}")

	print("Moving the circle...")
	c.set_position(Point(1.6, 3.2))
	print(c)

	print("Changing the circle's colour...")
	c.set_colour("green")
	print(c)

if __name__ == "__main__":
	main()
