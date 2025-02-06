import pygame
import sys
import networks
import cars

# Initialize pygame
pygame.init()

# Define initial grid properties
GRID_SIZE = 100  # Number of cells (100x100 grid)
initial_window_size = (600, 600)  # Initial window size

# Set up the display with resizable mode
screen = pygame.display.set_mode(initial_window_size, pygame.RESIZABLE)
pygame.display.set_caption("Responsive Grid - Streets and Junctions")

# Define junctions
junction_1 = networks.Junctions(1, 0, 0, 2, 2)
junction_2 = networks.Junctions(2, 50, 0, 2, 2)
junction_3 = networks.Junctions(3, 70, 0, 2, 2)
junction_4 = networks.Junctions(4, 100, 0, 2, 2)
junction_5 = networks.Junctions(5, 0, 20, 2, 2)
junction_6 = networks.Junctions(6, 50, 20, 2, 2)
junction_14 = networks.Junctions(14, 38, 38, 2, 2)
junction_15 = networks.Junctions(15, 62, 38, 2, 2)
junction_16 = networks.Junctions(16, 38, 62, 2, 2)
junction_17 = networks.Junctions(17, 62, 62, 2, 2)
junction_19 = networks.Junctions(19, 50, 38, 2, 2)
junction_20 = networks.Junctions(20, 50, 62, 2, 2)
junction_21 = networks.Junctions(21, 50, 50, 2, 2)
junction_22 = networks.Junctions(22, 0, 50, 2, 2)
junction_23 = networks.Junctions(23, 100, 50, 2, 2)
junction_24 = networks.Junctions(24, 38, 50, 2, 2)
junction_25 = networks.Junctions(25, 62, 50, 2, 2)
# y = 100 junctions
junction_18 = networks.Junctions(18, 50, 100, 2, 2)
junction_26 = networks.Junctions(26, 0, 100, 2, 2)
junction_27 = networks.Junctions(27, 25, 100, 2, 2)
junction_28 = networks.Junctions(28, 75, 100, 2, 2)
junction_29 = networks.Junctions(29, 100, 100, 2, 2)
# second last horizontal junctions 
junction_30 = networks.Junctions(30, 35, 90, 2, 2)
junction_31 = networks.Junctions(31, 65, 90, 2, 2)
junction_32 = networks.Junctions(32, 15, 70, 2, 2)
junction_33 = networks.Junctions(33, 15, 50, 2, 2)
junction_34 = networks.Junctions(34, 15, 20, 2, 2)
# x = 85 junctions
junction_35 = networks.Junctions(35, 85, 20, 2, 2)
junction_36 = networks.Junctions(36, 85, 50, 2, 2)
junction_37 = networks.Junctions(37, 85, 70, 2, 2)


juncts = [junction_1, junction_2, junction_3, junction_4, junction_5, junction_6, 
          junction_14, junction_15, junction_16, junction_17, junction_18, junction_19,
          junction_20, junction_21, junction_22, junction_23, junction_24, junction_25,
          junction_26, junction_27, junction_28, junction_29, junction_30, junction_31, 
          junction_32, junction_33, junction_34, junction_35, junction_36, junction_37]

