from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
}

#flipkart electronics page url
url = 'https://www.flipkart.com/audio-video/pr?sid=0pm&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_2bc8d29b-5adc-49c5-bfea-5da7f0b0d383_1_372UD5BXDFYS_MC.9JGNW7M0TUHD&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Electronics~Audio~All_9JGNW7M0TUHD&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=9JGNW7M0TUHD'

#requesting
response = requests.get(url, headers=headers)
html_content = response.text

#using BeautifuSoup for scraping 
soup = BeautifulSoup(html_content, 'lxml')

#out products lies in this class div
product_divs = soup.find_all('div', class_='cPHDOP col-12-12')

#prints len of all produsts
print(f'len of all is :',len(product_divs))
file_path = 'posts/file2.csv'
with open(file_path,'w',encoding='utf-8') as file:
    writer = csv.writer(file)
    
    #Headers of products info
    writer.writerow(['Product_name','Price','Rating','Seller_Name'])
    
    #for each product we are scaping the info
    for product_div in product_divs:
        #product_name
        product_name_tag = product_div.find('a', class_='wjcEIp')
        product_name = product_name_tag.text.strip() if product_name_tag else "Out of stock"
        #company or sponser name
        company_or_sponsor_tag = product_div.find('div', class_='xgS27m')
        company_or_sponsor = company_or_sponsor_tag.span.text.strip() if company_or_sponsor_tag else "None"
        #price
        price_tag = product_div.find('div', class_='Nx9bqj')
        price = price_tag.text.strip() if price_tag else "Out of stock"
        #rating
        rating_tag = product_div.find('div', class_='XQDdHH')
        rating = rating_tag.text if rating_tag else "None"
        
        #inserting each row of the product info into our csv file
        writer.writerow([product_name,price,rating,company_or_sponsor])
print("Data is been added to csv file")