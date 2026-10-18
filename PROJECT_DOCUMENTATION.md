Student Performance Analytics System

Student Name: Ananya Chinthakindi  
Department: Computer Science and Engineering  
Project Type: Individual Project

1. Introduction

The Student Performance Analytics System is a Python-based project that analyzes student marks and generates a performance report. It uses Pandas to organize student records and NumPy for numerical calculations.

The system calculates student totals and averages, assigns grades, checks pass/fail status, identifies top-performing students, and summarizes class and subject performance.

2. Objectives

- Analyze student academic performance using Python.
- Read and organize student data using Pandas.
- Perform numerical calculations using NumPy.
- Calculate total and average marks for each student.
- Assign grades and determine pass/fail status.
- Identify the highest- and lowest-performing students.
- Calculate subject-wise averages and the overall class average.
- Display the top five students based on average marks.

3. Technologies Used

- Python: Main programming language.
- NumPy: Numerical calculations and average computation.
- Pandas: Reading and organizing the student dataset.
- CSV: Storing student records.
- Visual Studio Code: Writing and running the program.

4. Dataset Description

The project uses students.csv, containing 20 student records.

The dataset includes:

- Student ID
- Name
- Department
- Python marks
- Mathematics marks
- Data Science marks
- Attendance

The program analyzes marks in three subjects. Attendance is included in the dataset but is not currently used in the calculations.

5. Implementation

5.1 Loading the Dataset

The program reads students.csv using Pandas and stores the records in a DataFrame. Student IDs are read as strings to preserve leading zeros.

5.2 Calculating Total and Average

The total marks are calculated by adding the marks obtained in Python, Mathematics, and Data Science.

The average is calculated by dividing the total marks by three. NumPy is used for numerical calculations.

5.3 Grade Assignment

Grades are assigned according to the student's average marks.

| Average Marks | Grade |

| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

5.4 Pass/Fail Calculation

A student is marked as Pass if their marks are at least 35 in all three subjects. If any subject mark is below 35, the student is marked as Fail.

Grade assignment and pass/fail status are calculated separately.

5.5 Performance Analysis

The program identifies the highest- and lowest-performing students, calculates the overall class average, determines subject-wise averages, identifies the best-performing subject, displays the top five students, and counts the students who passed and failed.

6. Results

The program produces the following results for the supplied dataset:

| Metric | Result |

| Highest-performing student | Sneha — 95.67 |
| Lowest-performing student | Vikram — 33.67 |
| Overall class average | 68.33 |
| Python average | 67.30 |
| Mathematics average | 68.65 |
| Data Science average | 69.05 |
| Best-performing subject | Data Science |
| Students passed | 18 |
| Students failed | 2 |

Top Five Students

| Student ID | Name | Average | Grade |

| 17 | Sneha | 95.67 | A+ |
| 07 | Kiran | 91.67 | A+ |
| 02 | Divya | 90.00 | A+ |
| 12 | Ananya | 89.33 | A |
| 19 | Divya | 85.67 | A |

7. How to Run the Project

- Install Python.
- Install the required libraries:
   python -m pip install numpy pandas
- Keep main.py and students.csv in the same folder.
- Open the project folder in Visual Studio Code.
- Run the program from the terminal:
   python main.py

8. Learning Outcomes

Through this project, I gained practical experience in:
- Python functions, loops, and conditional statements.
- Reading CSV files.
- Working with Pandas DataFrames.
- Performing numerical calculations using NumPy.
- Analyzing datasets and generating summary statistics.
- Finding and ranking top-performing records.

9. Future Enhancements

Possible improvements include:
- Attendance analysis.
- Department-wise performance comparisons.
- Charts and graphs for visualizing results.
- Validation for missing or invalid marks.
- A graphical user interface for easier interaction.

10. Conclusion

The Student Performance Analytics System demonstrates how Python, Pandas, and NumPy can be used to analyze student academic performance. It generates student-wise results, grades, pass/fail status, subject averages, class statistics, and a top-five ranking.

The project helped me apply programming fundamentals and data analysis techniques to a practical problem.

11. GitHub Repository

Repository URL: https://github.com/ananya26ch-ship-it/student-performance-analytics