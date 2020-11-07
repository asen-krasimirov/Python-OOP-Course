

class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

        self.__total_salary_sum = 0
        self.__total_animal_needs_sum = 0

    def add_animal(self, animal, price) -> str:

        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        self.__total_animal_needs_sum += animal.get_needs()
        return f"{animal.name} the {animal.type()} added to the zoo"

    def hire_worker(self, worker) -> str:

        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        self.__total_salary_sum += worker.salary
        return f"{worker.name} the {worker.type()} hired successfully"

    def fire_worker(self, worker_name: str) -> str:

        for worker in self.workers:
            if worker.name == worker_name:
                self.__total_salary_sum -= worker.salary
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:

        if self.__total_salary_sum > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= self.__total_salary_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:

        if self.__total_animal_needs_sum > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= self.__total_animal_needs_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = [repr(animal) for animal in self.animals if animal.type() == "Lion"]
        tigers = [repr(animal) for animal in self.animals if animal.type() == "Tiger"]
        cheetahs = [repr(animal) for animal in self.animals if animal.type() == "Cheetah"]

        full_animal_information = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
            '\n'.join(lions),
            f"----- {len(tigers)} Tigers:",
            '\n'.join(tigers),
            f"----- {len(cheetahs)} Cheetahs:",
            '\n'.join(cheetahs)
        ]

        return '\n'.join(full_animal_information)

    def workers_status(self) -> str:
        keepers = [repr(worker) for worker in self.workers if worker.type() == "Keeper"]
        caretakers = [repr(worker) for worker in self.workers if worker.type() == "Caretaker"]
        vets = [repr(worker) for worker in self.workers if worker.type() == "Vet"]

        full_worker_information = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers)} Keepers:",
            '\n'.join(keepers),
            f"----- {len(caretakers)} Caretakers:",
            '\n'.join(caretakers),
            f"----- {len(vets)} Vets:",
            '\n'.join(vets)
        ]

        return '\n'.join(full_worker_information)
