import os

from selene import browser, have, command


def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Petrov')
    browser.element('#userEmail').type('petrov@abc.com')
    browser.element('#genterWrapper label').should(have.exact_text('Male')).click()
    browser.element('#userNumber').type('7123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-dropdown-container').click()
    browser.element('.react-datepicker__month-select option[value = "0"]').click()
    browser.element('.react-datepicker__year-dropdown-container').click()
    browser.element('.react-datepicker__year-select option[value = "1917"]').click()
    browser.element('.react-datepicker__day--005').should(have.exact_text('5')).click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/img/one.png')
    browser.element('#currentAddress').type('Rome, Italy')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').perform(command.js.click)

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Student Name')).all('td')[1].should(
        have.exact_text('Ivan Petrov'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Student Email')).all('td')[1].should(
        have.exact_text('petrov@abc.com'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Gender')).all('td')[1].should(
        have.exact_text('Male'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Mobile')).all('td')[1].should(
        have.exact_text('7123456789'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Date of Birth')).all('td')[1].should(
        have.exact_text('05 January,1917'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Subjects')).all('td')[1].should(
        have.exact_text('Maths'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Hobbies')).all('td')[1].should(
        have.exact_text('Sports'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Picture')).all('td')[1].should(
        have.exact_text('one.png'))
    browser.all('.table tr').element_by_its('td', have.exact_text('Address')).all('td')[1].should(
        have.exact_text('Rome, Italy'))
    browser.all('.table tr').element_by_its('td', have.exact_text('State and City')).all('td')[1].should(
        have.exact_text('Uttar Pradesh Agra'))
