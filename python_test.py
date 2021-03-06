# -*- coding: utf-8 -*-

import time
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class ReadConfig:
    def __init__(self,filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.dirname(os.path.abspath('.'))
            configpath = "config.ini"
        
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)
     
    

    def get_path(self):
        value = self.cf.get("PATH","url")
        return value

    def use_passwd(self,userid):
        value = self.cf.get(userid,"passwd")
        return value

    def use_users(self,users):

        count = 0
        while (count < 3):
            
            value = self.cf.get(str(count),"user")
            count = count + 1
            if value == users:
                break

        userid = count

        return userid





class guoshui_infos:

    def __init__(self,config_path):
        url = "https://etax.beijing.chinatax.gov.cn/xxmh/html/index.html"
        self.url = url
        Iedriver_path = config_path
        capabilities = DesiredCapabilities.INTERNETEXPLORER
        capabilities.pop("platform",None)
        capabilities.pop("version",None)
        capabilities['excludeSwitches'] = "enable-automation"
        self.browser = webdriver.Ie(executable_path=Iedriver_path, capabilities=capabilities)
        self.wait = WebDriverWait(self.browser, 10) 
        self.browser.get(self.url)



    def login(self):

 
        self.browser.get(self.url)
    
        self.browser.implicitly_wait(5)
        if self.isElementPresent("class","layui-layer-btn0"):
     
           self.browser.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()

           self.browser.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()

           self.browser.find_element_by_xpath('//*[@class="dlbox"]').click()

        else:
           self.browser.find_element_by_xpath('//*[@class="loginico"]').click()
 

    def check_login(self):

        self.browser.switch_to_default_content()
        if self.isElementPresent("class","bjDzswjShowDiv"):
            return True
        else:
            return False

    def again_login(self):

        count = 0
        while count <5:
            self.browser.switch_to_default_content()
            self.browser.implicitly_wait(5)
            if self.isElementPresent("class","bjDzswjShowDiv") == False:
                if self.isElementPresent("class","layui-layer-btn0"):
            
                    self.browser.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()

                    self.browser.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()

                    self.browser.find_element_by_xpath('//*[@class="dlbox"]').click()

                else:
                    self.browser.find_element_by_xpath('//*[@class="loginico"]').click()

                if check_login():
                    count = 0
                    break
                else:
                    count += 1
            else:
                kehu_password = R_config.use_passwd("1")
                self.passwdwrite(kehu_password)
                count = 0
                break








    def user_input(self):

        self.browser.implicitly_wait(10)
        User_address = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div#bjDzswjShowDiv > div.logindiv > div.bjDzswjShowDiv')))
        print(User_address.text)
        print("user input")

        return User_address.text

            
                
        


    def passwdwrite(self,kuhu_password):      


        self.browser.implicitly_wait(10)
        self.browser.find_element_by_name('CapassWord').send_keys(kehu_password)
        time.sleep(1)
        self.browser.execute_script("dzswjLogin()")


    def declare(self):

        self.browser.implicitly_wait(10)
        Timely_declaration = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div#cygn > ul > li:first-child > a')))
        print(Timely_declaration.get_attribute('onclick'))
        self.browser.execute_script(Timely_declaration.get_attribute('onclick'))

        self.browser.switch_to.frame("ifrMain")
        self.browser.switch_to.frame("lhsbIframe")
        read_complete = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.white_content')))
        self.browser.execute_script("closeDialog()")


        write_VAT_declare = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.searchbox table tr:nth-child(2) td:nth-child(8)>a'))) #> table > tbody > tr:nth-child(2) > td:nth-child(8) > a')))
        print(write_VAT_declare.get_attribute('href'))
        self.browser.execute_script(write_VAT_declare.get_attribute('href'))

        self.browser.switch_to_default_content()
        self.browser.switch_to.frame("ifrMain")
        if self.isElementPresent("id","layui-layer1"):
            write_text1_declare = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#layui-layer1 .win-center>.layui-table>tbody>tr:nth-child(2)>td:nth-child(2)>button')))# win-center tbody tr:nth-child(2) td:nth-child(2)')))
        else:
            write_text1_declare = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#layui-layer2 .win-center>.layui-table>tbody>tr:nth-child(2)>td:nth-child(2)>button')))
        print(write_text1_declare.get_attribute('onclick'))
        self.browser.execute_script(write_text1_declare.get_attribute('onclick'))


    def jump_web(self):

        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[-1])
        write_text2_declare = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#layui-layer1')))
        print(write_text2_declare.text)
        self.browser.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()
        
    def read_one(self):
        self.browser.switch_to_default_content()
        write_text3_declare = WebDriverWait(self.browser,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'table>tbody>tr>td:nth-child(2)>li:nth-child(2)>a')))
        print(write_text3_declare.text)
        self.browser.execute_script(write_text3_declare.get_attribute('onclick'))
        self.browser.switch_to_default_content()
        self.browser.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()
  
        self.browser.execute_script("javascript:window.frames[0].refresh();")
  
        self.browser.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()
 
        self.browser.execute_script("javascript:window.frames[0].prepareForm();")

        self.browser.switch_to_default_content()
        self.browser.find_element_by_xpath('//*[@id="btnSave"]').click()
        self.browser.execute_script("javascript:window.frames[0].prepareForm();")
   
        self.browser.switch_to_default_content()
      
        self.browser.switch_to.frame("frmMain")
        self.browser.find_element_by_xpath('//*[@id="Message_btn_0"]').click()



    def declare_end(self):
        time.sleep(5)
        self.browser.switch_to_default_content()
        self.browser.switch_to.frame("frmMain")
        self.browser.find_element_by_xpath('//*[@id="fyyqfkgz"]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="yydTsjjdjxx"]').click()
        time.sleep(1)
        self.browser.find_element_by_xpath('//*[@id="closeTsjjdjxx"]').click()
        self.browser.switch_to_default_content()
        self.browser.find_element_by_xpath('//*[@id="btnPrepareMake"]').click()
        
        
       

    def isElementPresent(self,by,value):

        try:
            element = self.browser.find_element(by=by,value=value)
  
        except NoSuchElementException as e:

            return False
        else:
            return True

