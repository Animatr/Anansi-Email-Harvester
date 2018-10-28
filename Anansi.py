#!/usr/bin/env python
# -*- coding: utf-8 -*-

print"""
######################################################
              Anansi Email Toplayıcı v 1.0                          
######################################################
    Animatr
    BadShop.us
    mradmin@badshop.us
    Not: Aç kalırsanız zenginleri yiyiniz..
######################################################
"""

def Crawler():
    import urllib2, re
    try:
        website = raw_input("Web Sitesi:")
    
        request = urllib2.Request(website)
        response = urllib2.urlopen(request) 
        payload = response.read()
        results = re.findall(r'[\w\.-]+@[\w\.-]+', payload) 
        if len(results) == 0:
                print("Hiç email bulunamadı.") 
        else:
                for result in results:
                        print(result)
    except ValueError:
        print("Geçerli bir web adresi giriniz. Örn: http://www.domain.com/example.php")
        Crawler()
    except urllib2.URLError:
        print("Web sitesine erişilemiyor..")
        Crawler()
def Giris():
    print("\n\nTek Sayfa E-Mail Tarama (1) \nÇıkış (0)  ")    
    print("\n\nyapmak istediğiniz işlemi seçiniz..")
    input = int(raw_input("Seçiniz:"))
    if int(input) == 1:
        Crawler()
    elif int(input) == 0:
        exit
    else : 
        print("Hatalı giriş yaptınız tekrar deneyiniz..")
        Giris()

 
Giris()
