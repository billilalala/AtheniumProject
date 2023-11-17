
#automation skipping one step

from selenium import webdriver
from selenium.webdriver.safari.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.select import Select





#----input names 
#reading the CSV of doctors downloaded from scopus

# pd.read_csv('scopus_2.csv')
# author1 = pd.read_csv('scopus_2.csv', dtype = {'Year': str})
# author4 = pd.read_csv('scopus4.csv', dtype = {'Year': str})
# pd.read_csv('scopus_3.csv')
# author5 = pd.read_csv('scopus_3.csv', dtype = {'Year': str})
# pd.read_csv('scopus_1.csv')
# author7 = pd.read_csv('scopus_1.csv', dtype = {'Year': str})


# #my personal advice would be to check individually how each doctor is site in order to change the following script

# Author_1 = 'BANERJEE Sudipto'
# author1.insert(0, 'Author', Author_1)
# author1['Authors'] = author1['Authors'].str.replace('Banerjee ' , '')
# author1['Authors'] = author1['Authors'].str.replace('S.,', '').str.strip(',')
# author1['Authors'] = author1['Authors'].str.replace('Sudipto', '')
# author1['Authors'] = author1['Authors'].str.replace(' S.', '').str.strip(',')

# #-----------------------------


# Author_4 = 'DREFAHL SVEN'
# author4.insert(0, 'Author', Author_4)
# author4['Authors'] = author4['Authors'].str.replace('Drefahl ' , '')
# author4['Authors'] = author4['Authors'].str.replace('S.', '').str.strip(',')


# Author_5 = 'HERTELIU CLAUDIU'
# author5.insert(0, 'Author', Author_5)
# author5['Authors'] = author5['Authors'].str.replace('Herteliu ' , '')
# author5['Authors'] = author5['Authors'].str.replace('C.,', '').str.strip(',')
# author5['Authors'] = author5['Authors'].str.replace('Claudiu ' , '')
# author5['Authors'] = author5['Authors'].str.replace('Herțeliu', '')
# author5['Authors'] = author5['Authors'].str.replace('Herţeliu', '')

# #-----------------------------


# Author_7 = 'ZARULLI Virginia'
# author7.insert(0, 'Author', Author_7)
# author7['Authors'] = author7['Authors'].str.replace('Zarulli' , '').str.strip(',')
# author7['Authors'] = author7['Authors'].str.replace(' V.', '').str.strip(',')
# author7['Authors'] = author7['Authors'].str.replace('Zarullia ' , '')
# #-----------------------------------

# #In order to avoid random breaks another viable option would be not to bind all the authors together and compiling individually, in that 
# #case, it would also be needed to upload the starting range of the valori variable (line 100)

# frames = [author1, author4, author5, author7]
# data = pd.concat(frames, ignore_index = True)
# data = data.drop(["Author(s) ID", 'Source', 'EID', 'Page end', 'Page count', 'Page start', 'Publication Stage', 'Open Access',
#                'Cited by', 'Link', 'Art. No.', 'Issue', 'CODEN', 'ISBN', 'Volume'], axis='columns')
# data.loc[data['Year'] == '2007', 'Year' ] = ''
# data.loc[data['Year'] == '2006', 'Year' ] = ''
# data.loc[data['Year'] == '2005', 'Year' ] = ''
# data.loc[data['Year'] == '2004', 'Year' ] = ''
# data.loc[data['Year'] == '2003', 'Year' ] = ''
# data.loc[data['Year'] == '2002', 'Year' ] = ''
# data.loc[data['Year'] == '2001', 'Year' ] = ''
# data.loc[data['Year'] == '2000', 'Year' ] = ''
# data.loc[data['Document Type'] == 'Article', 'Document Type' ] = '262'
# data.loc[data['Document Type'] == 'Review', 'Document Type' ] = '263'
# data.loc[data['Document Type'] == 'Erratum', 'Document Type' ] = '298'
# data.loc[data['Document Type'] == 'Short Survey', 'Document Type' ] = '298'
# data.loc[data['Document Type'] == 'Retracted', 'Document Type' ] = '298'
# data.loc[data['Document Type']== 'Book Chapter', 'Document Type'] = '268'
# data.loc[data['Document Type'] == 'Letter', 'Document Type'] = '298'
# data.loc[data['Document Type'] == 'Conference Paper', 'Document Type'] = '274'
# data.loc[data['Document Type'] == 'Conference Review', 'Document Type'] ='273'
# data.loc[data['Document Type'] == 'Editorial', 'Document Type'] = '269'
# data.loc[data['Document Type'] == 'Book', 'Document Type'] = '292'
# data.loc[data['Document Type'] == 'Note', 'Document Type'] = '282'
# data.loc[data['Document Type']== 'Data Paper', 'Document Type'] = '295'
# data.loc[data['Document Type'] == 'Report', 'Document Type' ] = '298'
# data.loc[data['Document Type'] == 'Abstract Report', 'Document Type' ] = '298'
# data.loc[data['Document Type'] == 'Undefined', 'Document Type' ] = '298'

# #site-default includes filling NaN when the insertion key is not available
# data = data.fillna('nan')

# #those are the values needed in order to fill the cells, in case of random break of the function
# #(it could be doing that sometimes), upload the starting range of valori and valori_f will follow
# valori = list(range(0, 302, 1))
# valori_f = list(range(valori[0]+9, 301, 10))