# Define streets
street_1 = networks.Streets(1, junction_1, junction_2)
street_2 = networks.Streets(2, junction_2, junction_3)
street_3 = networks.Streets(3, junction_3, junction_4)
street_4 = networks.Streets(4, junction_2, junction_6)
street_5 = networks.Streets(5, junction_6, junction_19)
street_6 = networks.Streets(6, junction_20, junction_18)
street_7 = networks.Streets(7, junction_14, junction_15)
street_8 = networks.Streets(8, junction_14, junction_16)
street_9 = networks.Streets(9, junction_15, junction_17)
street_10 = networks.Streets(10, junction_14, junction_19)
street_11 = networks.Streets(11, junction_15, junction_19)
street_12 = networks.Streets(12, junction_16, junction_20)
street_13 = networks.Streets(13, junction_17, junction_20)
street_14 = networks.Streets(14, junction_19, junction_21)
street_15 = networks.Streets(15, junction_20, junction_21)
street_16 = networks.Streets(16, junction_21, junction_24)
street_17 = networks.Streets(17, junction_21, junction_25)
street_18 = networks.Streets(18, junction_22, junction_24)
street_19 = networks.Streets(19, junction_23, junction_25)
street_20 = networks.Streets(20, junction_18, junction_27)
street_24 = networks.Streets(24, junction_18, junction_28)
street_25 = networks.Streets(25, junction_29, junction_17)
street_26 = networks.Streets(26, junction_21, junction_17)
street_27 = networks.Streets(27, junction_29, junction_17)
# junctionn x = 0 streets
street_21 = networks.Streets(21, junction_26, junction_22)
street_22 = networks.Streets(22, junction_22, junction_5)
street_23 = networks.Streets(23, junction_5, junction_1)

# ring road
street_28 = networks.Streets(28, junction_34, junction_33)
street_29 = networks.Streets(29, junction_33, junction_32)
street_30 = networks.Streets(30, junction_32, junction_30)
street_31 = networks.Streets(31, junction_30, junction_31)
street_32 = networks.Streets(32, junction_31, junction_37)
street_33 = networks.Streets(33, junction_37, junction_36)
street_34 = networks.Streets(34, junction_36, junction_35)
# more streets
street_35 = networks.Streets(35, junction_35, junction_3)
street_36 = networks.Streets(36, junction_4, junction_23)
street_37 = networks.Streets(37, junction_34, junction_5)
street_38 = networks.Streets(38, junction_35, junction_6)
street_39 = networks.Streets(39, junction_23, junction_36)
street_40 = networks.Streets(40, junction_32, junction_16)
street_41 = networks.Streets(41, junction_34, junction_14)
street_42 = networks.Streets(42, junction_35, junction_15)


strts = [street_1, street_2, street_3, street_4, street_5, street_6, street_7, street_8, 
         street_9, street_10, street_11, street_12, street_13, street_14, street_15, street_16,
         street_17, street_18, street_19, street_20, street_21, street_22, street_23, street_24, 
         street_25, street_28, street_29, street_30, street_31, street_32, street_33, street_34, 
         street_35, street_36, street_37, street_38, street_39, street_40, street_41, street_42]

# Define train junctions
train_junction_1 = networks.TrainJunctions(101, 10, 10, 2, 2)
train_junction_2 = networks.TrainJunctions(102, 40, 10, 2, 2)
train_junction_3 = networks.TrainJunctions(103, 70, 10, 2, 2)
train_junction_4 = networks.TrainJunctions(104, 90, 10, 2, 2)
train_junction_5 = networks.TrainJunctions(105, 90, 40, 2, 2)
train_junction_6 = networks.TrainJunctions(106, 70, 40, 2, 2)
train_junction_7 = networks.TrainJunctions(107, 70, 60, 2, 2)
train_junction_8 = networks.TrainJunctions(108, 70, 80, 2, 2)
train_junction_9 = networks.TrainJunctions(109, 48, 80, 2, 2)
train_junction_10 = networks.TrainJunctions(110, 20, 80, 2, 2)
train_junction_11 = networks.TrainJunctions(111, 2, 98, 2, 2)

train_juncts1 = [train_junction_1, train_junction_2, train_junction_3, train_junction_4, 
                train_junction_5, train_junction_6, train_junction_7, train_junction_8, 
                train_junction_9, train_junction_10, train_junction_11]

