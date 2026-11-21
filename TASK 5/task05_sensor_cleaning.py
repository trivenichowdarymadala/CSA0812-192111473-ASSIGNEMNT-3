"""Q5: Clean temperature sensor readings using three approaches."""

def valid(value):
    return -50 <= value <= 50

def loop_clean(values):
    result = []
    for value in values:
        if valid(value):
            result.append(value)
    return result

def comprehension_clean(values):
    return [value for value in values if valid(value)]

def map_filter_clean(values):
    return list(filter(lambda value: -50 <= value <= 50, values))

def convert_temperatures(celsius_values):
    fahrenheit = [c * 9 / 5 + 32 for c in celsius_values]
    alarm_minutes = [(i + 1, value) for i, value in enumerate(celsius_values)
                     if value < 2 or value > 8]
    return fahrenheit, alarm_minutes

if __name__ == "__main__":
    readings = [4.5, 6.2, 55, -60, 1.5, 9.1, 7.0, 50]
    cleaned = comprehension_clean(readings)
    f_values, alarms = convert_temperatures(cleaned)
    print("Original:", readings)
    print("Cleaned:", cleaned)
    print("Fahrenheit:", [round(x, 2) for x in f_values])
    print("Alarm minutes (minute, Celsius):", alarms)
    print("All methods agree:", loop_clean(readings) == comprehension_clean(readings) == map_filter_clean(readings))
