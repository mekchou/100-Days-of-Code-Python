
import pandas as pd

# TODO 1. create a dict in this format: {"A": "Alfa", "B":"Bravo"}
dataframe = pd.read_csv(r"data\nato_phonetic_alphabet.csv")
# print(dataframe)

phonetic_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}
# print(phonetic_dict)

# TODO 2. Creat a list of the phonetic code words from a word that the user inputs

user_input = input("Input word to be converted to phonetic:\n").upper()
# user_input = "asd".upper()
result = [phonetic_dict[letter] for letter in user_input]
# result = [letter for letter in user_input_list]
print(result)







# numbers = [1,2,3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# range_numbers = range(1, 5)

# new_range_numbers = [n*2 for n in range_numbers]

# print(new_range_numbers)


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)


# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: random.randint(1,100) for student in names}

# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)

# student_dict = {
    # "student": ["Angela", "James", "Lily"],
    # "score": [56, 76, 98],
# }
# Looping through dictionaries:
# for (key, value) in student_dict.items():
    # print(value)
    # print(key)
    
# student_df = pd.DataFrame(student_dict)
# print(student_df)

# # Loop through a data frame
# for (key, value) in student_df.items():
#     print(value)

# # Loop through rows of a data frame
# for (index, row) in student_df.iterrows():
#     # print(index)
#     print(row.student)

