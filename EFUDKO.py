from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException as UA
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Efudko(object):
    
    def boot(self):
        # Запуск браузера и переход на страницу порала ЭФЮДКО
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get("http://portal.efudko.dkz.cloud/wps/portal/!ut/p/c5/04_SB8K\
            8xLLM9MSSzPy8xBz9QJ_89PTUFP_SEv2CdEVFALCPJr8!/")

    def login(self, lgin, pw):
        # Вход в систему с заданными данными УЗ и переход на главную страницу ЭФЮДКО
        user_id = self.driver.find_element_by_name('wps.portlets.userid')
        user_id.send_keys(lgin)
        password = self.driver.find_element_by_name('password')
        password.send_keys("2")
        password.clear()
        password.send_keys(pw)
        login_btn = self.driver.find_element_by_name('ns_7_CGAH47L00GNRC0I4B42HGB20E4__login')
        login_btn.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT,"ППК ЭФЮДКО")))
        EFUDKO_tab = self.driver.find_element_by_link_text('ППК ЭФЮДКО')
        EFUDKO_tab.click()
        try:
            efudko_iframe = self.driver.find_element_by_name("EFUDKO Viewer")
        except UA:
            self.driver.refresh()
            efudko_iframe = self.driver.find_element_by_name("EFUDKO Viewer")
        self.driver.switch_to.frame(efudko_iframe)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH,"//input[@name='j_username']")))
        user_id = self.driver.find_element_by_xpath("//input[@name='j_username']")
        user_id.send_keys("efdmanagerca")
        password = self.driver.find_element_by_xpath("//input[@name='j_password']")
        password.send_keys("2")
        password.clear()
        password.send_keys("2wsx2WSX")
        login_btn = self.driver.find_element_by_xpath("//input[@name='save']")
        login_btn.click()

    def close(self):
        # Закрытие браузера
        self.driver.close()

    def doc_kit_creation(self, lgin, pw):
        # Создание комплекта документов КО
        self.login(lgin, pw)
        self.driver.switch_to.default_content()
        doc_load_tab = self.driver.find_element_by_link_text('Загрузка внутренних ЭД')
        doc_load_tab.click()
        efudko_iframe = self.driver.find_element_by_name("EFUDKO Viewer")
        self.driver.switch_to.frame(efudko_iframe)
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(
            (By.LINK_TEXT,"×")))
        close_btn = self.driver.find_element_by_link_text('×')
        close_btn.click()
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(
            (By.XPATH,"//input[@*[starts-with(name(), 'jquery')]='141']")))
        proc_type = self.driver.find_element_by_xpath("//input[@*[starts-with(name(), 'jquery')]='141']")
        proc_type.send_keys('1100')
        proc_type.send_keys(Keys.DOWN)
        proc_type.send_keys(Keys.RETURN)
        resp_office = self.driver.find_element_by_xpath("//input[@*[starts-with(name(), 'jquery')]='185']")
        resp_office.send_keys('74')
        resp_office.send_keys(Keys.DOWN)
        resp_office.send_keys(Keys.RETURN)
        org_name = self.driver.find_element_by_xpath("//input[@*[starts-with(name(), 'jquery')]='119']")
        org_name.send_keys('1115')
        time.sleep(1)
        org_name.send_keys(Keys.DOWN)
        org_name.send_keys(Keys.RETURN)    
        explan_msg = self.driver.find_element_by_xpath("//input[@*[starts-with(name(), 'jquery')]='74']")
        explan_msg.send_keys('Тестирование ' + self.driver.session_id) 
        add_doc = self.driver.find_element_by_xpath("//button[@*[starts-with(name(), 'jquery')]='26']")
        add_doc.click()
        doc_upload = self.driver.find_element_by_xpath("//input[@*[starts-with(name(), 'jquery')]='211']")
        doc_folder = "C:\\Users\\aerofeev\\Downloads\\"
        doc_to_upload = doc_folder + "6921.pdf"
        doc_upload.send_keys(doc_to_upload)
        doc_type = self.driver.find_element_by_xpath("//input[@*[starts-with(name(), 'jquery')]='222']")
        doc_type.send_keys('11102')
        doc_type.send_keys(Keys.DOWN)
        doc_type.send_keys(Keys.RETURN)      
        submit_btn = self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-lg']")
        submit_btn.click()

    def del_and_restore(self):
        # Удаление и восстановление комплекта документов КО
        user_id = self.driver.find_element_by_name('wps.portlets.userid')
        user_id.send_keys("efdOperatorDelED")
        password = self.driver.find_element_by_name('password')
        password.send_keys("2")
        password.clear()
        password.send_keys("2wsx2WSX")
        login_btn = self.driver.find_element_by_name('ns_7_CGAH47L00GNRC0I4B42HGB20E4__login')
        login_btn.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT,"ППК ЭФЮДКО")))
        EFUDKO_tab = self.driver.find_element_by_link_text('ППК ЭФЮДКО')
        EFUDKO_tab.click()
        kit_del = self.driver.find_element_by_xpath("//a[text()='Удаление комплектов ']")
        kit_del.click()
        efudko_iframe = self.driver.find_element_by_name("EFUDKO Viewer")
        self.driver.switch_to.frame(efudko_iframe)
        kit_n = '000000103708'
        kit_name = 'EFDKO_RegKOCreation_' + kit_n
        kit_number = self.driver.find_element_by_xpath("//input[@tkPid='19']")
        kit_number.click()
        kit_number.send_keys(kit_n[:2])
        kit_number.click()
        kit_number.send_keys(kit_n[:2])
        kit_number.click()
        kit_number.send_keys(kit_n[:2])
        kit_number.send_keys(kit_n[6:8])
        kit_number.click()
        kit_number.send_keys(kit_n[8:10])
        kit_number.send_keys(kit_n[10:])
        find_btn = self.driver.find_element_by_xpath("//div[@tkPid='23']")
        find_btn.click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
            (By.XPATH,"//div[@tkPid='55']")))
        del_btn = self.driver.find_element_by_xpath("//div[@tkPid='55']")
        del_btn.click()
        del_btn = self.driver.find_element_by_xpath("//div[@tkPid='61']")
        del_btn.click()
        self.driver.switch_to.default_content()
        trash = self.driver.find_element_by_xpath("//a[text()='Корзина ']")
        trash.click()
        time.sleep(2)
        efudko_iframe = self.driver.find_element_by_name("EFUDKO Viewer")
        self.driver.switch_to.frame(efudko_iframe)
        more_btn = self.driver.find_element_by_xpath("//td[text()='" + kit_name + "']/../td/button")
        more_btn.click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
            (By.XPATH,"//div[@tkPid='117']")))
        restore_btn = self.driver.find_element_by_xpath("//div[@tkPid='117']")
        restore_btn.click()
        restore_btn = self.driver.find_element_by_xpath("//div[@tkPid='122']")
        restore_btn.click()


if __name__ == '__main__':
    efudko = Efudko()
    efudko.boot()
    efudko.login("efdmanagerca", "2wsx2WSX")
    efudko.del_and_restore()
    efudko.close()