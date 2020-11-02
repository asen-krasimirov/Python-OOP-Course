from project.task import Task


class Section:
    name: str
    tasks: list

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:

        for task in self.tasks:
            if task.name == new_task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:

        for task in self.tasks:
            if task.name == task_name:
                task.completed = not task.completed
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:

        cleaned_amount = 0
        index = 0
        while index < len(self.tasks):
            if self.tasks[index].completed:
                self.tasks.pop(index)
                cleaned_amount += 1
                continue
            index += 1
        return f"Cleared {cleaned_amount} tasks."

    def view_section(self) -> str:
        section_information = [
            f"Section {self.name}:",
            "\n".join([task.details() for task in self.tasks])
        ]

        return "\n".join(section_information)
