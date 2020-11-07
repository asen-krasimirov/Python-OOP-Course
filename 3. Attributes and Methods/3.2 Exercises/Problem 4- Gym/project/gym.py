from .customer import Customer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription
from .trainer import Trainer
from typing import List


def common_add(object_, dict_var_name, dict_by_id_var_name):
    if object_.id in dict_by_id_var_name:
        return

    dict_var_name.append(object_)
    dict_by_id_var_name[object_.id] = object_


class Gym:
    customers: List[Customer]
    trainers: List[Trainer]
    equipment: List[Equipment]
    plans: List[ExercisePlan]
    subscriptions: List[Subscription]

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

        self.customer_by_id = {}
        self.trainer_by_id = {}
        self.equipment_by_id = {}
        self.plan_by_id = {}
        self.subscription_by_id = {}

    @staticmethod
    def common_add(object_, dict_var_name, dict_by_id_var_name):
        if object_.id in dict_by_id_var_name:
            return

        dict_var_name.append(object_)
        dict_by_id_var_name[object_.id] = object_

    def add_customer(self, customer: Customer):
        self.common_add(customer, self.customers, self.customer_by_id)

    def add_trainer(self, trainer: Trainer):
        self.common_add(trainer, self.trainers, self.trainer_by_id)

    def add_equipment(self, equipment: Equipment):
        self.common_add(equipment, self.equipment, self.equipment_by_id)

    def add_plan(self, plan: ExercisePlan):
        self.common_add(plan, self.plans, self.plan_by_id)

    def add_subscription(self, subscription: Subscription):
        common_add(subscription, self.subscriptions, self.subscription_by_id)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = self.subscription_by_id[subscription_id]
        customer = self.customer_by_id[subscription.customer_id]
        trainer = self.trainer_by_id[subscription.trainer_id]
        plan = [plan for plan in self.plans if plan.trainer_id == trainer.id][0]
        equipment = self.equipment_by_id[plan.equipment_id]

        information = [
            subscription, customer, trainer, equipment, plan
        ]
        return "\n".join([info.__repr__() for info in information])
