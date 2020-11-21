

def get_average_report(report) -> float:
    report_length = len(report)
    new_report = (report[index][1] for index in range(0, len(report)))
    average_report = sum(new_report) / report_length
    return average_report
