import requests
import time
# import only system from os 
from os import system, name  
# import sleep to show output for some time period 
from time import sleep 
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

repeat = 1
while(repeat > 0):
    clear()   
    print(" ")
    print("-----------------------------------------------------------------")
    print("              Created by Muhamad Ferdiansyah - 2020              ")
    print("-----------------------------------------------------------------")
    print("    Analisis Pertumbuhan Kasus Covid-19 by Jalan Gedong Coding   ")
    print("-----------------------------------------------------------------")
    print("                            Version 2                            ")
    print("-----------------------------------------------------------------")
    print(" ")

    print("Pilih Menu ")
    print("1. Lihat Data dari Indonesia")
    print("2. Lihat Data dari Dunia")
    print("3. Lihat Data Berdasarkan Provinsi")
    print("4. Jumlah Total di Dunia")
    print("0. Exit")

    pilih = input("Saya ingin memilih nomor : ")

    if (pilih == '1') :
        ulang = 1
        while(ulang > 0) :
            clear() 
            print(" ")
            print("----------------")
            print("Waiting Dlu Gays")
            print("----------------")
            print(" ")
            res = requests.get('https://api.kawalcorona.com/indonesia')
            data = res.json() 
            ticks = time.asctime( time.localtime(time.time()) )      
            print(" ")
            clear() 
            print("-------------------------------------")
            print("     Info Update Corona Covid-19     ")
            print("-------------------------------------")
            print("Waktu saat ini   :", ticks)
            print(" ")   
            print("Negara           : ", data[0]['name'])
            print("Jumlah Positif   : ", data[0]['positif'])
            print("Jumlah Sembuh    : ", data[0]['sembuh'])
            print("Jumlah Meninggal : ", data[0]['meninggal']) 
            print(" ")
            tanya = input("Ulang Perhitungan atau tidak (y/n) : ")
            if (tanya == 'n'):
                break

    if (pilih == '2') :
        ulang = 1
        while (ulang > 0) :
            clear() 
            print(" ")
            print("----------------")
            print("Waiting Dlu Gays")
            print("----------------")
            print(" ")
            res = requests.get('https://api.kawalcorona.com/')
            data = res.json() 
            ticks = time.asctime( time.localtime(time.time()) ) 
            print(" ")
            clear() 
            print("-------------------------------------")
            print("     Info Update Corona Covid-19     ")
            print("-------------------------------------")
            print("Waktu saat ini   :", ticks)
            print(" ")    
            for isi in data :
                print("Negara : ", isi['attributes']['Country_Region'])
                print("     Positif   : ", isi['attributes']['Confirmed'])
                print("     Sembuh    : ", isi['attributes']['Recovered'])
                print("     Meninggal : ", isi['attributes']['Deaths'])
                print(" ")
            tanya = input("Ulang Perhitungan atau tidak (y/n) : ")
            if (tanya == 'n'):
                break

    if (pilih == '3') :
        ulang = 1
        while (ulang > 0) :
            clear() 
            print(" ")
            print("----------------")
            print("Waiting Dlu Gays")
            print("----------------")
            print(" ")
            res = requests.get('https://api.kawalcorona.com/indonesia/provinsi')
            data = res.json() 
            ticks = time.asctime( time.localtime(time.time()) ) 
            print(" ")
            clear() 
            print("-------------------------------------")
            print("     Info Update Corona Covid-19     ")
            print("-------------------------------------")
            print("Waktu saat ini   :", ticks)
            print(" ")    
            for isi in data :
                print("Provinsi : ", isi['attributes']['Provinsi'])
                print("     Positif   : ", isi['attributes']['Kasus_Posi'])
                print("     Sembuh    : ", isi['attributes']['Kasus_Semb'])
                print("     Meninggal : ", isi['attributes']['Kasus_Meni'])
                print(" ")
            tanya = input("Ulang Perhitungan atau tidak (y/n) : ")
            if (tanya == 'n'):
                break

    if (pilih == '4') :
        ulang = 1
        while (ulang > 0) :
            clear() 
            print(" ")
            print("----------------")
            print("Waiting Dlu Gays")
            print("----------------")
            print(" ")
            resPositif = requests.get('https://api.kawalcorona.com/positif')
            dataPositif = resPositif.json() 
            resSembuh = requests.get('https://api.kawalcorona.com/sembuh')
            dataSembuh = resSembuh.json() 
            resMeninggal = requests.get('https://api.kawalcorona.com/meninggal')
            dataMeninggal = resMeninggal.json() 
            ticks = time.asctime( time.localtime(time.time()) ) 
            print(" ")
            clear() 
            print("-------------------------------------")
            print("     Info Update Corona Covid-19     ")
            print("-------------------------------------")
            print("Waktu saat ini   :", ticks)
            print(" ")
            print("Total Dunia Positif   : ", dataPositif['value'])
            print("Total Dunia Sembuh    : ", dataSembuh['value'])  
            print("Total Dunia Meninggal : ", dataMeninggal['value'])
            print(" ")
            tanya = input("Ulang Perhitungan atau tidak (y/n) : ")
            if (tanya == 'n'):
                break

    if(pilih == "0"):
        break


clear()  
print(" ")
print("Terima kasih sudah menggunakan aplikasi ini :)")
