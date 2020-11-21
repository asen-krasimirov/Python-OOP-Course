import time

from report_generator import CPULoad
from report_formatter import format_to_text, format_to_pdf
from report_sender import send_text_email, send_pdf_email


class CPUReport:

    def __init__(self, generation_seconds: int):

        self._generator = CPULoad()
        self.generation_seconds = generation_seconds

    def _generate_report(self):
        return self._generator.get_cpu_load(self.generation_seconds)

    def _format_report(self):
        report = self._generate_report()
        average_report = sum(list(self._generator)) / len(self._generator)
        return self._formatter(report, average_report)
    
    def send_email(self):
        report = self._format_report()
        self._sender(report, self.generation_seconds)


class CPUTextReporter(CPUReport):
    
    def __init__(self, generation_seconds: int):
        super().__init__(generation_seconds)
        self._formatter = format_to_text
        self._sender = send_text_email


class CPUGraphReporter(CPUReport):
    
    def __init__(self, generation_seconds: int):
        super().__init__(generation_seconds)
        self._formatter = format_to_pdf
        self._sender = send_pdf_email


def send_plaint_text_email(seconds):
    reporter = CPUTextReporter(seconds)
    reporter.send_email()


def send_pdj_email(seconds):
    reporter = CPUGraphReporter(seconds)
    reporter.send_email()


def main():

    def send_plaint_text_email_test():
        reporter = CPUTextReporter(1)
        reporter.send_email()
        print('successfully send a text report')

    def send_pdj_email_test():
        reporter = CPUGraphReporter(1)
        reporter.send_email()
        print('successfully send a graph report')

    # send_plaint_text_email_test()
    # time.sleep(2)
    # send_pdj_email_test()
    # sub_tests()


if __name__ == '__main__':
    # send_plaint_text_email(10)
    pass