# Train junctions 2
train_junction_201 = networks.TrainJunctions(101, 90, 52, 2, 2)
train_junction_202 = networks.TrainJunctions(102, 90, 95, 2, 2)
train_junction_203 = networks.TrainJunctions(103, 60, 95, 2, 2)
train_junction_204 = networks.TrainJunctions(104, 10, 95, 2, 2)
train_junction_205 = networks.TrainJunctions(105, 10, 60, 2, 2)
train_junction_206 = networks.TrainJunctions(106, 35, 60, 2, 2)
train_junction_207 = networks.TrainJunctions(107, 35, 40, 2, 2)
train_junction_208 = networks.TrainJunctions(108, 5, 40, 2, 2)
train_junction_209 = networks.TrainJunctions(109, 5, 5, 2, 2)
train_junction_210 = networks.TrainJunctions(110, 30, 5, 2, 2)
train_junction_211 = networks.TrainJunctions(111, 2, 98, 2, 2)

train_juncts2 = [train_junction_201, train_junction_202, train_junction_203, train_junction_204, 
                 train_junction_205, train_junction_206, train_junction_207, train_junction_208, 
                 train_junction_209, train_junction_210]

train_junction_301 = networks.TrainJunctions(301, 56, 2, 2, 2)
train_junction_302 = networks.TrainJunctions(302, 56, 30, 2, 2)
train_junction_303 = networks.TrainJunctions(303, 56, 40, 2, 2)
train_junction_304 = networks.TrainJunctions(304, 46, 40, 2, 2)
train_junction_305 = networks.TrainJunctions(305, 46, 60, 2, 2)
train_junction_306 = networks.TrainJunctions(306, 46, 70, 2, 2)
train_junction_307 = networks.TrainJunctions(307, 56, 70, 2, 2)
train_junction_308 = networks.TrainJunctions(308, 56, 90, 2, 2)
train_junction_309 = networks.TrainJunctions(309, 5, 5, 2, 2)
train_junction_310 = networks.TrainJunctions(310, 30, 5, 2, 2)
train_junction_311 = networks.TrainJunctions(311, 2, 98, 2, 2)

train_juncts3 = [train_junction_301, train_junction_302, train_junction_303, train_junction_304, 
                 train_junction_305, train_junction_306, train_junction_307, train_junction_308]

# Define train streets connecting the junctions
train_street_1 = networks.TrainStreets(201, train_junction_1, train_junction_2)
train_street_2 = networks.TrainStreets(202, train_junction_2, train_junction_3)
train_street_3 = networks.TrainStreets(203, train_junction_3, train_junction_4)
train_street_4 = networks.TrainStreets(204, train_junction_4, train_junction_5)
train_street_5 = networks.TrainStreets(205, train_junction_5, train_junction_6)
train_street_6 = networks.TrainStreets(206, train_junction_6, train_junction_7)
train_street_7 = networks.TrainStreets(207, train_junction_7, train_junction_8)
train_street_8 = networks.TrainStreets(208, train_junction_8, train_junction_9)
train_street_9 = networks.TrainStreets(209, train_junction_9, train_junction_10)
train_street_10 = networks.TrainStreets(210, train_junction_10, train_junction_11)

train_strts = [train_street_1, train_street_2, train_street_3, train_street_4, train_street_5, 
               train_street_6, train_street_7, train_street_8, train_street_9, train_street_10]

# train streets line 2
train_street_201 = networks.TrainStreets(201, train_junction_201, train_junction_202)
train_street_202 = networks.TrainStreets(202, train_junction_202, train_junction_203)
train_street_203 = networks.TrainStreets(203, train_junction_203, train_junction_204)
train_street_204 = networks.TrainStreets(204, train_junction_204, train_junction_205)
train_street_205 = networks.TrainStreets(205, train_junction_205, train_junction_206)
train_street_206 = networks.TrainStreets(206, train_junction_206, train_junction_207)
train_street_207 = networks.TrainStreets(207, train_junction_207, train_junction_208)
train_street_208 = networks.TrainStreets(208, train_junction_208, train_junction_209)
train_street_209 = networks.TrainStreets(209, train_junction_209, train_junction_210)

train_strts2 = [train_street_201, train_street_202, train_street_203, train_street_204, train_street_205, 
                train_street_206, train_street_207, train_street_208, train_street_209]

