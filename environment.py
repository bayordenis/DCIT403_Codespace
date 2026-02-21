import random
import datetime

class DisasterEnvironment:
    """
    Simulated disaster environment for the Disaster Response
    and Relief Coordination System.
    """

    def __init__(self):
        # Possible disaster types
        self.disaster_types = [
            "Flood",
            "Earthquake",
            "Fire",
            "Landslide"
        ]

        # Possible affected locations
        self.locations = [
            "North Zone",
            "South Zone",
            "East Zone",
            "West Zone"
        ]

    def generate_event(self):
        """
        Generates a random disaster event with severity.
        Returns:
            dict: disaster event details
        """
        disaster_type = random.choice(self.disaster_types)
        location = random.choice(self.locations)
        severity = random.randint(1, 10)  # 1 = low, 10 = extreme

        event = {
            "type": disaster_type,
            "location": location,
            "severity": severity,
            "timestamp": datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        return event