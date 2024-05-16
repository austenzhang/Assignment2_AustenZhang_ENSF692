# input_processing.py
# Austen Zhang, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

# Creating class Sensor
class Sensor:

    # Creating default constructor. Setting its values to green traffic light, no pedestrian, no vehicle. No other constructor is created as it is not required for this program.
    def __init__(self):
        self.traffic_light_colour = 'green'
        self.pedestrian = 'no'
        self.vehicle = 'no'
        
    # Update Status takes the option and selection determined in the main method and adjust instance variables to match.
    def update_status(self, option, selection):
        if option == 1: # if option selected is traffic light, set traffic light to specified colour
            self.traffic_light_colour = selection
        elif option == 2: # if option selected is pedestrian, set pedestrian to specified state, yes or no.
            self.pedestrian = selection
        elif option == 3: # if option selected is vehicle, set pedestrian to specified state, yes or no.
            self.vehicle = selection
            


# Print Message function takes an argument, which is the sensor object. It uses the instance variables in the object to determine what message to print.
def print_message(sensor):
    # Series of if, elif, else, nested if/elif statements to determine what message to print.
    # Start with traffic light being red.
    if sensor.traffic_light_colour == 'red': # if traffic light is red, print Stop.
        print("\nSTOP")
    elif sensor.traffic_light_colour == 'green': # if traffic light is green, need to look at pedestrian.
        if sensor.pedestrian == 'yes': # if there is pedestrian, need to print stop.
            print("\nSTOP")
        elif sensor.pedestrian == 'no': # if there is no pedestrian, need to check vehicle
            if sensor.vehicle == 'yes': # if there is vehicle, need to print stop.
                print("\nSTOP")
            elif sensor.vehicle == 'no': # if there is no vehicle, then can proceed.
                print("\nProceed")
    elif sensor.traffic_light_colour == 'yellow': # similar to green light, if light is yellow, need to check pedestrian.
        if sensor.pedestrian == 'yes': # if there is pedestrian, need to print stop.
            print("\nSTOP")
        elif sensor.pedestrian == 'no': # if there is no pedestrian, need to check vehicle.
            if sensor.vehicle == 'yes': # if there is vehicle, need to  print stop.
                print("\nSTOP")
            elif sensor.vehicle == 'no': # if there is no vehicle, print caution as it is a yellow light.
                print("\nCaution")
    print(f"\nLight = {sensor.traffic_light_colour}, Pedestrian = {sensor.pedestrian}, Vehicle = {sensor.vehicle}.\n") #Printing values of current instance variables in sensor.   


# Main function, this is the function that will be called when the program starts.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n") # Printing title of program
    sensor = Sensor() #Creating new sensor object
    
    while True:
        option = int(input("Are changes detected in the vision input?\nSelect 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program. ")) # Obtaining input from user on which variable to change.
        if not(option == 0 or option == 1 or option == 2 or option == 3): # checking if input is valid
            print("Invalid input. You must select either 1, 2, 3 or 0") # if not valid, print this message. Loop should restart from beginning after printing current variable and current recommendation. QUESTION: Not raising ValueError exactly. How do I raise it without it terminating the program?
        elif option == 0: # if option is 0, exit while loop.
            break
        else:
            if option == 1: # if option is 1, ask for light selection input
                light_selection = input("What change has been identified? ")
                if not(light_selection == 'green' or light_selection == 'yellow' or light_selection == 'red'): # check if light selection is valid (i.e. red, green or yellow)
                    print("Invalid vision change. Value must be green, yellow, or red") # if input is not valid, print this message
                else:
                    sensor.update_status(option, light_selection) # if input is valid, update sensor object variable to match new light colour.
            elif option == 2: # if option is 2, ask for pedestrian selection, yes or no
                pedestrian_selection = input("What change has been identified? ")
                if not(pedestrian_selection == 'yes' or pedestrian_selection == 'no'): # check if pedestrian selection is valid (i.e. yes or no)
                    print("Invalid vision change. Value must be yes or no") # if input is not valid, print this message
                else:
                    sensor.update_status(option, pedestrian_selection) # if input is valid, update sensor object variable to match new pedestrian selection.
            elif option == 3:
                vehicle_selection = input("What change has been identified? ")
                if not(vehicle_selection == 'yes' or vehicle_selection == 'no'): # check if vehicle selection is valid (i.e. yes or no)
                    print("Invalid vision change. Value must be yes or no") # if input is not valid, print this message
                else:
                    sensor.update_status(option, vehicle_selection) # if input is valid, update sensor object variable to match new vehicle selection.
        print_message(sensor) # Call print message function to display current recommendation and current variables in the sensor object.

        





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

