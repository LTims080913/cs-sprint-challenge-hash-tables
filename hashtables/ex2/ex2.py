#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = [None] * length
    stops = {}
    for tic in tickets:
        stops[tic.source] = tic.destination
    next = stops["NONE"]
    for each in range(0, length):
        route[each] = next
        next = stops[next]
    return route
