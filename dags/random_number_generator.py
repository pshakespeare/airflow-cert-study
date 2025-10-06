from airflow.decorators import dag, task
from datetime import datetime
import random 



@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    description='A simple DAG to generate and check random numbers',
    catchup=False,
    tags=["random_num_gen"]
)
def random_number_checker_taskflow():
    @task
    def generate_random_number():
        number = random.randint(1, 100)
        print(f"Generated random number: {number}")
        return number

    @task
    def check_even_odd(number):
        result = "even" if number % 2 == 0 else "odd"
        print(f"The number {number} is {result}.")

    generated_number = generate_random_number()
    check_even_odd(generated_number)
random_number_checker_taskflow = random_number_checker_taskflow()