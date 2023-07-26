from config import app,db
from models import Course,User,Instructor,Student,Enrollment
from faker import Faker
from random import randint, choice as rc

faker=Faker()

with app.app_context():

    Enrollment.query.delete()
    Course.query.delete()
    Instructor.query.delete()
    Student.query.delete()
    User.query.delete()

    course_titles=["math","science","social studies","english"]
    courses=[]
    for course_title in course_titles:
        course=Course(title=course_title)
        courses.append(course)
        db.session.add(course)
    db.session.commit()

    profile_pics=["https://www.incimages.com/uploaded_files/image/1920x1080/getty_481292845_77896.jpg","https://cdn2.psychologytoday.com/assets/styles/manual_crop_1_91_1_1528x800/public/field_blog_entry_images/2018-09/shutterstock_648907024.jpg?itok=7lrLYx-B","https://cdn.shopify.com/s/files/1/0850/2114/files/tips_to_help_heighten_senses_480x480.png?v=1624399167","https://www.dmarge.com/wp-content/uploads/2021/01/dwayne-the-rock-.jpg"]
    instructors=[]
    for i in range(10):
        instructor=Instructor(fname=faker.first_name(),lname=faker.last_name(),age=randint(18,65),profile_pic=rc(profile_pics))
        instructors.append(instructor)
        db.session.add(instructor)
    db.session.commit()

    for course in courses:
        course.instructor=rc(instructors)
    db.session.commit()

    students=[]
    for i in range(500):
        student=Student(fname=faker.first_name(),lname=faker.last_name(),age=randint(18,65),profile_pic=rc(profile_pics))
        students.append(student)
        db.session.add(student)
    db.session.commit()

    for i in range(25):
        student=rc(students)
        course=rc(courses)
        if course not in student.courses:
            student.courses.append(course)
    db.session.commit()
