from qa_guru_4_10.data import Student
from qa_guru_4_10.pages.registration_page import Student_Registration_Page_Steps

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
    picture='/img/one.png',
    address='Rome, Italy',
    state='Uttar Pradesh',
    city='Agra'
)


def test_registration_form():
    registration_page = Student_Registration_Page_Steps()
    registration_page.open()

    # WHEN
    registration_page.registration(student)

    # THEN
    registration_page.should_have_registered_user_with(
        'Ivan Petrov',
        'petrov@abc.com',
        'Male',
        '7123456789',
        '05 January,1917',
        'Maths',
        'Sports',
        'one.png',
        'Rome, Italy',
        'Uttar Pradesh Agra'
    )
