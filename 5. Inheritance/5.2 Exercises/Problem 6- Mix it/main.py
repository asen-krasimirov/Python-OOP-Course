from project.vehicle.car import Car
from project.vehicle.bus import Bus
from project.vehicle.plane import Plane
from project.technology.laptop import Laptop
from project.technology.smart_phone import SmartPhone
from project.parking_mall.level1 import Level1
from project.parking_mall.level2 import Level2
from project.parking_mall.level3 import Level3


def vehicle_tests():
    print("Vehicle Tests: ")

    def car_tests():
        print('Car Tests: ')

        def drive_test():
            loc_object = Car(5, 100, 1, 50)
            assert loc_object.drive(10) == "We've enjoyed the travel!"
            assert loc_object.fuel == 40, loc_object.fuel
            loc_object.drive(50)
            assert loc_object.fuel == 40, loc_object.fuel
            print('drive_test Test passed')

        def refuel_test():
            loc_object = Car(5, 100, 1, 50)
            loc_object.refuel(40)
            assert loc_object.fuel == 90, loc_object.fuel
            assert loc_object.refuel(20) == "Capacity reached!"
            loc_object.refuel(10)
            assert loc_object.fuel == 100, loc_object.fuel
            print('refuel_test Test passed')

        drive_test()
        refuel_test()

    def bus_tests():
        print('Bus Tests: ')

        def get_ticket_test():
            loc_object = Bus(5, 2)
            loc_object.get_ticket(2)
            assert loc_object._Bus__tickets_sold == 2
            assert loc_object.get_ticket(4) == "Capacity reached!"
            print('get_ticket_test Test passed')

        def get_total_profit_test():
            loc_object = Bus(5, 2)
            loc_object.get_ticket(5)
            assert loc_object._Bus__tickets_sold == 5
            assert loc_object.get_total_profit() == 10
            print('get_total_profit_test Test passed')

        get_ticket_test()
        get_total_profit_test()

    def plane_tests():
        print('Plane Tests: ')

        def buy_tickets_test():
            loc_object = Plane(10, 5, 2)
            loc_object.buy_tickets(6, 2)
            assert loc_object.buy_tickets(6, 2) == f"There is no row 6 in the plane!"
            loc_object.buy_tickets(2, 2)
            assert loc_object._Plane__seats_available[2] == 0, loc_object._Plane__seats_available[2]
            assert loc_object.buy_tickets(2, 2) == "Not enough tickets on row 2!"
            print('buy_tickets_test Test passed')

        buy_tickets_test()

    car_tests()
    bus_tests()
    plane_tests()


def technology_tests():
    print("Technology Tests: ")

    def laptop_tests():
        print('Laptop Tests: ')

        def install_software_test():
            loc_object = Laptop(100, 0)
            assert loc_object.install_software('test_app', 50) == 50, loc_object._memory_taken
            assert loc_object.install_software('test_app', 51) == "You don't have enough space for test_app!"
            print('install_software_test Test passed')

        install_software_test()

    def phone_tests():
        print('SmartPhone Tests: ')

        def install_apps_test():
            loc_object = SmartPhone(100, 50)
            assert loc_object.install_apps('test_app', 50) == 0
            assert loc_object.install_apps('test_app', 50) == "You don't have enough space for test_app!"
            print('install_app_tests Test passed')

        install_apps_test()

    laptop_tests()
    phone_tests()


def parking_mall_tests():
    print("Parking Mall Tests: ")

    def level1_tests():
        print('Level1 Tests: ')

        loc_object = Level1(100)
        assert loc_object.check_availability() == "Parking lots available: 50", loc_object.check_availability()
        loc_object2 = Level1(150)
        assert loc_object2.check_availability() == "There are no more parking lots!", loc_object2.check_availability()
        print('level1_tests Test passed')

    def level2_tests():
        print('Level2 Tests: ')

        loc_object = Level2(50)
        assert loc_object.check_availability() == "Parking lots available: 50", loc_object.check_availability()
        loc_object2 = Level2(100)
        assert loc_object2.check_availability() == "There are no more parking lots!", loc_object2.check_availability()
        print('level2_tests Test passed')

    def level3_tests():
        print('Level3 Tests: ')

        loc_object = Level3(40)
        assert loc_object.check_availability() == "Parking lots available: 40", loc_object.check_availability()
        loc_object2 = Level3(80)
        assert loc_object2.check_availability() == "There are no more parking lots!", loc_object2.check_availability()
        print('level2_tests Test passed')

    level1_tests()
    level2_tests()
    level3_tests()


if __name__ == '__main__':
    vehicle_tests()
    technology_tests()
    parking_mall_tests()
