import random

from elf import Elf
from food import Food
from food_types import Milk, Chocolate, Bread, Pizza


class Journey:
    def __init__(self):
        self.elf_list = [Elf("1")]

    def start(self):
        self.read_calories_list()

        print(self.get_elf_with_most_calories())
        print(self.get_top_three_calorie_holder())

        backpack = [Milk(15), Chocolate(50), Bread(30), Pizza.hawaii(), Pizza(100,["cheese","ham"])]
        for item in backpack:
            if item == "pizza":
                print(f"{item.name} , {item.ingredients}")
            else:
                print(f"{item.name} form : {Food.form(item.name)}")

    def read_calories_list(self):
        with open("input.txt", "r") as file:
            elf_count = 0
            for line in file.readlines():
                if line != "\n":
                    food = Food(int(line))
                    self.elf_list[elf_count].add_to_backpack(food)
                    continue

                self.elf_list.append(Elf(str(elf_count + 2)))
                elf_count += 1

    def get_elf_with_most_calories(self):
        most_calories_elf = self.elf_list[0]
        highest_calories = most_calories_elf.calculate_calories_in_bag()
        for elf in self.elf_list:
            if elf.calculate_calories_in_bag() > highest_calories:
                most_calories_elf = elf
                highest_calories = elf.calculate_calories_in_bag()

        return f"Name of elf with most calories in bag: {most_calories_elf.name} with {highest_calories} in bag."

    def get_top_three_calorie_holder(self):
        sorted_elf_list = sorted(self.elf_list, key=lambda x: x.calculate_calories_in_bag(), reverse=True)
        first = sorted_elf_list[0]
        first_calories = first.calculate_calories_in_bag()
        second = sorted_elf_list[1]
        second_calories = second.calculate_calories_in_bag()
        third = sorted_elf_list[2]
        third_calories = third.calculate_calories_in_bag()

        return f"1,{first.name} => {first_calories} \n" \
               f"2,{second.name} => {second_calories} \n" \
               f"3,{third.name} => {third_calories} \n" \
               f"Total calories : {first_calories + second_calories + third_calories}"


if __name__ == "__main__":
    journey = Journey()
    journey.start()