# train streets line 3
train_street_301 = networks.TrainStreets(201, train_junction_301, train_junction_302)
train_street_302 = networks.TrainStreets(202, train_junction_302, train_junction_303)
train_street_303 = networks.TrainStreets(203, train_junction_303, train_junction_304)
train_street_304 = networks.TrainStreets(204, train_junction_304, train_junction_305)
train_street_305 = networks.TrainStreets(205, train_junction_305, train_junction_306)
train_street_306 = networks.TrainStreets(206, train_junction_306, train_junction_307)
train_street_307 = networks.TrainStreets(207, train_junction_307, train_junction_308)

train_strts3 = [train_street_301, train_street_302, train_street_303, train_street_304, train_street_305, 
                train_street_306, train_street_307]

# Define parking bays
parking_bay_1 = networks.ParkingBay(1, 10, 22, 5, 10)
parking_bay_2 = networks.ParkingBay(2, 52, 52, 6, 10)
parking_bay_3 = networks.ParkingBay(3, 92, 52, 6, 10)
parking_bay_4 = networks.ParkingBay(4, 52, 52, 6, 10)
parking_bay_5 = networks.ParkingBay(5, 52, 52, 6, 10)
parking_bay_6 = networks.ParkingBay(6, 52, 52, 6, 10)

parking_bays = [parking_bay_1, parking_bay_2, parking_bay_3]


# Create cars
car_1 = cars.Car(car_id=1, car_type="Sedan", capacity=4, color="red", initial_position=(parking_bay_1.x * cell_size, parking_bay_1.y * cell_size))
car_2 = cars.Car(car_id=2, car_type="SUV", capacity=6, color="blue", initial_position=(parking_bay_1.x * cell_size, parking_bay_1.y * cell_size))
car_3 = cars.Car(car_id=3, car_type="Truck", capacity=2, color="green", initial_position=(parking_bay_2.x * cell_size, parking_bay_2.y * cell_size))
car_4 = cars.Car(car_id=4, car_type="Sedan", capacity=4, color="yellow", initial_position=(parking_bay_2.x * cell_size, parking_bay_2.y * cell_size))

# Add cars to the parking bays
parking_bay_1.add_car(car_1)
parking_bay_1.add_car(car_2)
parking_bay_2.add_car(car_3)
parking_bay_2.add_car(car_4)



# Define colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # Color for train lines
GREEN = (0, 255, 0)  # Color for parking bays
RED = (255, 0, 0),    # Red
YELLOW = (255, 255, 0),  # Yellow
ORANGE = (255, 165, 0),  # Orange
PURPLE = (128, 0, 128),  # Purple
CYAN = (0, 255, 255),  # Cyan
PINK = (255, 20, 147)  # Pink

