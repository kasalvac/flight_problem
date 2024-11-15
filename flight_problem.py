airports = [
"BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
"JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD",
]

routes = [
["DSM", "ORD"],
["ORD", "BGI"],
["BGI", "LGA"],
["SIN", "CDG"],
["CDG", "SIN"],
["CDG", "BUD"],
["DEL", "DOH"],
["DEL", "CDG"],
["TLV", "DEL"],
["EWR", "HND"],
["HND", "ICN"],
["HND", "JFK"],
["ICN", "JFK"],
["JFK", "LGA"],
["EYW", "LHR"],
["LHR", "SFO"],
["SFO", "SAN"],
["SFO", "DSM"],
["SAN", "EYW"],
]

starting_airport = ["LGA"]

def find_possible_destinations(start):
    options = []
    for flight in routes:
        if flight[0] == start:
            options.append(flight[1])

    return (options)

test = find_possible_destinations("CDG")
print(test)