from os import system


# def show_temperature(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         temperature = None  # TODO: measure temperature of a part
#         return result, temperature
#     return wrapper
#

def show_os():
    system('wmic os get Name')


def show_cpu_specs():
    system('wmic cpu get Name')


def show_ram():
    system('wmic MEMORYCHIP get Capacity')


def show_motherboard_specs():
    system('wmic baseboard get Manufacturer')
    system('wmic baseboard get Product')


def show_graphic_card_specs():
    system('wmic path win32_VideoController get Name')


def show_storages():
    system('wmic diskdrive get Model')
    system('wmic diskdrive get Size')


all_pc_specs = [
    show_os,
    show_cpu_specs,
    show_ram,
    show_motherboard_specs,
    show_graphic_card_specs,
    show_storages
]


def main():

    for spec in all_pc_specs:
        spec()


if __name__ == '__main__':
    main()
