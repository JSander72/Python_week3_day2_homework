
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes & competitor_routes

unique_to_our_airline = our_routes - competitor_routes

all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}
neither_shared_destinations = all_possible_destinations - (our_routes | competitor_routes)

print(f"Common Destinations: {common_destinations}")
print(f"Unique to Our Airline: {unique_to_our_airline}")
print(f"Destinations neither airline shares: {neither_shared_destinations}")


