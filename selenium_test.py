import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('/Users/danielsullivan/Documents/Selenium/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://mueller-qa.cerebri.systems/');
#time.sleep(2) # Let the user actually see something!
recommended_products = driver.find_element_by_xpath("//a[@href='/recommendedproducts']")

def frame_switch(id):
  driver.switch_to.frame(driver.find_element_by_css_selector(id))

#Click "Build Your Dream
recommended_products.click()
#time.sleep(2) # Let the user actually see something!

#Click the Facebook login button
facebook_button = driver.find_element_by_xpath("//img[@src='/MuellerProducts-portlet/image/social-facebook.png']")
facebook_button.click()
#time.sleep(2)

#Enter in Facebook username and password
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
login_button = driver.find_element_by_name("login")
username.send_keys("esinschmeling@gmail.com")
password.send_keys("44484448")
login_button.click()

#On the second login screen, enter phone number, ZIP Code, select buildings, and submit
phone = driver.find_element_by_id("_customerportalregistration_WAR_MuellerProductsportlet_Phone")
zip = driver.find_element_by_id("_customerportalregistration_WAR_MuellerProductsportlet_zip-code")
buildings_button = driver.find_element_by_xpath("//label[@for='buildings-radio']")
submit = driver.find_element_by_name("Submit")

phone.send_keys("9879877787")
zip.send_keys("75142")
buildings_button.click()
submit.click()

#Click the first product on the Recommended Products page
first_product = driver.find_element_by_xpath("//div[@class='layout-images']/a[1]")
first_product.click()

#Click the close overlay button
dismiss_button = driver.find_element_by_id("CloseOverlay")
dismiss_button.click()

#Add the product and education doc to the Checklist
add_to_checklist = driver.find_element_by_id("checklistBtn")
education_search = driver.find_element_by_id("EducationSearch")
education_search_button = driver.find_element_by_id("EducationSearchGo")

driver.execute_script("arguments[0].click();", add_to_checklist)
education_search.send_keys("a")
driver.execute_script("arguments[0].click();", education_search_button)

time.sleep(1)
first_article = driver.find_element_by_xpath("//ul[@id='searchResult']/li[2]")
first_article.click()
time.sleep(1)
doc_checklist = driver.find_element_by_id("AddDocToChecklist")
doc_checklist.click()
time.sleep(1)

#Open checklist
view_checklist = driver.find_element_by_id("ViewChecklist")
view_checklist.click()
driver.implicitly_wait(3)


frame_switch("iframe.dialog-iframe-node ")

#Fill in fields
time_frame = driver.find_element_by_xpath("//select[@id='_recommendedproducts_WAR_MuellerProductsportlet_project_timeline']")
land_checkbox = driver.find_element_by_xpath("//input[@id='_recommendedproducts_WAR_MuellerProductsportlet_check_landCheckbox']")

land_checkbox.click()
time_frame.select_by_index(2)





#View the Checklist

#Fill out all unfilled fields

#Submit the checklist

time.sleep(10) # Let the user actually see something!
driver.quit()
