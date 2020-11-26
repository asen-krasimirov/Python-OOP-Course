import os


def get_data():
    with open('pc_specs.txt', 'w'):
        pass
    command = r'python C:\Users\Game\Desktop\Python-OOP\pc_specifications\specs.py >> C:\Users\Game\Desktop\Python-OOP\pc_specifications\pc_specs.txt'
    os.system(command)


def format_data():
    global hardware_information_by_category

    # deleting test
    hardware_information_by_category.pop('test')

    # reformatting RAM
    total_ram = 0
    for i in range(len(hardware_information_by_category['RAM'])):
        total_ram += int(hardware_information_by_category['RAM'][i]) // 1_000_000_000
    hardware_information_by_category['RAM'] = [f'{total_ram} GB']

    # reformatting Storage Size
    total_storage = 0
    for i in range(len(hardware_information_by_category['Total Storage Size'])):
        total_storage += int(hardware_information_by_category['Total Storage Size'][i]) // 1_000_000_000_000
    hardware_information_by_category['Total Storage Size'] = [f"{total_storage} TB"]

    # reformatting multiple values
    for key, value in hardware_information_by_category.items():
        hardware_information_by_category[key] = '\n'.join(value)

    # reformatting OS
    hardware_information_by_category['OS'] = hardware_information_by_category['OS'].split('|')[0]

    # reformatting Motherboard Information
    mother_board_information = hardware_information_by_category['Motherboard Manufacturer'] + ' ' + hardware_information_by_category['Motherboard Model']
    hardware_information_by_category.pop('Motherboard Manufacturer')
    hardware_information_by_category.pop('Motherboard Model')
    hardware_information_by_category['Motherboard Model'] = mother_board_information


hardware_information = []
hardware_information_by_category = {
    'test': [],
    'OS': [],
    'CPU(s)': [],
    'RAM': [],
    'Motherboard Manufacturer': [],
    'Motherboard Model': [],
    'GPU(s)': [],
    'Storage Model(s)': [],
    'Total Storage Size': []
}
split_names = {'Manufacturer', 'Product', 'Name', 'Model', 'Size', 'Capacity'}


def main_logic():
    global hardware_information, hardware_information_by_category

    with open('pc_specs.txt', encoding='utf-16') as file:
        data = file.readlines()
        for string in data:
            hardware_information.append(string)

    for key in hardware_information_by_category:
        while hardware_information:
            part = hardware_information.pop(0).strip('\n').strip()
            if part in split_names:
                break

            hardware_information_by_category[key].append(part)
    # hardware_information_by_category.pop('test')
    #
    # for key, value in hardware_information_by_category.items():
    #     hardware_information_by_category[key] = ', '.join(value)

    # hardware_information_by_category['OS'] = hardware_information_by_category['OS'].split('|')[0]


def main():
    get_data()
    main_logic()
    format_data()
    return hardware_information_by_category
