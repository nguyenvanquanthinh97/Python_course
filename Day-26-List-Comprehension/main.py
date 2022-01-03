from random import randint
import pandas

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Angela"
letter_list = [c for c in name]

doublex = [num * 2 for num in range(1, 5)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_uppercase_names = [name.upper() for name in names if len(name) >= 5]

students_scores = {name: randint(50, 100) for name in names}
passed_students_scores = {name: score for (name, score) in students_scores.items() if score >= 70}

# Loop through a DataFrame
students_scores = {
    "student": names,
    "score": [randint(50, 100) for i in range(len(names))]
}
students_scores_dataframe = pandas.DataFrame(students_scores)
# for (key, value) in students_scores_dataframe.items():
#     print(value)

for (index, row) in students_scores_dataframe.iterrows():
    print(row)