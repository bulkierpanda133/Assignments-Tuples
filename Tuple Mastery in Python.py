#Task 1: Formatting Flight Itineraries
def format_flight_itineraries(itineraries):
    formatted_itineraries = []
    
    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        formatted_itinerary = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(formatted_itinerary)

    return "\n".join(formatted_itineraries)


itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
output = format_flight_itineraries(itineraries)
print(output)
