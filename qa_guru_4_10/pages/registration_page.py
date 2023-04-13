import os

from selene import browser, command, have


class StudentRegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.element('#fixedban').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def select_gender(self, value):
        browser.element('#genterWrapper label').should(have.exact_text(value)).click()

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__day--005').should(have.exact_text(str(day))).click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.getcwd() + value)

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    def should_have_registered_user_with(self, full_name, email, gender, mobile, date, subject, hobbies, picture,
                                         adress,
                                         state_and_city):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.all('.table tr').element_by_its('td', have.exact_text('Student Name')).all('td')[1].should(
            have.exact_text(full_name))
        browser.all('.table tr').element_by_its('td', have.exact_text('Student Email')).all('td')[1].should(
            have.exact_text(email))
        browser.all('.table tr').element_by_its('td', have.exact_text('Gender')).all('td')[1].should(
            have.exact_text(gender))
        browser.all('.table tr').element_by_its('td', have.exact_text('Mobile')).all('td')[1].should(
            have.exact_text(mobile))
        browser.all('.table tr').element_by_its('td', have.exact_text('Date of Birth')).all('td')[1].should(
            have.exact_text(date))
        browser.all('.table tr').element_by_its('td', have.exact_text('Subjects')).all('td')[1].should(
            have.exact_text(subject))
        browser.all('.table tr').element_by_its('td', have.exact_text('Hobbies')).all('td')[1].should(
            have.exact_text(hobbies))
        browser.all('.table tr').element_by_its('td', have.exact_text('Picture')).all('td')[1].should(
            have.exact_text(picture))
        browser.all('.table tr').element_by_its('td', have.exact_text('Address')).all('td')[1].should(
            have.exact_text(adress))
        browser.all('.table tr').element_by_its('td', have.exact_text('State and City')).all('td')[1].should(
            have.exact_text(state_and_city))
