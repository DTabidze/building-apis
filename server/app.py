from config import app,db
from models import Course,User,Instructor,Student


@app.route("/courses")
def courses():
    all=Course.query.all()
    courses=[]
    for course in all:
        courses.append(course.to_dict(rules=("-instructor","-students")))
    return courses

@app.route("/courses/<int:id>")
def course_by_id(id):
    course=Course.query.filter(Course.id==id).first()
    if course==None:
        return {}, 404
    return course.to_dict(rules=("-instructor.profile_pic","-instructor.tenured","-instructor.user_id"))

@app.route("/instructors")
def instructors():
    all=Instructor.query.all()
    instructors=[]
    for instructor in all:
        instructors.append(instructor.to_dict())
    return instructors

@app.route("/students")
def students():
    all=Student.query.all()
    students=[]
    for student in all:
        students.append(student.to_dict())
    return students

@app.route("/students/<int:id>")
def get_student_by_id(id):
    student=Student.query.filter(Student.id==id).first()
    if not student:
        return {},404
    return student.to_dict()

