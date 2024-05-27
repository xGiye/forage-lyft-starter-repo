from battery.battery import Battery
from util import add_years_to_date
# Spinder Battery Class

class SpinderBattery(Battery):
    def __init__(self,last_service,current_date) -> None:
        self.last_service = last_service
        self.current_date = current_date
        
        
    # + needs_service(): bool
    def needs_service(self) -> bool:
        sugggested_date_of_serviced = add_years_to_date(self.last_service,3)
        if self.current_date >= sugggested_date_of_serviced:
            return True
        else:
            return False
    


