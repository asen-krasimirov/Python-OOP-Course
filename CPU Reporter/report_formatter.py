from typing import List
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def format_to_text(report: List[list]):

    for i in range(len(report)):
        report[i] = [datetime.strftime(report[i][0], "%H:%M:%S:%f"), f'{report[i][1] :.2f} %']

    return '\n'.join(' -> '.join(elem) for elem in report)


def format_to_pdf(report: List[list]):

    times = [elem[0] for elem in report]
    measurements = [elem[1] for elem in report]

    plt.plot(times, measurements, color='red', marker='o', )
    plt.title('Измервания срешу Времена', fontsize=14)
    plt.xlabel('Времена', fontsize=14)
    plt.ylabel('Измервания в %', fontsize=14)
    plt.grid(True)
    plt.savefig('image_to_send.png')


if __name__ == '__main__':
    pass