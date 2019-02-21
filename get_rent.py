from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chinatest import convertCharacter2Dight as c2v

def get_rent(address):
    global address1
    rent_date=[]
    total_results = []
    dict ={'士林區':"15",'大同區':"09",'大安區':"02",'中山區':"10",'中正區':"03",'內湖區':"14",'文山區':"11",'北投區':"16",'松山區':"01",'信義區':"17",'南港區':"13",'萬華區':"05"}
    dict_of ={"１":"一段","２":"二段","３":"三段","４":"四段","５":"五段","６":"六段","７":"七段","８":"八段","９":"九段"}
    dict_int ={"1":"一段","2":"二段","3":"三段","4":"四段","5":"五段","6":"六段","7":"七段","8":"八段","9":"九段"}
 
    driver = webdriver.Chrome('C:/Users/LAB412/Desktop/論文題目/code/chromedriver')
    driver.get('https://cloud.land.gov.taipei/ImmPrice/LandPrice.aspx')
    try:
        driver.find_element_by_link_text("門牌查詢").click()
        time.sleep(1)
        driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_radiobtn_HistoryLandData').click()
        select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_MasterGond'))
        select.select_by_value(dict.get(address[3:6]))
        time.sleep(3)
    except:
        total_results = None

    
    try:
        if(address[7:8]=="街"): #X街
            select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
            select.select_by_visible_text(address[6:8])   # 把x[6:8]放入select
            time.sleep(1)
            driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[8:]))
            time.sleep(3)
            driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
            time.sleep(4)
            try:
                id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                table = id.find_elements_by_tag_name('table')[11]
                final_table = table.find_element_by_tag_name('table')
                rows = final_table.find_elements_by_tag_name('tr')
                for row in rows[1:2]:
                    # col0 = row.find_elements_by_tag_name('td')[0].text
                    col =row.find_elements_by_tag_name('td')[1].text
                    total_results.append(col)
            except:
                total_results = None 
        elif(address[8:9]=="街"): #XX街
            if(address[10:11]=="段"):
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                if dict_of.get(address[9:10]):
                    select.select_by_visible_text(address[6:9]+dict_of.get(address[9:10])) # 把x[6:11]放入select
                elif dict_int.get(address[9:10]):
                    select.select_by_visible_text(address[6:9]+dict_int.get(address[9:10]))
                else:
                    select.select_by_visible_text(address[6:11])
                time.sleep(1)
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[11:]))
                time.sleep(3)
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(20)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None 
            else:
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                select.select_by_visible_text(address[6:9]) # 把x[6:9]放入select
                time.sleep(1)
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[9:]))  
                time.sleep(3)     
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(15)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None
        elif(address[9:10]=="街"):#XXX街
            select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
            select.select_by_visible_text(address[6:10]) #把x[6:10]放入select
            time.sleep(1)
            driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[10:])) 
            time.sleep(3)      
            driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
            time.sleep(4)
            try:
                id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                table = id.find_elements_by_tag_name('table')[11]
                final_table = table.find_element_by_tag_name('table')
                rows = final_table.find_elements_by_tag_name('tr')
                for row in rows[1:2]:
                    # col0 = row.find_elements_by_tag_name('td')[0].text
                    col =row.find_elements_by_tag_name('td')[1].text
                    total_results.append(col)
            except:
                total_results = None
        elif(address[10:11]=="街"):
            select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
            select.select_by_visible_text(address[6:11]) #把x[6:10]放入select
            time.sleep(1)
            driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[11:])) 
            time.sleep(3)      
            driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
            time.sleep(4)
            try:
                id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                table = id.find_elements_by_tag_name('table')[11]
                final_table = table.find_element_by_tag_name('table')
                rows = final_table.find_elements_by_tag_name('tr')
                for row in rows[1:2]:
                    # col0 = row.find_elements_by_tag_name('td')[0].text
                    col =row.find_elements_by_tag_name('td')[1].text
                    total_results.append(col)
            except:
                total_results = None

        elif(address[8:9]=="路"):#XX路
            if(address[10:11]=="段"):
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                if dict_of.get(address[9:10]):
                    select.select_by_visible_text(address[6:9]+dict_of.get(address[9:10])) # 把x[6:11]放入select
                elif dict_int.get(address[9:10]):
                    select.select_by_visible_text(address[6:9]+dict_int.get(address[9:10]))
                else :
                    select.select_by_visible_text(address[6:11])
                time.sleep(1)           
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[11:]))                 
                time.sleep(3)       
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(10)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None
            else:
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                select.select_by_visible_text(address[6:9]) # 把x[6:9]放入select
                time.sleep(1)
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[9:]))   
                time.sleep(3)    
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(8)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None
        elif(address[9:10]=="路"):#XXX路
            if(address[11:12]=="段"):
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                if dict_of.get(address[10:11]):
                    select.select_by_visible_text(address[6:10]+dict_of.get(address[10:11]))
                elif dict_int.get(address[10:11]):
                    select.select_by_visible_text(address[6:10]+dict_int.get(address[10:11]))
                else:
                    select.select_by_visible_text(address[6:12])
                time.sleep(1)
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[12:]))       
                time.sleep(4)
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(50)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None
            else:
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                select.select_by_visible_text(address[6:10]) # 把x[6:9]放入select
                time.sleep(1)
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[10:]))  
                time.sleep(3)     
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(10)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None      
        elif(address[9:10]=="道"):
            if(address[11:12]=="段"):
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                if dict_of.get(address[10:11]):
                    select.select_by_visible_text(address[6:10]+dict_of.get(address[10:11]))
                elif dict_int.get(address[10:11]):
                    select.select_by_visible_text(address[6:10]+dict_int.get(address[10:11]))
                else:
                    select.select_by_visible_text(address[6:12])
                time.sleep(1)
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[12:]))       
                time.sleep(4)
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(10)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None
            else:
                select = Select(driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$ddl_doorNumber'))
                select.select_by_visible_text(address[6:10]) # 把x[6:9]放入select
                time.sleep(1)
                driver.find_element_by_name('ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DoorNumberSearch$txt_doorNumber').send_keys(c2v(address[10:]))  
                time.sleep(3)     
                driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberSearch_btn_Search').click()
                time.sleep(5)
                try:
                    id = driver.find_element_by_id('ContentPlaceHolder1_ContentPlaceHolder1_DoorNumberHistoryLandData_updatepanel')
                    table = id.find_elements_by_tag_name('table')[11]
                    final_table = table.find_element_by_tag_name('table')
                    rows = final_table.find_elements_by_tag_name('tr')
                    for row in rows[1:2]:
                        # col0 = row.find_elements_by_tag_name('td')[0].text
                        col =row.find_elements_by_tag_name('td')[1].text
                        total_results.append(col)
                except:
                    total_results = None
            
        address1 =total_results 
        driver.close()
        return address1
    except:
        return None


# print(get_rent("臺北市信義區信義路5段150巷310號"))