class Vehicle:
    
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner
        
    def update_owner(self, new_owner):
        self.owner = new_owner
        
    def display_details(self):
        print(f"Regisration: {self.reg_num}. Vehicle type: {self.vehicle_type}, Owner: {self.owner}")

vehicles = {}

def register_vehicle(reg_num, vehicle_type, owner):
    if reg_num in vehicles:
        print("Error vehicle registration already exists")
        return
    vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print(f"Vehicle with reg num {reg_num} has been registered.")
        
def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated owner for vehicle {reg_num}.")
    else: 
        print("Vehicle not found")
    
def display_all():
    for vehicle in vehicles.values():
        vehicle.display_details()
while True:
    action = input("register, update, display, exit ").lower()
    if action == 'exit':
        break
    try:
        if action == 'register':
            reg_num = input("Enter the registration number: ")
            vehicle_type = input ("Enter the vehicle type: ")
            owner = input("Enter the vehicle owner: ")
            register_vehicle(reg_num, vehicle_type, owner)
        elif action == 'update':
            reg_num = input("Enter the registration number: ")
            new_owner = input("Enter the new owner name: ")
            update_vehicle_owner(reg_num,new_owner)
        elif action == 'display':
            display_all()
          #  print (vehicles)
    except Exception as e:
        print(f"An error has occured {e} ")

print("DMV system closed")