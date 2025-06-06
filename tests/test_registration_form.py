import os
import pytest
from selene import browser, have, be, have

@pytest.fixture(scope="function", autouse=True)
def browser_settings():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config_height = 1080
    yield
    browser.quit()


def test_submit_form():
    # открыть форму
    browser.open("/automation-practice-form")

    # заполнить форму
    browser.element('#firstName').type('Vika')
    browser.element('#lastName').type('Zhuchkova')
    browser.element('#userEmail').type('vika.zh@gmail.com')
    browser.element('[for=gender-radio-2]').click()
    browser.element('#userNumber').type('9881112345')

    # выбрать дату рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="9"').click() # октябрь
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1994"').click()  # 1994
    browser.element('.react-datepicker__day--001').click()  # день 1

    # заполнить форму subjects
    browser.element('#subjectsInput').type('English').press_enter()

    # выбрать хобби
    browser.element('[for=hobbies-checkbox-1]').click() # Sports

    # загрузка картинки
    browser.element('#uploadPicture').send_keys(os.path.abspath('testpion.jpeg'))

    # заполнить адрес
    browser.element('#currentAddress').type('Test address 789')

    # выбрать State and City
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    # отправить форму
    browser.element('#submit').click()

    # проверить данные
    browser.element('.table').should(have.text('Vika Zhuchkova'))
    browser.element('.table').should(have.text('vika.zh@gmail.com'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('9881112345'))
    browser.element('.table').should(have.text('01 October,1994'))  # Добавлено: проверка даты
    browser.element('.table').should(have.text('English'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('Test address 789'))
    browser.element('.table').should(have.text('Uttar Pradesh Agra'))



