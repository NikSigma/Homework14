def describe_trip(destination, duration, transport= "car"):
    print(f"Traveling to {destination} for {duration} days by {transport}.")

describe_trip("Kyiv", 7, "plane")
describe_trip("Xmelnyckiy", 4, "train")
describe_trip("Ivano-Frankivsk", 5, "car")
describe_trip("Lviv", 3, "bus")
