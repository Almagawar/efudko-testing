from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException as UA
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        login = self.driver.find_element_by_name('ns_7_CGAH47L00GNRC0I4B42HGB20E4__login')
        login.click()
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
        login = self.driver.find_element_by_xpath("//input[@name='save']")
        login.click()

    def close(self):
        self.driver.close()

    # def elem_id(self):
    #     elem = self.driver.find_element_by_class_name('navigationPanel')
    #     return elem.get_attribute('id')

    # def del_tab(self):
    #     del_tab = self.driver.find_element_by_link_text('На рассмотрении')
    #     del_tab.click() 

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
        # proc_type = self.driver.find_element_by_xpath("//input[@tabIndex='-32768' and\
            #  @placeholder='Для вывода списка введите не менее 2х символов']")
        # proc_type.send_keys('11')
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
        # proc_type.clear()
        org_name = self.driver.find_element_by_xpath("//input[starts-with(name(@*), 'jQuery')='141']")
        org_name.send_keys('11')
        org_name.sendKeys(Keys.DOWN)
        org_name.sendKeys(Keys.RETURN)
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(
            (By.LINK_TEXT,"×")))
        responsible = self.driver.find_element_by_xpath("//input[@tabIndex='-32768' and\
             @style='WIDTH: 8px']")
        responsible.send_keys('74 Департамент допуска и прекращения деятельности финансовых организаций')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.LINK_TEXT,"×")))



if __name__ == '__main__':
    efudko = Efudko()
    efudko.login()
    efudko.close()