from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
customer2 = Customer("Atanas", "test", "test.jones@gmail.com")
equipment = Equipment("Treadmill")
equipment2 = Equipment("Push Ups")
trainer = Trainer("Peter")
trainer2 = Trainer("Gosho")
subscription = Subscription("14.05.2020", 1, 1, 1)
subscription2 = Subscription("05.11.2020", 2, 2, 2)
plan = ExercisePlan(1, 1, 20)
plan2 = ExercisePlan.from_hour(2, 2, 3)

gym = Gym()

gym.add_customer(customer2)
gym.add_equipment(equipment2)
gym.add_trainer(trainer2)
gym.add_plan(plan2)
gym.add_subscription(subscription2)

# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
print(gym.subscription_info(2))

