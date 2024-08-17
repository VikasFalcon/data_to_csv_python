
import csv

# Dummy employee records
employee_records = [
    {'emp_id': 1, 'name': 'Jorge Martinez', 'gender': 'Male', 'age': 29, 'address': '7600 Margaret Mill\nPort Patricia, MD 34001'},
    {'emp_id': 2, 'name': 'Debra Griffin', 'gender': 'Female', 'age': 47, 'address': '4180 Brian Ports Suite 801\nCunninghamstad, PA 74351'},
    {'emp_id': 3, 'name': 'Nathaniel Williams', 'gender': 'Male', 'age': 38, 'address': '6660 Murphy Views\nEast Daniel, MA 17692'},
    {'emp_id': 4, 'name': 'Rebecca Davidson', 'gender': 'Female', 'age': 30, 'address': '331 Brown Stravenue\nNew Martinberg, AL 31479'},
    {'emp_id': 5, 'name': 'Edward Robinson', 'gender': 'Male', 'age': 55, 'address': '3452 Alexander Causeway\nMichellport, TX 68983'},
    {'emp_id': 6, 'name': 'Barbara Johnson', 'gender': 'Female', 'age': 45, 'address': '9820 Adrian Ford\nSouth Jennifer, MN 72680'},
    {'emp_id': 7, 'name': 'Jason Miller', 'gender': 'Male', 'age': 25, 'address': '8896 Richard Point\nClarkview, CO 44023'},
    {'emp_id': 8, 'name': 'Emily Smith', 'gender': 'Female', 'age': 32, 'address': '5217 Allen Drive\nEast Matthewtown, CA 63711'},
    {'emp_id': 9, 'name': 'Christopher Davis', 'gender': 'Male', 'age': 42, 'address': '4380 Mason Center\nHarrisonfurt, WI 81148'},
    {'emp_id': 10, 'name': 'Linda Brown', 'gender': 'Female', 'age': 27, 'address': '8153 Elizabeth Plaza\nMeyerland, GA 95738'},
    {'emp_id': 11, 'name': 'Michael Lee', 'gender': 'Male', 'age': 39, 'address': '2292 Stewart Port\nRodriguezview, VA 78332'},
    {'emp_id': 12, 'name': 'Sarah Anderson', 'gender': 'Female', 'age': 28, 'address': '9831 Carter Street Suite 818\nSimpsonstad, OR 40922'},
    {'emp_id': 13, 'name': 'Daniel Clark', 'gender': 'Male', 'age': 50, 'address': '4295 Carol Alley\nPaulberg, MO 60784'},
    {'emp_id': 14, 'name': 'Jessica Harris', 'gender': 'Female', 'age': 34, 'address': '1715 Simpson Mall Suite 238\nWest Angela, NY 41258'},
    {'emp_id': 15, 'name': 'David Wilson', 'gender': 'Male', 'age': 31, 'address': '8593 Stephen Village\nDavisberg, FL 92601'},
    {'emp_id': 16, 'name': 'Karen Walker', 'gender': 'Female', 'age': 49, 'address': '2334 Kelly Heights\nPort Monicaville, NJ 58614'},
    {'emp_id': 17, 'name': 'Paul Robinson', 'gender': 'Male', 'age': 60, 'address': '1392 Walker Springs\nWrighttown, IL 94326'},
    {'emp_id': 18, 'name': 'Lisa Lewis', 'gender': 'Female', 'age': 23, 'address': '9768 Linda View\nSouth Stephanie, SC 75639'},
    {'emp_id': 19, 'name': 'James Young', 'gender': 'Male', 'age': 35, 'address': '5580 Thompson Center\nSmithton, LA 19840'},
    {'emp_id': 20, 'name': 'Nancy King', 'gender': 'Female', 'age': 26, 'address': '6831 James Way\nBennettfort, UT 84567'}
]

# print("records=>",employee_records)

csv_file = 'employee_data.csv'

# This will get keys from your first record
fieldnames = employee_records[0].keys()

# Write data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the data rows
    writer.writerows(employee_records)
