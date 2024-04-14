from pymongo import MongoClient
import os

client = MongoClient('mongodb+srv://user1:hehe@atlascluster.t9cnxbb.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster')


db = client['test_database']
assignments = db['assignments']
ta = db['ta']
graded = db['graded']
assigned = db['assigned']

def get_student_courses(roll_number,table):
    #table = assigned
    query = {'roll_num':roll_number}
    cursor = table.find(query)
    s = set()
    for x in cursor:
        s.add(x['course'])
    s = list(s)
    return s

    
def get_student_assignments(roll_number, course,table):
    #table = assigned
    query = {'roll_num':roll_number,'course': course}
    cursor = table.find(query)
    s = []
    for x in cursor:
        s.append(x['assignment_num'])

    return s



def add_submission(roll_number, course, assignment, file, details,table):
    #table = assignments
    user_data = {'roll_num':roll_number,'course':course,'assignment_num':assignment,'file':file,'remarks':details}
    try:
        table.insert_one(user_data)
        return "SUCCESS"
    except:
        return "FAIl"
    

##VIEW SUBMISSION

def get_submitted_assignments(roll_number, course,table):
   #table = assignments
   query = {'roll_num':roll_number,'course':course}
   cursor = table.find(query)
   s = []
   for x in cursor:
       s.append(x['assignment_num'])
   return s
    
def view_submission(roll_number, course, assignment,table):
    #table = graded 
    query = {'roll_num':roll_number,'course':course,'assignment_num': assignment}
    cursor = table.find(query)
    s = []
    for x in cursor:
        data = {'marks':x['marks'],'plag':x['plag'],'comments':x['comments']}
        s.append(data)
    return s
'''
def reval_request(roll_number, course, assignment, details):
    print(1)
'''

##EVALUATE SUBMISSIONS
def get_assignments_to_evaluate(ta_id,table):
    #table = ta
    query = {'ta_roll_num':ta_id}
    print(query)
    cursor = ta.find(query)
    s = set()
    s1 = []
    print(s1)
    roll_nums = []
    texts = []
    cursor1 = assignments.find()
    for x in cursor:
        s1.append((x['course'],x['roll_num']))
    for x in cursor1:
        if (x['course'],x['roll_num']) in s1:
            s.add(x['assignment_num'])
    s=list(s)
    return (s)



def get_plag_list(ta_id, assignment):
    # Fetch roll numbers of students associated with the given TA and course
    query_ta = {'ta_roll_num': ta_id}
    cursor_ta = ta.find(query_ta)
    roll_numbers = [x['roll_num'] for x in cursor_ta]

    # Fetch submissions for the given assignment and course
    query_submissions = {'assignment_num': assignment, 'roll_num': {'$in': roll_numbers}}
    cursor_submissions = assignments.find(query_submissions)

    # Initialize a dictionary to store files grouped by roll numbers
    roll_files_map = {roll_num: [] for roll_num in roll_numbers}

    # Organize submissions into the dictionary using roll numbers as keys
    for submission in cursor_submissions:
        roll_files_map[submission['roll_num']].append(submission['file'])

    # Filter out roll numbers with no submissions
    roll_numbers_with_submissions = [roll_num for roll_num, files in roll_files_map.items() if files]

    # Convert the dictionary to the desired 2D array format
    assignments_2d_array = [roll_files_map[roll_num] for roll_num in roll_numbers_with_submissions]

    return roll_numbers_with_submissions, assignments_2d_array

    
def get_students_associated(ta_id, assignment,table):
    query = {'ta_roll_num':ta_id}
    print(query)
    cursor = ta.find(query)
    s = set()
    s1 = []
    print(s1)
    cursor1 = assignments.find()
    for x in cursor:
        s1.append((x['roll_num']))
    for x in cursor1:
        if (x['roll_num']) in s1 and x['assignment_num']==assignment: 
            s.add(x['roll_num'])
    s=list(s)
    return s
    
   
def return_assignment(ta_id, roll_number, course, assignment, marks, plag, comments,table):
    #table = graded
    user_data = {'roll_num':roll_number,'course':course,'assignment':assignment,'marks':marks,'plag':plag,'comments':comments}
    table.insert_one(user_data)
    return

##VIEW EVALUATIONS

def get_code(ta_id, assignment, student):
    query = {'ta_roll_num':ta_id}
    cursor = ta.find(query)
    s = set()
    s1 = []
    #print(s1)
    cursor1 = assignments.find()

    for x in cursor:
        s1.append((x['course']))
    print("S!!")
    print(s1)
    for x in cursor1:
        if (x['roll_num'])==student and  x['assignment_num']==assignment and x['course'] in s1:
            return x['file'].decode('utf-8')

def get_evaluated_assignments(assignment,ta_id,roll_number,table):
    #table  = graded
    query = {'assignment':assignment,'ta_roll_num':ta_id,'roll_num':roll_number}
    cursor = table.find(query)
    s = []
    for x in cursor:
        data = {'marks':x['marks'],'plag':x['plag'],'comments':x['comments']}
        s.append(data)

    return(s)