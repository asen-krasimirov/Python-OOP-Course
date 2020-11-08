

def get_preset():

    preset_information = [
        '---> Small Exploder',
        '---> Exploder',
        '---> 10 Cell Row',
        '---> Tumbler',
        '---> Gosper Glider Gun',
        "Type here: "
    ]

    select_information = '\n'.join(preset_information)

    preset = input(
        "Select a preset from the given ones:\n"
        f"{select_information}"
    )

    path_by_preset = {
        'Small Exploder': 'presets/small_exploder.txt',
        'Exploder': 'presets/exploder.txt',
        '10 Cell Row': 'presets/10_cell_row.txt',
        'Tumbler': 'presets/tumbler.txt',
        'Gosper Glider Gun': 'presets/gosper_glider_gun.txt'
    }

    preset_path = path_by_preset[preset]
    with open(preset_path) as file:
        return file.read()
