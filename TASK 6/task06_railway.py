"""Q6: Nested railway timetable data."""
from datetime import datetime

TRAINS = {
    "12601": {
        "name": "Chennai Express",
        "stops": [("Chennai", "06:00", "06:10"), ("Katpadi", "08:00", "08:05"),
                  ("Bengaluru", "11:00", "11:10")],
        "running_days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat"},
    },
    "12602": {
        "name": "Coastal Express",
        "stops": [("Chennai", "07:00", "07:10"), ("Villupuram", "09:00", "09:05"),
                  ("Thanjavur", "11:30", "11:40")],
        "running_days": {"Mon", "Wed", "Fri", "Sun"},
    },
    "12603": {
        "name": "Delta Express",
        "stops": [("Mayiladuthurai", "08:00", "08:05"), ("Thanjavur", "09:30", "09:35"),
                  ("Trichy", "11:00", "11:10")],
        "running_days": {"Tue", "Thu", "Sat"},
    },
    "12604": {
        "name": "City Link",
        "stops": [("Chennai", "12:00", "12:10"), ("Katpadi", "14:00", "14:05"),
                  ("Bengaluru", "17:00", "17:10")],
        "running_days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"},
    },
    "12605": {
        "name": "Southern Express",
        "stops": [("Chennai", "18:00", "18:10"), ("Villupuram", "20:00", "20:05"),
                  ("Mayiladuthurai", "22:00", "22:10")],
        "running_days": {"Tue", "Thu", "Sat", "Sun"},
    },
}

def trains_at_station(station, day, trains=TRAINS):
    matches = []
    for number, info in trains.items():
        if day in info["running_days"]:
            for stop in info["stops"]:
                if stop[0].lower() == station.lower():
                    matches.append((number, info["name"], stop[1], stop[2]))
                    break
    return sorted(matches, key=lambda item: datetime.strptime(item[2], "%H:%M"))

def build_station_index(trains=TRAINS):
    index = {}
    for number, info in trains.items():
        for station, arrival, departure in info["stops"]:
            index.setdefault(station.lower(), []).append((number, arrival, departure))
    return index

if __name__ == "__main__":
    print("Trains at Chennai on Monday:")
    for row in trains_at_station("Chennai", "Mon"):
        print(row)
    print("Station index:", build_station_index())
    print("Third station departure of 12601:", TRAINS["12601"]["stops"][2][2])
