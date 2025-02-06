# networks.py

# networks.py

class Junctions:
    def __init__(self, junction_id, x, y, width, height):
        """
        Represents a junction with an ID and a rectangular area on the grid.
        The area must be at least 2 grid positions (width * height >= 2) and 
        at most 4 grid positions (width * height <= 4).

        :param junction_id: Unique ID for the junction
        :param x: The x-coordinate of the top-left corner of the junction
        :param y: The y-coordinate of the top-left corner of the junction
        :param width: The width of the junction (number of grid cells horizontally)
        :param height: The height of the junction (number of grid cells vertically)
        """
        self.junction_id = junction_id

        # Validate the junction size
        if not (2 <= width * height <= 4):
            raise ValueError("Junction must be between 2 and 4 grid positions in size.")

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return (f"Junction(id={self.junction_id}, "
                f"x={self.x}, y={self.y}, width={self.width}, height={self.height})")

    def area(self):
        """
        Returns the area of the junction in grid positions.
        """
        return self.width * self.height



class Streets:
    def __init__(self, street_id, start_junction, end_junction):
        """
        Represents a street connecting two junctions.
        :param street_id: Unique ID for the street
        :param start_junction: The starting junction (instance of Junctions)
        :param end_junction: The ending junction (instance of Junctions)
        """
        self.street_id = street_id
        self.start_junction = start_junction
        self.end_junction = end_junction

    def __repr__(self):
        return (f"Street(id={self.street_id}, "
                f"start={self.start_junction.junction_id}, "
                f"end={self.end_junction.junction_id})")

    def street_length(self):
        """
        Calculates the length of the street using Euclidean distance.
        """
        return ((self.start_junction.x - self.end_junction.x) ** 2 + 
                (self.start_junction.y - self.end_junction.y) ** 2) ** 0.5

class TrainLines:
    def __init__(self, line_id):
        """
        Represents a train line consisting of multiple streets and junctions.
        
        :param line_id: Unique identifier for the train line.
        """
        self.line_id = line_id
        self.streets = []
        self.junctions = []

    def add_street(self, street):
        """
        Adds a street to the train line. Streets should be in sequential order
        (i.e., the end junction of one street should be the start junction of the next).
        
        :param street: An instance of the Street class to add to the train line.
        """
        # Ensure the new street is connected to the previous junction (if any)
        if self.streets and self.streets[-1].end_junction != street.start_junction:
            raise ValueError("The street is not connected to the previous street.")
        
        self.streets.append(street)
        
        # Add junctions (avoid duplicates)
        if not self.junctions:
            self.junctions.append(street.start_junction)
        self.junctions.append(street.end_junction)

    def get_total_length(self):
        """
        Calculate the total length of the train line (sum of all street lengths).
        
        :return: The total length of the streets on the train line.
        """
        return sum(street.street_length() for street in self.streets)

    def get_streets(self):
        """
        Get all the streets in the train line.
        
        :return: A list of all streets in the train line.
        """
        return self.streets

    def get_junctions(self):
        """
        Get all the junctions in the train line.
        
        :return: A list of all junctions in the train line.
        """
        return self.junctions

    def __repr__(self):
        return (f"TrainLine(id={self.line_id}, "
                f"streets={len(self.streets)}, junctions={len(self.junctions)})")
    
class TrainJunctions:
    def __init__(self, junction_id, x, y, width, height):
        """
        Represents a train-specific junction, similar to regular junctions, but distinct for the train network.
        """
        self.junction_id = junction_id

        # Validate the junction size for the train
        if not (2 <= width * height <= 4):
            raise ValueError("Train Junction must be between 2 and 4 grid positions in size.")

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __repr__(self):
        return (f"TrainJunction(id={self.junction_id}, "
                f"x={self.x}, y={self.y}, width={self.width}, height={self.height})")

    def area(self):
        """
        Returns the area of the train junction in grid positions.
        """
        return self.width * self.height


class TrainStreets:
    def __init__(self, street_id, start_junction, end_junction):
        """
        Represents a street connecting two train junctions.
        :param street_id: Unique ID for the train street
        :param start_junction: The starting train junction (instance of TrainJunctions)
        :param end_junction: The ending train junction (instance of TrainJunctions)
        """
        self.street_id = street_id
        self.start_junction = start_junction
        self.end_junction = end_junction

    def __repr__(self):
        return (f"TrainStreet(id={self.street_id}, "
                f"start={self.start_junction.junction_id}, "
                f"end={self.end_junction.junction_id})")

    def street_length(self):
        """
        Calculates the length of the train street using Euclidean distance.
        """
        return ((self.start_junction.x - self.end_junction.x) ** 2 + 
                (self.start_junction.y - self.end_junction.y) ** 2) ** 0.5


class TrainLines:
    def __init__(self, line_id):
        """
        Represents a train line consisting of multiple train streets and junctions.
        
        :param line_id: Unique identifier for the train line.
        """
        self.line_id = line_id
        self.train_streets = []
        self.train_junctions = []

    def add_street(self, street):
        """
        Adds a train street to the train line. Streets should be in sequential order
        (i.e., the end junction of one street should be the start junction of the next).
        
        :param street: An instance of the TrainStreet class to add to the train line.
        """
        # Ensure the new street is connected to the previous junction (if any)
        if self.train_streets and self.train_streets[-1].end_junction != street.start_junction:
            raise ValueError("The train street is not connected to the previous train street.")
        
        self.train_streets.append(street)
        
        # Add train junctions (avoid duplicates)
        if not self.train_junctions:
            self.train_junctions.append(street.start_junction)
        self.train_junctions.append(street.end_junction)

    def get_total_length(self):
        """
        Calculate the total length of the train line (sum of all train street lengths).
        
        :return: The total length of the train streets on the train line.
        """
        return sum(street.street_length() for street in self.train_streets)

    def get_streets(self):
        """
        Get all the train streets in the train line.
        
        :return: A list of all train streets in the train line.
        """
        return self.train_streets

    def get_junctions(self):
        """
        Get all the train junctions in the train line.
        
        :return: A list of all train junctions in the train line.
        """
        return self.train_junctions

    def __repr__(self):
        return (f"TrainLine(id={self.line_id}, "
                f"train_streets={len(self.train_streets)}, train_junctions={len(self.train_junctions)})")

class ParkingBay:
    def __init__(self, bay_id, x, y, width, height):
        """
        Represents a Parking Bay on the grid.
        
        :param bay_id: Unique ID for the parking bay
        :param x: The x-coordinate of the top-left corner of the parking bay
        :param y: The y-coordinate of the top-left corner of the parking bay
        :param width: The width of the parking bay (number of grid cells horizontally)
        :param height: The height of the parking bay (number of grid cells vertically)
        """
        self.bay_id = bay_id

        # Validate the parking bay size
        if width < 4:
            raise ValueError("Parking bay width must be at least 4 grid positions.")
        if height < 8:
            raise ValueError("Parking bay height must be at least 8 grid positions.")
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cars = []  # List to hold cars in the parking bay

    def add_car(self, car):
        """
        Adds a car to the parking bay.
        :param car: An instance of the Car class.
        """
        self.cars.append(car)

    def __repr__(self):
        return (f"ParkingBay(id={self.bay_id}, x={self.x}, y={self.y}, "
                f"width={self.width}, height={self.height})")

    def area(self):
        """
        Returns the area of the parking bay in grid positions.
        """
        return self.width * self.height

