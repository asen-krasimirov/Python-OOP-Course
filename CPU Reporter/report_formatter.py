from typing import List
from datetime import datetime
import matplotlib.pyplot as plt


def format_to_text(report: List[list], average_report: float):

    for i in range(len(report)):
        report[i] = [datetime.strftime(report[i][0], "%H:%M:%S:%f"), f'{report[i][1] :.2f} %']
    average_report = f"Average CPU load: {average_report :.2f} %"

    return '\n'.join(' -> '.join(elem) for elem in report) + '\n' + average_report


def format_to_pdf(report: List[list], average_report: float):

    times = [elem[0] for elem in report]
    measurements = [elem[1] for elem in report]
    average_report = f"Average CPU load: {average_report :.2f} %"

    plt.plot(times, measurements, color='red', marker='o', )
    plt.title(average_report, fontsize=10)
    plt.xlabel('Times', fontsize=14)
    plt.ylabel('Measurements [in %]', fontsize=14)
    plt.suptitle('Measurements Vs Times', fontsize=14)
    plt.grid(True)
    plt.savefig('image_to_send.png')


if __name__ == '__main__':
    pass
