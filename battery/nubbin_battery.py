from battery import Battery

# Nubbin Battery Class

class NubbinBattery(Battery):
    def __init__(self,last_service, current_data):
        self.last_service = last_service
        self.current_data = current_data

    # + needs_service(): bool     
    def needs_service(self) -> bool:
        pass
        

