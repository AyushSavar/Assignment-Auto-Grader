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
           
    texts = []
    cursor1 = assignments.find()
    for x in cursor:
        s1.append((x['course'],x['roll_num']))
    for x in cursor1:
        if (x['course'],x['roll_num']) in s1:
            s.add(x['assignment_num'])
            texts.append(x['file'])
    s=list(s)
    return (s, texts)
    
def get_students_associated(ta_id, assignment,table):

    #table = ta 
    query = {'ta_roll_num':ta_id,'assignment':assignment}
    cursor = table.find(query)
    s = []
    for x in cursor:
        s.append(x['roll_num'])
    return s
    
def return_assignment(ta_id, roll_number, course, assignment, marks, plag, comments,table):
    #table = graded
    user_data = {'roll_num':roll_number,'course':course,'assignment':assignment,'marks':marks,'plag':plag,'comments':comments}
    table.insert_one(user_data)
    return

##VIEW EVALUATIONS

def get_evaluated_assignments(assignment,ta_id,roll_number,table):
    #table  = graded
    query = {'assignment':assignment,'ta_roll_num':ta_id,'roll_num':roll_number}
    cursor = table.find(query)
    s = []
    for x in cursor:
        data = {'marks':x['marks'],'plag':x['plag'],'comments':x['comments']}
        s.append(data)

    return(s)