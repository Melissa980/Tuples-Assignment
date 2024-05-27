# Question 1 Task 1 

def format_itineraries(itineraries):
    result = ""
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        result += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return result.strip()  # Remove trailing newline

# Example usage
flight_info = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted = format_itineraries(flight_info)
print(formatted)