class sys_kill:

    def __init__(self):
        os.system("taskkill /F /im iexplore.exe")
        time.sleep(1)
        os.system("taskkill /F /im IEDriverServer.exe")
 



if __name__ == "__main__":
    
    print("##################################\n")
    print("#########This is script!##########\n")
    print("##################################\n")
    print("waiting........\n")

    U_state_flag = False
    while 1:
        U_state = raw_input("请确认U盾是否插入:")
        if U_state == "yes":
            U_state_flag = True
        else:
            U_state_flag = False
        
        if U_state_flag:
            time.sleep(1)
            print("进入循环！\r\n")
            U_state_flag = False

            R_config = ReadConfig()
            Iedriver_path = R_config.get_path()
            if len(Iedriver_path) > 0:
                start = guoshui_infos(Iedriver_path)
            else:
                print("NoReadConfig:::配置文件路径出错:\r\n",str(Iedriver_path))
                break

            start.login()
            time.sleep(2)
            '''
            if start.check_login():
                kehu_password = R_config.use_passwd("1")
                start.passwdwrite(kehu_password)
            else:
                start.again_login()
                if start.check_login() == False:
                    sys = sys_kill()
                    print("网页打开过于迟缓，或者网页出现问题！\r\n")
                    continue
            '''
            kehu_password = R_config.use_passwd("1")
            start.passwdwrite(kehu_password)
            if start.isElementPresent("id","cygn"):
                start.declare()
            else:
                sys = sys_kill()
                print("网页打开过于迟缓，或者网页出现问题！\r\n")
                continue

            start.jump_web()
            time.sleep(1)
            start.read_one()
            start.declare_end()
            print("申报已完成!\r\n")
            sys = sys_kill()




            
                
            


            

                    


            

            

            


        


'''
    R_config = ReadConfig()
    print("Read config complated......\n")
    Iedriver_path = R_config.get_cf()
    print(Iedriver_path)
    print("PATH Loaded......\n")
    print(Iedriver_path)
    start = guoshui_infos(Iedriver_path)
    print("web start........\n")

    start.login()
    print("Login complated.......\n")
  #  time.sleep(4)
  #  users = start.user_input()


   # users_conf =  R_config.use_users(users)

    kehu_password = R_config.use_passwd("1")

    print(kehu_password)
    print("Get Password.........\n")
    start.passwdwrite()
    time.sleep(5)
    print("PassWord write OK..........\n")
    start.declare()

    time.sleep(2)
    start.jump_web()

    time.sleep(1)
    start.read_one()
    start.declare_end()
    print("coming!!!!!!!!")
'''
