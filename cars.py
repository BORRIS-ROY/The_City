import math

class Car:
    def __init__(self, car_id, car_type, capacity, color, initial_position, speed=50):
        """
        Represents a car with a unique ID, type, capacity, color, and initial position.
        
        :param car_id: Unique ID for the car
        :param car_type: Type of the car (e.g., Sedan, SUV, Truck)
        :param capacity: The seating capacity of the car
        :param color: The color of the car
        :param initial_position: The (x, y) starting position of the car
        :param speed: The speed of the car in pixels per second
        """
        self.car_id = car_id
        self.car_type = car_type
        self.capacity = capacity
        self.color = color
        self.current_position = initial_position  # Initial position in (x, y) format
        self.speed = speed  # Speed in pixels per second

    def __repr__(self):
        """
        Provides a readable string representation of the car.
        """
        return (f"Car(id={self.car_id}, type={self.car_type}, capacity={self.capacity}, color={self.color})")
    
    def is_suitable_for_group(self, group_size):
        """
        Checks if the car is suitable for a given group size based on capacity.
        :param group_size: The number of people in the group
        :return: True if the car's capacity is greater than or equal to the group size
        """
        return self.capacity >= group_size

    def get_size_in_cells(self):
        """
        Determines the size of the car in terms of grid cells based on the car type.
        :return: The size of the car in grid cells.
        """
        if self.car_type == "Sedan":
            return 2  # Sedans take up 2 grid cells
        elif self.car_type == "SUV":
            return 3  # SUVs take up 3 grid cells
        elif self.car_type == "Truck":
            return 4  # Trucks take up 4 grid cells
        else:
            return 2  # Default to 2 grid cells for unknown types
    
    def update_position(self, start_pos, end_pos, time_delta):
        """
        Updates the position of the car as it moves along the street.
        :param start_pos: The starting position of the car
        :param end_pos: The target position the car is moving towards
        :param time_delta: The time elapsed since the last update, for smooth movement
        """
        self.current_position = move_car_along_street(self, start_pos, end_pos, self.speed, time_delta)

# Helper function to move a car along a street
def move_car_along_street(car, start_pos, end_pos, speed, time_delta):
    """
    Moves the car along a straight line between start_pos and end_pos at a given speed.
    
    :param car: The car object (with its current position)
    :param start_pos: The (x, y) starting position of the car
    :param end_pos: The (x, y) ending position of the car (target point)
    :param speed: Speed of the car in pixels per second
    :param time_delta: The time elapsed since the last update, used for smooth movement
    :return: Updated (x, y) position of the car
    """
    car_x, car_y = car.current_position
    target_x, target_y = end_pos

    # Calculate the direction vector
    direction_x = target_x - car_x
    direction_y = target_y - car_y

    # Calculate the distance to the target point
    distance = math.sqrt(direction_x ** 2 + direction_y ** 2)

    # Normalize the direction vector
    if distance > 0:
        direction_x /= distance
        direction_y /= distance

    # Calculate the new position of the car based on speed and time elapsed
    car_x += direction_x * speed * time_delta
    car_y += direction_y * speed * time_delta

    # Update car's current position
    car.current_position = (car_x, car_y)

    return car.current_position

# Example route planning function (for driving from parking bay to street)
def get_route_from_parking_to_street(parking_bay, start_junction, end_junction, cell_size):
    """
    Generates a simple route from the parking bay to a street, keeping on the left side.
    :param parking_bay: The parking bay where the car starts
    :param start_junction: The starting junction on the street
    :param end_junction: The destination junction on the street
    :return: A list of (x, y) coordinates representing the path
    """
    # Simple example: car exits the parking bay and reaches the start_junction on the street
    route = [(parking_bay.x * cell_size, parking_bay.y * cell_size),  # Exit point from parking bay
             (start_junction.x * cell_size, start_junction.y * cell_size),  # Left side of the street (start)
             (end_junction.x * cell_size, end_junction.y * cell_size)]  # Left side of the street (end)
    return route
