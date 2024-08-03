
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to
common_destinations = our_routes & competitor_routes

# 2. Destinations unique to your airline
unique_to_our_airline = our_routes - competitor_routes

# 3. Check if there are destinations that neither airline shares
all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}
neither_shared_destinations = all_possible_destinations - (our_routes | competitor_routes)

print(f"Common Destinations: {common_destinations}")
print(f"Unique to Our Airline: {unique_to_our_airline}")
print(f"Destinations neither airline shares: {neither_shared_destinations}")


