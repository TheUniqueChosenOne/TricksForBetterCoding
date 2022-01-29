# When we have different options , we can consider using strategy design pattern.
# In python, we can implement strategy pattern either by class or by functions (function is first-class object in python).
from concurrent.futures import process
import string
import random
from abc import ABC, abstractmethod

class SupportTicket:
    id: str
    customer: str
    issue: str
    
    def generate_id(self):
        return ''.join(random.choices(string.ascii_uppercase, k=10))

    def __init__(self, name, issue):
        self.id = self.generate_id()
        self.name = name
        self.issue = issue

"""
class TicketOrderStrategy(ABC):
    @abstractmethod
    def process_ticket(self, tickets: list[SupportTicket])->list[SupportTicket]:
        pass

class FIFOOrderTicketStrategy(TicketOrderStrategy):
    def process_ticket(self, tickets: list[SupportTicket])->list[SupportTicket]:
        return tickets.copy()

class FILOOrderTicketStrategy(TicketOrderStrategy):
    def process_ticket(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        copy_list = tickets.copy()
        copy_list = reversed(copy_list)
        return copy_list

class RandomOrderTicketStrategy(TicketOrderStrategy):
    def process_ticket(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        copy_list = tickets.copy()
        random.shuffle(copy_list)
        return copy_list
"""
def fifo_ticket_strategy(tickets:list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()

def filo_ticket_strategy(tickets:list[SupportTicket]) -> list[SupportTicket]:
    return reversed(tickets.copy())

def random_ticket_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    copy_list = tickets.copy()
    random.shuffle(copy_list)
    return copy_list

class CustomerSupport:
    tickets = []

    def create_tickets(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))
    
    def process_tickets(self, process_func):
        if self.tickets == 0:
            print(f'tickets length = {len(self.tickets)}, there is no tickets needed to be processed.')

        ticket_list = process_func(self.tickets)
        for ticket in ticket_list:
            self.process_ticket(ticket)
        

    def process_ticket(self, ticket: SupportTicket):
        print('---------------------')
        print(f'ticket customer: {ticket.name}')
        print(f'ticket id: {ticket.id}')
        print(f'ticket issue: {ticket.issue}')
        print('---------------------')


if __name__ == '__main__':
    app = CustomerSupport()
    app.create_tickets('daishan', 'item is broken.')
    app.create_tickets('Smith', 'money is lost.')
    app.create_tickets('Soluri', 'find right purchase.')

    app.process_tickets(random_ticket_strategy)