# Function to calculate cell size based on window size and maintain aspect ratio
def calculate_cell_size(window_size, grid_size):
    # Use the smaller of the window's width and height divided by the number of grid cells
    return min(window_size[0] // grid_size, window_size[1] // grid_size)

# Function to draw junctions
def draw_junctions(screen, junctions, cell_size):
    for junction in junctions:
        rect = pygame.Rect(junction.x * cell_size, junction.y * cell_size,
                           junction.width * cell_size, junction.height * cell_size)
        pygame.draw.rect(screen, GREY, rect)

# Updated function to draw streets with the same width as junctions
def draw_streets(screen, streets, cell_size):
    for street in streets:
        start_junction = street.start_junction
        end_junction = street.end_junction

        # Calculate the center of the start and end junctions
        start_center_x = (start_junction.x + start_junction.width / 2) * cell_size
        start_center_y = (start_junction.y + start_junction.height / 2) * cell_size
        end_center_x = (end_junction.x + end_junction.width / 2) * cell_size
        end_center_y = (end_junction.y + end_junction.height / 2) * cell_size

        # Use the width of the start junction to determine the street width (in pixels)
        street_width = int(start_junction.width * cell_size)

        # Draw the street as a line between the junctions with the specified width
        pygame.draw.line(screen, GREY, (start_center_x, start_center_y), (end_center_x, end_center_y), street_width)

# Function to draw train junctions
def draw_train_junctions(screen, junctions, cell_size, color=BLUE):
    for junction in junctions:
        rect = pygame.Rect(junction.x * cell_size, junction.y * cell_size,
                           junction.width * cell_size, junction.height * cell_size)
        pygame.draw.rect(screen, color, rect)

# Function to draw train streets
def draw_train_streets(screen, streets, cell_size, color=BLUE):
    for street in streets:
        start_junction = street.start_junction
        end_junction = street.end_junction

        # Calculate the center of the start and end junctions
        start_center_x = (start_junction.x + start_junction.width / 2) * cell_size
        start_center_y = (start_junction.y + start_junction.height / 2) * cell_size
        end_center_x = (end_junction.x + end_junction.width / 2) * cell_size
        end_center_y = (end_junction.y + end_junction.height / 2) * cell_size

        # Draw the train street as a line between the junctions
        pygame.draw.line(screen, color, (start_center_x, start_center_y), (end_center_x, end_center_y), 3)

# Function to draw parking bays
def draw_parking_bays(screen, parking_bays, cell_size, color=GREEN):
    for bay in parking_bays:
        rect = pygame.Rect(bay.x * cell_size, bay.y * cell_size,
                           bay.width * cell_size, bay.height * cell_size)
        pygame.draw.rect(screen, color, rect)
        
def draw_cars_in_parking_bay(screen, parking_bays, cell_size):
    for bay in parking_bays:
        for i, car in enumerate(bay.cars):
            # Calculate car size in cells based on its type
            car_size_in_cells = car.get_size_in_cells()
            
            # Calculate the car's position within the parking bay
            car_x = (bay.x + (i % (bay.width // car_size_in_cells))) * cell_size
            car_y = (bay.y + (i // (bay.width // car_size_in_cells))) * cell_size

            # Calculate the car's width and height in pixels based on cell size
            car_width = car_size_in_cells * cell_size
            car_height = car_width // 2  # Keep the car's aspect ratio (width:height = 2:1)

            # Draw the car as a rectangle
            car_color = pygame.Color(car.color)
            pygame.draw.rect(screen, car_color, pygame.Rect(car_x, car_y, car_width, car_height))


# Main loop
running = True
window_size = initial_window_size
cell_size = calculate_cell_size(window_size, GRID_SIZE)

# Define a route from the parking bay to the street
route = cars.get_route_from_parking_to_street(parking_bay_1, junction_1, junction_2, cell_size)

# Variables for car movement
current_route_index = 0  # Index of the current target in the route

clock = pygame.time.Clock()
while running:
    
    time_delta = clock.tick(60) / 1000.0  # Time elapsed since the last frame, in seconds
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle window resize event
        if event.type == pygame.VIDEORESIZE:
            window_size = event.size
            screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)
            cell_size = calculate_cell_size(window_size, GRID_SIZE)

    # Fill the screen with white background
    screen.fill(WHITE)
    
    # Draw train streets and junctions
    draw_train_streets(screen, train_strts, cell_size, BLUE)
    draw_train_junctions(screen, train_juncts1, cell_size, BLUE)
    draw_train_streets(screen, train_strts2, cell_size, PURPLE)
    draw_train_junctions(screen, train_juncts2, cell_size, PURPLE)
    draw_train_streets(screen, train_strts3, cell_size, CYAN)
    draw_train_junctions(screen, train_juncts3, cell_size, CYAN)

    # Draw streets and junctions
    draw_streets(screen, strts, cell_size)
    draw_junctions(screen, juncts, cell_size)
    
    draw_parking_bays(screen, parking_bays, cell_size, GREY)
    
    # Draw cars in the parking bays
    draw_cars_in_parking_bay(screen, parking_bays, cell_size)
    

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
