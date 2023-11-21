from behave import *
from selenium.webdriver.common.by import By
import time


@given(u'I got navigated to home page')
def step_impl(context):
    expected_title = "Your Store"
    assert context.driver.title.__eq__(expected_title)


@when(u'I enter valid product into search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP LP3065")


@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@id='search']//button").click()


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    time.sleep(5)



@when(u'I enter Invalid product in search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")


@then(u'Proper message should be displayed in search results')
def step_impl(context):
    expected_text = "There is no product that matches the search criteria."
    assert (context.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p")
            .text.__eq__(expected_text))



@when(u"I don't enter any product in search box field")
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
