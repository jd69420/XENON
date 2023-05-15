import os
import sys
import nltk
import socks
import socket
import requests
import platform
import datetime
from art import *
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_sentences = [sentence for sentence in sentences if sentence.lower() not in stop_words]
    return filtered_sentences

def summarize_text(text, num_sentences=3):
    filtered_sentences = preprocess_text(text)
    summary = " ".join(filtered_sentences[:num_sentences])
    return summary

def scrape_text_from_url(url):
    #response = requests.get(url)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while scraping URL: {url}\n{e}")
        return None
    

def scrape(urls):
    for url in urls:
        text = scrape_text_from_url(url)
        print("\nURL:", url)
        print("-----------")
        output_file = f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        path = os.getcwd()
        path += '.txt'
        output_path = os.path.join(path, output_file)
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Output saved to {output_path}")
        print("------------------------------------------------------------------------")
        file.close()
        print("BEGINNING PHASE 2")
        tprint("\nSUMMARIZING CONTENT\n",font="mini")
        summary = summarize_text(text)
        summary_file = f"summary_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        path1 = os.getcwd()
        path1 += '.txt'
        summary_path = os.path.join(path1, summary_file)
        with open(summary_file, "w", encoding="utf-8") as file1:
            file1.write(summary)
        print(f"summary saved to {summary_path}")
        file1.close()
        
def scrape_tor(url):
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket
    #response = requests.get(url)
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print("Connection Error:", e)
    path = os.getcwd()
    output_file = f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    path = os.getcwd()
    path += '.txt'
    output_path = os.path.join(path, output_file)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)
    print(f"Output saved to {output_path}")    
    print("------------------------------------------------------------------------")
    file.close()
    print("BEGINNING PHASE 2")
    tprint("\nSUMMARIZING CONTENT\n")    
    
    summary = summarize_text(text)
    summary_file = f"summary_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    path1 = os.getcwd()
    path1 += '.txt'
    summary_path = os.path.join(path1, summary_file)
    with open(summary_file, "w", encoding="utf-8") as file1:
        file1.write(summary)
    file1.close()    
    print(f"summary saved to {summary_path}")


print("-----------------------------------------------------------------------")
tprint("\n\n----- XENON-----",font="broadway")
tprint("THE SCRAPER \nAND SUMMARIZATION FRAMEWORK",font="mini")
print("------------------------------------------------------------------------")
print("\nMODE-SELECTION")
mode = int(input("\nPress [0] for [[clearnet]] and [1] for [[darknet]] -> "))
if mode == 0:
    print("\nMODE SET TO { CLEARNET }\n")
    print("------------------------------------------------------------------------")
    url = input("\nPaste the URL: ")
    print("------------------------------------------------------------------------")
    print("BEGINNING PHASE 1")
    tprint(f"\nSCRAPING URL\n",font="mini")
    scrape([url])
    print("------------------------------------------------------------------------")
    print("\nSite scraped successfully")
    q = input("PLEASE PROVIDE FEEDBACK: ")

elif mode == 1:
    print("\nMODE SET TO { DARKNET }\n")
    url = input("\nPaste the '.onion' URL: ")
    scrape_tor(url)
    print("Site scraped successfully")
    q = input("PLEASE PROVIDE YOUR FEEDBACK: ")
    if q:
        print("Thank You for your feedback..")

