import csv

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

students = []
subject_columns = ["Calculus", "Physics", "Chemistry", "English", "Computer Science"]


with open("marks.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = sum(int(row[sub]) for sub in subject_columns)
        percentage = total / (len(subject_columns) * 100) * 100
        grade = get_grade(percentage)
        students.append({
            "Roll": row["Roll"],
            "Name": row["Name"],
            "Total": total,
            "Percentage": round(percentage, 2),
            "Grade": grade
        })


average_class = sum(s["Percentage"] for s in students) / len(students)
topper = max(students, key=lambda x: x["Percentage"])
lowest = min(students, key=lambda x: x["Percentage"])

print("\n===== CLASS REPORT =====")
for s in students:
    print(f"{s['Roll']} | {s['Name']} | Total: {s['Total']} | %: {s['Percentage']} | Grade: {s['Grade']}")

print("\n===== CLASS STATISTICS =====")
print(f"Class Average Percentage: {round(average_class, 2)}")
print(f"Topper: {topper['Name']} — {topper['Percentage']}%")
print(f"Lowest: {lowest['Name']} — {lowest['Percentage']}%")


with open("report.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Roll", "Name", "Total", "Percentage", "Grade"])
    for s in students:
        writer.writerow([s["Roll"], s["Name"], s["Total"], s["Percentage"], s["Grade"]])

print("\nReport saved to file: report.csv")