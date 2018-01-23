'''
Site:
Author:
Goal:
Date

'''

import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

#Activate the webdriver and use whatever Browser tickles your fancy
driver = webdriver.Chrome()

# COMMENT: adding the base url for the MarketWiseDailyReport here
base_url = 'http://agmarknet.nic.in/agnew/NationalBEnglish/MarketWiseDailyReport.aspx'
driver.get(base_url)

#Select the year
year = Select(driver.find_element_by_name('drpDwnYear'))
option =year.options
year.select_by_value('2016')

#Select the Month
month = Select(driver.find_element_by_name('drpDwnMonth'))
month.select_by_value('March')
#driver.refresh()

print (driver.current_url)

#bsObj = BeautifulSoup(html, "html.parser")
#bsObj2 = bsObj.prettify()

# TODO: Find the total number of days in this Month
# TODO: Add code that checks to see if there is a link in the location
# TODO: Write a for loop that goes through each day that have a link

driver.find_element_by_link_text("5").click() #code will be changed once for loop is added

################################
#2. This is the point where all state values are selected
##############################

select_box = driver.find_element_by_name('ListBox1') #Find the forms
all_options = select_box.find_elements_by_tag_name("option") #Find all the options values
for option in all_options: #Prints and clicks all of them
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
driver.find_element_by_name('Submit_list').click()

################################
#3. This is the point where all markets are selected
##############################

table = driver.find_element_by_id("GridView1")
all_options = table.find_elements_by_tag_name('td')

count = 1
for option in all_options[:900]:
    try:
        tag = option.find_element_by_tag_name('input')
        tag.click()
        print("Clicking Market {}: {}".format(count, option.text))
        count += 1
    except:
        print("\n******************************************")
        print(option.text)
        print("******************************************\n")
    #option.click()

    #print("Clicking Market {}: {}".format(count, option.text))
    #count += 1
# TODO: Get the current url or tell the page to go back to re-rerunthe function
# TODO: Trun this option click and submit into a command
# TODO: split the options list into even group of many 10 and run the funciton on each of them
#to avoid timing out.

driver.find_element_by_name('btnSubmit').click()

# TODO: Save the output either as an XML or a CSV. Save to a folder

#bsObj = BeautifulSoup(html, "html.parser")
#bsObj2 = bsObj.prettify()

#print(bsObj2)





#response = mechanize.urlopen("http://www.facebook.com")
#print response.read()

#response.select_form(id="login_form")
#print(response.form)

#br.select_form(name="order") #the sign up form in github is in third position(search and sign in formscome before signup)
'''
This code use mechanize.Browser(). But mechanize cannot handle javascript generated fields. So above is the code for use selenium to scrub the site of data.

#import mechanize
#from selenium import webdriver
#from urllib2 import urlopen

br = mechanize.Browser()
br.set_handle_robots(False) #ignore robots.txt
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.open("http://agmarknet.nic.in/agnew/NationalBEnglish/MarketWiseDailyReport.aspx")
assert br.viewing_html()

br.select_form(name="form1")
#br['drpDwnYear'] = 2018
#br['drpFwnMonth'] = 'January'
form = br.form
form['drpDwnYear'] = ['2017']
form['drpDwnMonth'] = ['March']
br.submit
print(br.response().read())
#br.open(br.geturl())

#response = br.submit()
#br.open(response.geturl())
#br.open(response.geturl())
#br.select_form(name="form1")

#print(br.form)

#response2 = br.submit()
'''
