import numpy as np
import pandas as pd

df = pd.read_csv("students.csv", dtype={"Student_ID": str})

subjects = ["Python", "Mathematics", "Data Science"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = np.mean(df[subjects].to_numpy(), axis=1)

averages = df["Average"].tolist()
print("\nStudent Totals and Averages\n")
print(
    df[["Student_ID", "Name", "Total", "Average"]]
    .to_string(index=False)
)


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


grades = []
for average in averages:
    grades.append(assign_grade(average))
df["Grade"] = grades


def check_pass(row):
    if (
        row["Python"] >= 35
        and row["Mathematics"] >= 35
        and row["Data Science"] >= 35
    ):
        return "Pass"
    else:
        return "Fail"


statuses = []
for index in range(len(df)):
    status = check_pass(df.iloc[index])
    statuses.append(status)
df["Status"] = statuses

print("\nStudent Performance Report\n")
print(
    df[
        ["Student_ID", "Name", "Average", "Grade", "Status"]
    ].to_string(index=False)
)


highest_index = 0
lowest_index = 0
for index in range(1, len(df)):
    if averages[index] > averages[highest_index]:
        highest_index = index
    if averages[index] < averages[lowest_index]:
        lowest_index = index

print("\nHighest-performing Student")
print("Name:", df.loc[highest_index, "Name"])
print("Average:", round(averages[highest_index], 2))

print("\nLowest-performing Student")
print("Name:", df.loc[lowest_index, "Name"])
print("Average:", round(averages[lowest_index], 2))


class_average = np.mean(averages)
print("\nOverall Class Average:", round(class_average, 2))


print("\nSubject-wise Average Marks:")
for subject in subjects:
    subject_average = np.mean(df[subject])
    print(subject, ":", round(subject_average, 2))


best_subject = subjects[0]
highest_subject_average = np.mean(df[best_subject])
for subject in subjects[1:]:
    subject_average = np.mean(df[subject])
    if subject_average > highest_subject_average:
        highest_subject_average = subject_average
        best_subject = subject
print("\nBest-performing Subject:", best_subject)
print("Highest Subject Average:", round(highest_subject_average, 2))


top_indices = []
for index in range(len(df)):
    position = 0
    while position < len(top_indices):
        if averages[index] > averages[top_indices[position]]:
            break
        position += 1

    top_indices.insert(position, index)
    if len(top_indices) > 5:
        top_indices.pop()


print("\nTop 5 Performing Students\n")
top_five = df.iloc[top_indices][
    ["Student_ID", "Name", "Average", "Grade"]
]
print(top_five.to_string(index=False))


pass_count = 0
fail_count = 0
for status in df["Status"]:
    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("\nPASS/FAIL Summary")
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)