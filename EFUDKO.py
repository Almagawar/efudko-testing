from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException as UA
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Efudko(object):
    
    def login(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.get("http://portal.efudko.dkz.cloud/wps/portal/!ut/p/c5/04_SB8K\
            8xLLM9MSSzPy8xBz9QJ_89PTUFP_SEv2CdEVFALCPJr8!/")
        user_id = self.driver.find_element_by_name('wps.portlets.userid')
        user_id.send_keys("efdmanagerca")
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
        self.driver.close()

    def elem_id(self):
        elem = self.driver.find_element_by_class_name('navigationPanel')
        return elem.get_attribute('id')

    def del_tab(self):
        del_tab = self.driver.find_element_by_link_text('На рассмотрении')
        del_tab.click() 

    def doc_kit_creation(self):
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

if __name__ == '__main__':
    efudko = Efudko()
    efudko.login()
    efudko.close()



# self.driver.execute_script("""var div1 = document.querySelector('div.col-xs-12 * div.selectize-input.items.not-full'); \
#     var input = document.querySelector('div.col-xs-12 * div.selectize-input.items.not-full input');\
#     var div2 = document.createElement('div'); \
#     div2.innerHTML = '1100 - Согласование наименования КО при ее учреждении'; \
#     div1.insertBefore(div2, input); div2.setAttribute('class', 'item'); div2.setAttribute('data-value', '1100');\
#     div1.setAttribute('class', 'selectize-input items has-options full has-items');""")
# self.driver.execute_script("""var procCodeOpt = document.querySelector('select[name="registrationProcedureCode"] option');\
#     procCodeOpt.setAttribute('value', '1100');var structDeptOpt = document.querySelector('select[name="structuralDepartment"] option');\
#     structDeptOpt.setAttribute('value', '74');var orgOpt = document.querySelector('select[id="organizationNew"] option');\
#     orgOpt.setAttribute('value', 'ООО "Костромаселькомбанк"');""")