from qa_guru_4_10.pages.registration_page import StudentRegistrationPage
from selene import browser

from utils import attach


def test_registration_form_():
    registration_page = StudentRegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Petrov')
    registration_page.fill_email('petrov@abc.com')
    registration_page.select_gender('Male')
    registration_page.fill_mobile('7123456789')
    registration_page.fill_date_of_birth("1917", "January", "5")
    registration_page.fill_subjects('Maths')
    registration_page.select_hobbies('Sports')
    registration_page.upload_picture('one.png')
    registration_page.fill_current_address('Rome, Italy')
    registration_page.select_state('Uttar Pradesh')
    registration_page.select_city('Agra')
    registration_page.submit()

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
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
