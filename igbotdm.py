#Project5k dm bot

from selenium import webdriver;
from time import sleep;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#must set up path based on where you have your chrome!
PATH = "/Users/sarinali/Downloads/chromedriver" 
driver = webdriver.Chrome(PATH);
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher'); 
sleep(2);

#type in username
username = driver.find_element_by_name('username');
username.send_keys('ur username'); 
sleep(2);

#type in password
password = driver.find_element_by_name('password');
password.send_keys('ur pass'); 
sleep(1);

#logs in
submit = driver.find_element_by_tag_name('form');
submit.submit();
sleep(3);

#goes to messages section
message = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')));
message.click(); 
sleep(3);

#closes pop up
notnow = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')));
notnow.click(); 
sleep(3);

# put your list of users here in this format: 'username',
users = ['sarinastoenail', 'rogers_fan.page'];
#individually dms each of the usernames in the list
for i in range(len(users)):
    # clicks the write message icon
    message = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')));
    message.click();
    sleep(2);
    # searches the username
    person = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')));
    person.send_keys(users[i]);
    sleep(2);
    # selects the account
    select = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//html/body/div[5]/div/div/div[2]/div[2]/div/div')));
    select.click();
    sleep(2);
    #presses next
    nxt = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button')));
    nxt.click();
    sleep(2);
    # IMPORTANT: PUT YOUR MESSAGE HERE!! (in text.send_keys(*your message*)
    text = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')));
    text.send_keys('hello :D');
    sleep(2);
    # sends the message
    send = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')));
    send.click();
    sleep(2); 
