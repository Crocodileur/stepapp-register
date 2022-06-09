from re import M
from onesec_api import Mailbox
import time
import string
import random
from selenium import webdriver
import argparse


parser = argparse.ArgumentParser(description='Usage : \nscript.py \"your-link\"')
parser.add_argument('link', type=str)
args = parser.parse_args()


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def split(word):
    return [char for char in word]

while True:

    web = webdriver.Chrome()
    web.get(args.link)  #ENTER YOUR REFERAL LINK RIGHT THERE

    time.sleep(6)

    rdm_mail_a = get_random_string(14)
    random_mail = (rdm_mail_a,'@dcctb.com')
    last = web.find_element_by_xpath('/html/body/div/div/div/input')
    last.send_keys(random_mail)

    time.sleep(2)

    boutton = web.find_element_by_xpath('/html/body/div/div/div/div[2]')
    boutton.click()

    time.sleep(11)

    mail_boxe = Mailbox(rdm_mail_a)
    get_id = mail_boxe.filtred_mail()

    if isinstance(get_id, list):
        mf = mail_boxe.mailjobs('read',get_id[0])
        recu = mf.json()['body']
        print(mf.json()['body']) # only body
        print('')
        code_fin = recu[24:32]
        print('LEN : ', len(code_fin))

    if (len(code_fin) == 7):

        code_coupe = split(code_fin)

        code1 = web.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/input')
        code1.send_keys(code_coupe[0])

        code2 = web.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/input')
        code2.send_keys(code_coupe[1])

        code3 = web.find_element_by_xpath('/html/body/div/div/div/div[2]/div[3]/input')
        code3.send_keys(code_coupe[2])

        code4 = web.find_element_by_xpath('/html/body/div/div/div/div[2]/div[4]/input')
        code4.send_keys(code_coupe[3])

        code5 = web.find_element_by_xpath('/html/body/div/div/div/div[2]/div[5]/input')
        code5.send_keys(code_coupe[4])

        code6 = web.find_element_by_xpath('/html/body/div/div/div/div[2]/div[6]/input')
        code6.send_keys(code_coupe[5])
        time.sleep(2)
        web.close
    else:
        web.close