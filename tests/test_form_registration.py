from qa_guru_4_10.data import Student
from qa_guru_4_10.pages.registration_page import StudentRegistrationPageSteps



student = Student(
    first_name='Ivan',
    last_name='Petrov',
    email='petrov@abc.com',
    gender='Male',
    mobile='7123456789',
    year_of_birth='1917',
    month_of_birth='January',
    day_of_birth='5',
    subjects='Maths',
    hobbies='Sports',
    picture='one.png',
    address='Rome, Italy',
    state='Uttar Pradesh',
    city='Agra'
)


def test_registration_form():
    registration_page = StudentRegistrationPageSteps()
    registration_page.open()

    # WHEN
    registration_page.registration(student)

    # THEN
    registration_page.should_have_registered_user_with(
        student.first_name + ' ' + student.last_name,
        student.email,
        student.gender,
        student.mobile,
        '0' + student.day_of_birth + ' ' + student.month_of_birth + ',' + student.year_of_birth,
        student.subjects,
        student.hobbies,
        student.picture,
        student.address,
        student.state + ' ' + student.city
    )
