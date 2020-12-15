from abc import ABC, abstractmethod


class Connector:
    __is_connected: bool

    def __init__(self):
        self.__is_connected = False

    def connect(self):
        self.__is_connected = True

    def connect_to(self, cable: 'Connector'):
        self.connect()
        cable.connect()

    def __repr__(self):
        return self.__class__.__name__


class HDMIConnector(Connector):
    pass


class EthernetConnector(Connector):
    pass


class PowerConnector(Connector):
    pass


class Device:

    # @abstractmethod
    # def connected(self, device: 'Device', cable: Connector):
    #     pass

    # def connected(self, device: 'Device', cable: Connector):
    #     self.connected_to.append(device)
    #     cable.connect_to(self.hdmi_cable)
    #     if self not in device.connected_to:
    #         device.connected(self, cable)

    def __repr__(self):
        return self.__class__.__name__


class TV(Device):
    # TODO: Liskov Substitution / Open/Closed / Single Responsibility

    hdmi_cable: HDMIConnector
    power_cable: PowerConnector
    ethernet_cable: EthernetConnector

    def __init__(self):
        self.hdmi_cable = HDMIConnector()
        self.power_cable = PowerConnector()
        self.ethernet_cable = EthernetConnector()
        self.connected_to = []

    def connected(self, device: Device, cable: Connector):
        self.connected_to.append(device)
        cable.connect_to(self.hdmi_cable)
        if self not in device.connected_to:
            device.connected(self, cable)


class DVDPlayer(Device):

    def __init__(self):
        self.hdmi_cable = HDMIConnector()
        self.power_cable = PowerConnector()
        self.connected_to = []

    # def connected(self, device: Device, cable: Connector):
    #     self.connected_to.append(device)
    #     cable.connect_to(self.hdmi_cable)
    #     if self not in device.connected_to:
    #         device.connected(self, cable)
    #


class GameConsole(Device):

    def __init__(self, cable: Connector):
        self.cable_number_one = cable
        self.hdmi_cable = HDMIConnector()
        self.power_cable = PowerConnector()
        self.ethernet_cable = EthernetConnector()
        self.connected_to = []

    # TODO: Dependency Inversion
    def connected(self, device, cable):
        self.connected_to.append(device)
        self.cable_number_one.connect_to(cable)
        if self not in device.connected_to:
            device.connected(self, cable)


class Router(Device):

    def __init__(self):
        self.power_cable = PowerConnector()
        self.ethernet_cable = EthernetConnector()
        self.connected_to = []

    # TODO: Interface Segregation
    def connect_vie_ethernet(self, device):
        self.ethernet_cable.connect_to(device.ethernet_cable)

    def connect_via_power(self, wall):
        # Warning: Pseudo Code -> \n
        self.power_cable.connect_to(wall.power_cable)


def test_one():
    tv = TV()
    dvd = DVDPlayer()

    tv.connected(dvd, tv.hdmi_cable)
    print(tv.hdmi_cable)
    print(tv.hdmi_cable._Connector__is_connected)
    print(dvd.hdmi_cable._Connector__is_connected)
    print(tv.connected_to)
    print(dvd.connected_to)


def test_two():
    tv = TV()
    hdmi_cable = HDMIConnector()
    console = GameConsole(hdmi_cable)
    console.connected(tv, tv.hdmi_cable)
    print(tv.connected_to)
    print(console.connected_to)


test_two()
###############################################################
# class EntertainmentDevice:
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass
#
#
# class Television(EntertainmentDevice):
#     def connect_to_dvd(self, dvd_player):
#         self.connect_to_device_via_rca_cable(dvd_player)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_hdmi_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class dvd_player(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class GameConsole(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_hdmi_cable(television)
#
#     def connect_to_router(self, router):
#         self.connect_to_device_via_ethernet_cable(router)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
#
#
# class Router(EntertainmentDevice):
#     def connect_to_tv(self, television):
#         self.connect_to_device_via_ethernet_cable(television)
#
#     def connect_to_game_console(self, game_console):
#         self.connect_to_device_via_ethernet_cable(game_console)
#
#     def plug_in_power(self):
#         self.connect_device_to_power_outlet(self)
