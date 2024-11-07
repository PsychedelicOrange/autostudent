from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
from datetime import datetime
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")

option.add_argument("start-maximized")

option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", 
{"profile.default_content_setting_values.notifications": 2 
 }) 

driver = webdriver.Chrome(options=option,executable_path='C:\\Users\\parth\\code\\python\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(120)
driver.get('https://teams.microsoft.com/_?culture=en-us&country=US&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school//?ctx=teamsGrid');
email = driver.find_element_by_css_selector('#i0116')
email.send_keys("<INSERT_EMAIL>")
email.send_keys(Keys.ENTER)
passwd = driver.find_element_by_css_selector('#i0118')
passwd.send_keys("<INSERT PASSWORD>")
passwd_submit = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input')
def jitterclick(button):
    attempts = 0;
    while attempts < 10 :
        try :
            button.click();
            break;
        except :
            nothing = 1
        attempts += 1
jitterclick(passwd_submit)
yes = driver.find_element_by_css_selector('#idSIButton9')
jitterclick(yes)

def clickon_team(term) :
    driver.find_element_by_css_selector('#control-input').click()
    driver.find_element_by_css_selector('#searchInputField').send_keys(term)
    time.sleep(2)
    driver.find_element_by_css_selector('#autosuggest-id-1 > span:nth-child(2) > button').click()
def join():
     driver.find_element_by_css_selector('#m1616221047901 > calling-join-button > button').click()
     driver.find_element_by_css_selector('#ngdialog2 > div.ngdialog-content > div > div > div > div.content > div > div > div.buttons-wrapper > div > button').click()
     driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()
     driver.find_element_by_css_selector('#page-content-wrapper > div.flex-fill > div > calling-pre-join-screen > div > div > div.ts-calling-pre-join-content > div.central-section > div.video-and-name-input > div > div > section > div.flex-fill.input-section > div > div > button').click()

def leave_lecture(term):
    driver.find_element_by_css_selector('#hangup-button > ng-include > svg').click()
    driver.get('https://teams.microsoft.com/_?culture=en-us&country=US&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/school//?ctx=teamsGrid');

def join_lecture(team):
    if(team == 'MOS'):
        clickon_team('MOS G')
        
    if(team == 'MAT'):
        clickon_team('P Q R _')
        
    if(team == 'CPI'):
        clickon_team('CPI_Sem_')
        
    if(team == 'BEL'):
        clickon_team('BE_')
        
    if(team =='PHY'):
        clickon_team('Engineering Phy')
        
    if(team == 'ENG'):
        clickon_team('R section.')
        
    if(team == 'BME'):
        clickon_team('BME Tea') 
    join()
'''
#schedule
def check_time():    
    day = datetime.today().strftime("%A")
    time = datetime.now().strftime("%H:%M")
    if (day == 'Monday') & (time == '07:54') :
        join_lecture('MOS')
    if (day == 'Monday') & (time == '09:32') :
        leave_lecture('MOS')
    if (day == 'Monday') & (time == '09:53') :
        leave_lecture('BEL')
    if (day == 'Monday') & (time == '11:33') :
        leave_lecture('MOS')
        
    if (day == 'Tuesday') & (time == '13:55') :
        join_lecture('BME')
    if (day == 'Tuesday') & (time == '15:34') :
        leave_lecture('MOS')
    if (day == 'Tuesday') & (time == '15:50') :
        leave_lecture('MAT')
    if (day == 'Tuesday') & (time == '18:05') :
        leave_lecture('MOS')
        
    if (day == 'Wednesday') & (time == '07:54') :
        join_lecture('PHY')
    if (day == 'Wednesday') & (time == '09:32') :
        leave_lecture('MOS')
    if (day == 'Wednesday') & (time == '09:53') :
        leave_lecture('ENG')
    if (day == 'Wednesday') & (time == '11:33') :
        leave_lecture('MOS')
        
    if (day == 'Thursday') & (time == '13:55') :
        join_lecture('MOS')
    if (day == 'Thursday') & (time == '15:34') :
        leave_lecture('MOS')
    if (day == 'Thursday') & (time == '15:50') :
        leave_lecture('BEL')
    if (day == 'Thursday') & (time == '17:35') :
        leave_lecture('MOS')

    if (day == 'Friday') & (time == '07:54') :
        join_lecture('PHY')
    if (day == 'Friday') & (time == '09:32') :
        leave_lecture('MOS')
    if (day == 'Friday') & (time == '09:53') :
        leave_lecture('ENG')
    if (day == 'Friday') & (time == '11:33') :
        leave_lecture('MOS')

    if (day == 'Saturday') & (time == '13:55') :
        join_lecture('PHY')
    if (day == 'Saturday') & (time == '15:34') :
        leave_lecture('MOS')
    if (day == 'Saturday') & (time == '15:50') :
        leave_lecture('CPI')
    if (day == 'Saturday') & (time == '17:35') :
        leave_lecture('MOS')


schedule.every().minute.do(check_time)
while True:
    schedule.run_pending()
'''

