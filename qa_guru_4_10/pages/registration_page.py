import os

from selene import browser, command, have

from qa_guru_4_10.data import Student


class Student_Registration_Page_Steps:

    def found_td(self, value1, value2):
        browser.all('.table tr').element_by_its('td', have.exact_text(value1)).all('td')[1].should(
            have.exact_text(value2))
        return self

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('#fixedban').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, value):
        browser.element('#genterWrapper label').should(have.exact_text(value)).click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__day--005').should(have.exact_text(str(day))).click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.getcwd() + value)
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    def registration(self, student: Student):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.fill_email(student.email)
        self.select_gender(student.gender)
        self.fill_mobile(student.mobile)
        self.fill_date_of_birth(student.year_of_birth, student.month_of_birth, student.day_of_birth)
        self.fill_subjects(student.subjects)
        self.select_hobbies(student.hobbies)
        self.upload_picture(student.picture)
        self.fill_current_address(student.address)
        self.select_state(student.state)
        self.select_city(student.city)
        self.submit()

    def should_have_registered_user_with(self, full_name, email, gender, mobile, date, subject, hobbies, picture,
                                         adress,
                                         state_and_city):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

        self.found_td('Student Name', full_name)
        self.found_td('Student Email', email)
        self.found_td('Gender', gender)
        self.found_td('Mobile', mobile)
        self.found_td('Date of Birth', date)
        self.found_td('Subjects', subject)
        self.found_td('Hobbies', hobbies)
        self.found_td('Picture', picture)
        self.found_td('Address', adress)
        self.found_td('State and City', state_and_city)
