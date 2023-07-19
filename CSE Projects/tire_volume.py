import math
from datetime import datetime


width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

width = width / 25.4
aspect_ratio = aspect_ratio / 100
diameter = diameter + (width * aspect_ratio)
volume = (math.pi * (diameter / 2) ** 2) * width

with open("volume.txt", "a") as f:
    f.write("{}, {:.2f} liters\n".format(datetime.now(), volume))
print("The approximate volume is {:.2f} liters".format(volume))

buy_tires = input("Do you want to buy tires with these dimensions? (yes or no): ")
if buy_tires.lower() == "yes":
    phone_number = input("Enter your phone number: ")
    with open("volume.txt", "a") as f:
        f.write("Phone number: {}\n".format(phone_number))
        print("Thank you for your purchase! Your phone number has been stored in the volumes.txt file.")
else:
    print("Thank you for your interest. Goodbye!")
