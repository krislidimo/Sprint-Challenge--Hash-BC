#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []
    firstTicket = None
    lastTicket = None

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

        if ticket.source == 'NONE':
            firstTicket = ticket.destination
        elif ticket.destination == 'NONE':
            lastTicket = ticket.source

    route.append(firstTicket)
    current = firstTicket
    nextTicket = hash_table_retrieve(hashtable, current)
    while current != 'NONE':
        route.append(nextTicket)
        current = nextTicket
        nextTicket = hash_table_retrieve(hashtable, current)


    return route
