# Water Notification System

# importing modules
from plyer import notification
import time

# only applicable under this function
if __name__ == '__main__':
    # while loop to continue
    while True:
        # notification syntax
        notification.notify(
            title = " Hey Majed! Please Drink Water Now",
            message = "An adequate daily fluid intake is: " \
                      "About 15.5 cups (3.7 liters) of fluids for men." \
                      "About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon ="Gallery/water.ico",
            timeout = 10
        )
        time.sleep(6)
