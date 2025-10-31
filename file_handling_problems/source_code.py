def read_marks(filename):
    marks = {}
    with open(filename, 'r') as file:
        for line in file:
            student_id, name, subject, score = line.strip().split(',')
            score = int(score)
            if student_id not in marks:
                marks[student_id] = {'name': name, 'scores': {}}
            marks[student_id]['scores'][subject] = score
    return marks

def calculate_marks(marks):
    report = {}
    for student_id, data in marks.items(): #studentid ante rollno, data lo {name,scores}
        scores = data['scores'] #scores ki okadict untadi with subject and scores as its key-value pair
        total = sum(scores.values())
        average = total / len(scores)
        highest_subject = max(scores)
        lowest_subject = min(scores)
        report[student_id] = {
            'name': data['name'],
            'total': total,
            'average': average,
            'highest': (highest_subject, scores[highest_subject]),
            'lowest': (lowest_subject, scores[lowest_subject])
        }
    return report

def write_report(report, filename):
    with open(filename, 'w') as file:
        for student_id, data in sorted(report.items(), key=lambda item: item[1]['average'], reverse=True): 
            #displays records in the descending order of avg of each student - sorted(report.items(),key = based on val,decending/ascending)
            file.write(f"Student ID: {student_id}\n")
            file.write(f"Name: {data['name']}\n")
            file.write(f"Total Marks: {data['total']}\n")
            file.write(f"Average Marks: {data['average']:.1f}\n")
            file.write(f"Highest Scored Subject: {data['highest'][0]} ({data['highest'][1]})\n")
            file.write(f"Lowest Scored Subject: {data['lowest'][0]} ({data['lowest'][1]})\n")
            file.write("--------------------------------------\n")

marks = read_marks('marks.txt') # marks = {rollno:{name:'',scores:{subjname:''}}}
report = calculate_marks(marks)
write_report(report, 'report.txt')
