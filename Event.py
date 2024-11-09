class Event:
    def __init__(self,name,date,location):
        self.name = name
        self.date = date
        self.location = location
        self.participant_count = 0
        
    def add_participant(self):
        self.participant_count += 1
        
    def get_participant_count(self):
        return self.participant_count
        
    def display_event(self):
        print(f"Event: {self.name}, Date: {self.date}, Location: {self.location}")
        print(f"Participants: {self.get_participant_count()}")
        
events ={}

while True:
    action = input("Enter action (add,add participant, display, exit:) ").lower()
    if action == 'exit':
        break
    try:   
        if action == 'add':
            name = input("Enter event name: ")
            date = input("Enter date of the event: ")
            location = input("Enter event location: ")
            events[name] = Event(name,date,location)
        elif action == 'add participant':
            event_name = input("Enter event name: ")
            event.add_participant()
            print(f"Participant added to {event_name}")
                       
        elif action == 'display':
            for event in events.values():
                event.display_event()# display
    except Exception as e:
        print(f"An error has occured {e}")
        
print("Event planner system closed.")