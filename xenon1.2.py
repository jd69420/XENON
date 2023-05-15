import os
import sys
import logging
import argparse
import requests
import platform
import datetime
from art import *
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

import nltk
nltk.download('punkt')
nltk.download('stopwords')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
        logger.error(f"Error occurred while scraping URL: {url}\n{e}")
        return None

def scrape(urls, output_dir):
    for url in urls:
        logger.info(f"Scraping URL: {url}")
        text = scrape_text_from_url(url)
        if text is not None:
            output_file = f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            output_path = os.path.join(output_dir, output_file)
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(text)
            logger.info(f"Output saved to {output_path}")

            logger.info("Summarizing content")
            summary = summarize_text(text)
            summary_file = f"summary_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
            summary_path = os.path.join(output_dir, summary_file)
            with open(summary_path, "w", encoding="utf-8") as file:
                file.write(summary)
            logger.info(f"Summary saved to {summary_path}")
        logger.info("--------------------------------------")

def scrape_tor(url, output_dir):
    try:
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        text = response.text

        output_file = f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        output_path = os.path.join(output_dir, output_file)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
        logger.info(f"Output saved to {output_path}")

        logger.info("Summarizing content")
        summary = summarize
        text = response.text

        output_file = f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        output_path = os.path.join(output_dir, output_file)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
        logger.info(f"Output saved to {output_path}")

        logger.info("Summarizing content")
        summary = summarize_text(text)
        summary_file = f"summary_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        summary_path = os.path.join(output_dir, summary_file)
        with open(summary_path, "w", encoding="utf-8") as file:
            file.write(summary)
        logger.info(f"Summary saved to {summary_path}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred while scraping URL: {url}\n{e}")

def create_output_directory():
    output_dir = f"output_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def main():
    parser = argparse.ArgumentParser(description="Xenon Web Scraper")
    parser.add_argument("mode", type=str, choices=["clearnet", "darknet"], help="Mode for scraping: 'clearnet' or 'darknet'")
    parser.add_argument("url", type=str, help="URL to scrape")
    args = parser.parse_args()

    output_dir = create_output_directory()

    tprint("\n\n----- XENON -----", font="broadway")
    tprint("THE SCRAPER\nAND SUMMARIZATION FRAMEWORK", font="mini")
    logger.info("--------------------------------------")
    logger.info("MODE SELECTION")
    logger.info(f"\nMODE SET TO {args.mode.upper()}")

    if args.mode == "clearnet":
        logger.info("--------------------------------------")
        logger.info("BEGINNING PHASE 1")
        tprint("\nSCRAPING URL\n", font="mini")
        scrape([args.url], output_dir)
        logger.info("--------------------------------------")
        logger.info("\nSite scraped successfully")
        feedback = input("PLEASE PROVIDE FEEDBACK: ")

    elif args.mode == "darknet":
        logger.info("--------------------------------------")
        scrape_tor(args.url, output_dir)
        logger.info("Site scraped successfully")
        feedback = input("PLEASE PROVIDE YOUR FEEDBACK: ")
        if feedback:
            logger.info("Thank you for your feedback.")

if __name__ == "__main__":
    main()




