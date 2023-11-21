from behave import *
from selenium.webdriver.common.by import By
import time


@given(u'I navigate to register page')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@when(u'I enter mandatory fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("Saikiran32")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Sri")
    context.driver.find_element(By.ID, "input-email").send_keys("SaikiranSri32@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("9123456981")
    context.driver.find_element(By.ID, "input-password").send_keys("Saikiran")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Saikiran")


@when(u'I Select Privacy Policy')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.NAME, "agree").click()


@when(u'I click on Register button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then(u'Account should be created')
def step_impl(context):
    expected_text = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)


@when(u'I enter all fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("Saikirann532")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Srii")
    context.driver.find_element(By.ID, "input-email").send_keys("Saikirann532222@gmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys("9123456234")
    context.driver.find_element(By.ID, "input-password").send_keys("Saikiranqq")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Saikiranqq")
    context.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()


@when(u'I enter all fields except email field')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("Ssaikirannn3222")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Sriiii")
    context.driver.find_element(By.ID, "input-telephone").send_keys("9123412345")
    context.driver.find_element(By.ID, "input-password").send_keys("Saikiran12")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Saikiran12")


@when(u'I enter existing email address on email field')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-email").send_keys("SaikiranSri32@gmail.com")


@then(u'I should get proper warning message')
def step_impl(context):
    expected_warning_msg = "Warning: E-Mail Address is already registered!"
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
            .text.__contains__(expected_warning_msg))
    time.sleep(2)


@when(u'I dont enter anything into fields')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


@then(u'I should get Proper warning message every mandatory fields should be displayed')
def step_impl(context):
    expected_warning_msg_empty_fields = "Warning: You must agree to the Privacy Policy!"
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
            .text.__contains__(expected_warning_msg_empty_fields))
    time.sleep(2)


@when(u'I click on Policy check box')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.NAME, "agree").click()


@then(u'I should get Proper warning message are you an existing user')
def step_impl(context):
    expected_warning_msg_empty_fields_with_policy = "If you already have an account with us, please login at the login page."
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]")
            .text.__contains__(expected_warning_msg_empty_fields_with_policy))
    time.sleep(2)