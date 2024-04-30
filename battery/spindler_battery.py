from battery import Battery


# Spinder Battery Class

class SpinderBattery(Battery):
    def __init__(self,last_service,current_date) -> None:
        self.last_service = last_service
        self.current_date = current_date
        
        
    # + needs_service(): bool
    def needs_service(self) -> bool:
        pass
    



