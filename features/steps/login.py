from behave import *
from selenium.webdriver.common.by import By
import time
from datetime import datetime


@given(u'I got navigate to login page')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT,"Login").click()


@when(u'I enter valid email id and valid password into the fields')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("saik@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Saikiran")


@when(u'I click on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then(u'I should logged in')
def step_impl(context):
    time.sleep(2)
    assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()


@given(u'I got navigated to login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'I enter invalid email id and valid password into the fields')
def step_impl(context):
    time.sleep(3)
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_email = "sai" + time_stamp + "@gmail.com"
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(invalid_email)
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Saikiran")


@then(u'I should get Proper warning message Invalid Email id')
def step_impl(context):
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]")
            .text.__contains__(expected_warning_msg))


@when(u'I enter valid email id and invalid password into fields')
def step_impl(context):
    time.sleep(3)
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    invalid_password = "sai" + time_stamp + "12345"
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("saik@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(invalid_password)


@then(u'I should get proper warning message Invalid Password')
def step_impl(context):
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]")
            .text.__contains__(expected_warning_msg))


@when(u'I not enter email id and password into fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")
    context.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")


@then(u'I should get proper warning message Enter Email id and Password')
def step_impl(context):
    expected_warning_msg = "Warning: No match for E-Mail Address and/or Password."
    assert (context.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]")
            .text.__contains__(expected_warning_msg))