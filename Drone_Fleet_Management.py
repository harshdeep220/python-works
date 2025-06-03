class device:
    def __init__(self):
        self.device_info= "The device has GPS, Camera, and Sensors."

    def Show_device(self):
        print(self.device_info)

class flyer:
    def fly(self):
        print("The drone is flying.")

class Drone(device, flyer):
    def __init__(self):
        device.__init__(self)
        flyer.__init__(self)

    def capture_image(self):
        print("Drone Captured an Image")

my_drone = Drone()
my_drone.Show_device()
my_drone.fly()
my_drone.capture_image()
