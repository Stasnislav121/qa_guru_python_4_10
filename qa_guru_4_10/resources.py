import tests
from selene import browser, command


class StudentRegistrationPage:

    def open(self):
        browser.config.window_width = 1080
        browser.config.window_height = 1440
        browser.config.base_url = 'https://demoqa.com'
        browser.config.hold_browser_open = True
        browser.element('#fixedban').perform(command.js.remove)