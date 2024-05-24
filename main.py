
from datetime import datetime
from car_factory import CarFactory

def main():
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - 5)
    current_mileage = 0
    last_service_mileage = 0

    car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
    print(car.needs_service())
    print(car.battery.last_service)
    print(car.battery.current_date)
    
    # current_date = datetime.today().date()
    # last_service_date = current_date.replace(year = current_date.year - 1)
    # current_mileage = 0
    # last_service_mileage = 0

    # calliope_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    # print(calliope_car.needs_service())
    # print(calliope_car.battery.last_service)
    # print(calliope_car.battery.current_date)

if __name__ == "__main__":
    main()