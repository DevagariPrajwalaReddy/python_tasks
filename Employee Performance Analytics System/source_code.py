import os
    

def validate_record(record):
    parts = record.split(',')
    if len(parts) != 4:
        return False, "Invalid record format"
    
    employee_id, employee_name, department, rating = parts #destructuring the parts list
    
    if not employee_id.strip().isdigit(): #validating the employee id
        return False, "EmployeeID is not numeric"
    
    if not employee_name.strip(): #validating the employee name
        return False, "EmployeeName cannot be empty"
    
    if not department.strip(): #validating the department
        return False, "Department cannot be empty"
    
    try: #validating the rating
        rating = float(rating)
        if rating < 1.0 or rating > 5.0:
            return False, "Rating is not between 1.0 and 5.0"
    except ValueError:
        return False, "Rating is not a valid float"
    
    return True, (employee_id, employee_name, department, rating)

def process_records(records):
    valid_records = []
    error_log = []
    
    for record in records:
        is_valid, result = validate_record(record)
        if is_valid:
            valid_records.append(result)
        else:
            error_log.append(f"Invalid row: \"{record}\" -> {result}")
    
    return valid_records, error_log

def write_error_log(file_name, error_log):
    with open(file_name, 'w') as file:
        for error in error_log:
            file.write(error + '\n')

def calculate_summary(valid_records):

    department_ratings = {} #{dept1:[val1,val2...],dept2:[val1,val2..],...}
    top_performer = None
    max_rating = 0
    
    total_employees = len(valid_records)

    for employee_id, employee_name, department, rating in valid_records:
        if department not in department_ratings:
            department_ratings[department] = []
        department_ratings[department].append(rating)
        
        if rating > max_rating:
            max_rating = rating
            top_performer = (employee_name, department, rating)

    average_ratings = {} #{deptname:avg_rating,...}
    for department, ratings in department_ratings.items(): #calculating the average ratings for each department
        average_ratings[department] = sum(ratings) / len(ratings)

    
    return total_employees, average_ratings, top_performer

def write_summary(file_name, total_employees, average_ratings, top_performer):
    with open(file_name, 'w') as file:
        file.write(f"Total Valid Employees: {total_employees}\n")
        file.write("Average Ratings by Department:\n")
        for department, rating in average_ratings.items():
            file.write(f"{department}: {rating:.2f}\n")
        file.write("Top Performer:\n")
        file.write(f"Employee Name: {top_performer[0]}\n")
        file.write(f"Department: {top_performer[1]}\n")
        file.write(f"Rating: {top_performer[2]}\n")

def main():
    file_name = 'employee_performance.txt'
    #validating the file
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            records = [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        records = []
    
    valid_records, error_log = process_records(records)
    write_error_log('error_log.txt', error_log)
    
    if valid_records:
        total_employees, average_ratings, top_performer = calculate_summary(valid_records)
        write_summary('performance_summary.txt', total_employees, average_ratings, top_performer)
    else:
        print("No valid records found.")

if __name__ == "__main__":
    main()


"""  
1. validate the employee_performance.txt file -- check if the file exists
2. validate each record in the file -- check if the record is valid -- process_records() -- returns valid records and error log
3. in error_log.txt, write the error log which we got from process_records()
4. next we work on valid_records from process_records():
   from valid records we need:
         - total number of valid employees
         - average ratings of each department
         - top performer based on ratings of all the employees: and display employee name, department, rating
    All this goes into performance_summary.txt
   
"""