#Web driver basics
options = webdriver.ChromeOptions()
options.add_argument('--window-size= 2000x2080')
options.add_argument('--verbose')
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"

#-----------login

driver = webdriver.Chrome()
driver.get("https://loginmiur.cineca.it/front.php/login.html")

username = driver.find_element(By.XPATH, '//*[@id="username"]')
#username to be inserted in the following line
username.send_keys('')
time.sleep(2)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
#password to be inserted in the following
password.send_keys('')
time.sleep(2)

procedi = driver.find_element(By.XPATH, '//*[@id="contenitore2"]/div[1]/div[1]/form/div/input[3]')
procedi.click()
time.sleep(3)

#-----------leading to the grid 

dottorati = driver.find_element(By.XPATH, '//*[@id="colonna-dx"]/ul/li[7]/a')
dottorati.click()
nota = driver.find_element(By.XPATH, '/html/body/div[2]/table[1]/tbody/tr[2]/td[1]/form/input[8]')
nota.click()
time.sleep(3)
driver.switch_to.frame('benvenuto')
accept_cookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
accept_cookies.click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame('bottoni')
time.sleep(3)
pencil = driver.find_element(By.XPATH, '/html/body/div/ul/li[2]/a')
pencil.click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame('benvenuto')
time.sleep(2)
recenter = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[15]/td[1]')
time.sleep(3)
arecenter = driver.execute_script('arguments[0].scrollIntoView(true)', recenter)
compile001 = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[18]/td[1]/form/input[12]')
compile001.click()
driver.maximize_window()
time.sleep(2)


#defining the function:
#it has to be taken into consideration that the following actions were needed according to a specific case
#so not all of the cells in the site are cited for the compilation.

def compile():
        j = 0
        for j in range(len(data)):
                for i in valori:
                        #Autore 
                        selections = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[2]/span/select'
                        autore = Select(driver.find_element(By.XPATH, selections))
                        autore.select_by_value(str(data['Author'][j]))
                        time.sleep(1)
                        #Altri autori 
                        expression = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[3]/span/textarea' 
                        others = driver.find_element(By.XPATH , expression)
                        others.clear()
                        others.send_keys(data['Authors'][j])
                        time.sleep(5)
                        #Anno 
                        selections2 = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[4]/span/select'
                        anno = Select(driver.find_element(By.XPATH, selections2))
                        anno.select_by_value(str(data['Year'][j]))
                        time.sleep(1)
                        #Tipologia 
                        selections3 = f'/html/body/form/div/table/tbody/tr[{i}]/td[5]/span/select'
                        select_tipologia = Select(driver.find_element(By.XPATH, selections3))
                        select_tipologia.select_by_value(str(data['Document Type'][j]))
                        #Titolo
                        expression2 = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[6]/span/textarea'
                        title = driver.find_element(By.XPATH , expression2)
                        title.clear()
                        title.send_keys(data['Title'][j])
                        time.sleep(5)
                        #Titolo della fonte
                        expression3 = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[7]/span/textarea'
                        stitle = driver.find_element(By.XPATH , expression3)
                        stitle.clear()
                        stitle.send_keys(data['Source title'][j])
                        time.sleep(2)
                        #ISSN            
                        expression4 = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[8]/span/input'
                        issn = driver.find_element(By.XPATH, expression4)
                        issn.clear()
                        issn.send_keys(data['ISSN'][j])
                        time.sleep(2)
                        #ISBN 
                        expression5 = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[9]/span/input'
                        isbn = driver.find_element(By.XPATH, expression5).clear()
                        #ISMN  
                        expression6 = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[10]/span/input'
                        ismn = driver.find_element(By.XPATH, expression6).clear()
                        #DOI
                        expression7 = f'/html/body/form/div[1]/table/tbody/tr[{i}]/td[11]/span/input'
                        doi = driver.find_element(By.XPATH, expression7)
                        doi.clear()
                        doi.send_keys(data['DOI'][j])
                        time.sleep(2)
                        i = i+1
                        j = j+1
                        valori.pop((-1))     
                        data.drop(data.index[-1], inplace= False)
                        if i == valori_f[0]:
                                valori_f.pop(0)
                                aggiorna = driver.find_element(By.XPATH, '/html/body/form/center/font/input[1]')
                                aggiorna.click()
                                time.sleep(10)
                                continue
                        if i == 301:
                                time.sleep(5)
                                data.to_csv('yet-to-be-compiled.csv', index=True)
                                aggiorna = driver.find_element(By.XPATH, '/html/body/form/center/font/input[1]')
                                aggiorna.click()
                                time.sleep(10)
                                print('There are others')
                                #in this case given that currently we do not have access 
                                #to the miur page the following steps should be adopted:
                                #creating a new data reading the 'yet-to-be-compiled.csv', automatically
                                #saved from current last step and renaming it data
                                #then proceed to compile again with the new data and given the following if 
                                #the function will automatically stop once all the text is compiled                                 
                        if j not in range(len(data)):
                                time.sleep(3)
                                aggiorna = driver.find_element(By.XPATH, '/html/body/form/center/font/input[1]')
                                aggiorna.click()
                                time.sleep(5)
                                driver.quit()
                                print('All done dear')

#196-207

compile()

