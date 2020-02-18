#!/usr/bin/env python
# coding: utf-8


import config
import telebot
import logging
import requests
import shutil
import socket
import socks
import time
from telebot import types
from requests.packages.urllib3.exceptions import InsecureRequestWarning

logging.basicConfig(level = logging.DEBUG, filename = time.strftime("/var/log/bot-%Y-%m.log"))

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

telebot.apihelper.proxy = {'https':'socks5h://аывавваываываываываыва'}

bot = telebot.TeleBot(config.token)
	

def get_image_temperatura11pdu1():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-1h&height=500&orgId=2&panelId=2&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f11pdu1.png', 'wb') as f11pdu1:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f11pdu1)  
	return None


def get_image_dash():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d/t9-niW5mz/ctd-dash?from=now-1h&height=1100&orgId=4&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1920&timeout=600", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('dash.png', 'wb') as dash:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, dash)
	return None

def get_image_exchange():
	headers = {"Authorization": "Bearer fasdf=="}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d/kSn9kLSiz/grigorjevap_exchange?from=now-1h&height=1100&orgId=1&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1920&timeout=600", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('exchange.png', 'wb') as dash:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, dash)
	return None


def get_image_temperatura11pdu3():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-3h&height=500&orgId=2&panelId=2&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f11pdu3.png', 'wb') as f11pdu3:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f11pdu3)  
	return None

def get_image_temperatura11pdu6():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-6h&height=500&orgId=2&panelId=2&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f11pdu6.png', 'wb') as f11pdu6:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f11pdu6)  
	return None


def get_image_temperatura11pdu12():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-12h&height=500&orgId=2&panelId=2&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f11pdu12.png', 'wb') as f11pdu12:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f11pdu12)  
	return None

def get_image_temperatura11pdu24():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-24h&height=500&orgId=2&panelId=2&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f11pdu24.png', 'wb') as f11pdu24:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f11pdu24)  
	return None



def get_image_temperatura406pdu1():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-1h&height=500&orgId=2&panelId=3&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f406pdu1.png', 'wb') as f406pdu1:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f406pdu1)  
	return None



def get_image_temperatura406pdu3():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-3h&height=500&orgId=2&panelId=3&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f406pdu3.png', 'wb') as f406pdu3:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f406pdu3)  
	return None

def get_image_temperatura406pdu6():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-6h&height=500&orgId=2&panelId=3&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f406pdu6.png', 'wb') as f406pdu6:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f406pdu6)  
	return None


def get_image_temperatura406pdu12():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-12h&height=500&orgId=2&panelId=3&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f406pdu12.png', 'wb') as f406pdu12:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f406pdu12)  
	return None

def get_image_temperatura406pdu24():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-24h&height=500&orgId=2&panelId=3&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('f406pdu24.png', 'wb') as f406pdu24:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f406pdu24)  
	return None



def get_image_temperaturalac1():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-1h&height=500&orgId=2&panelId=5&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('flac1.png', 'wb') as flac1:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, flac1)  
	return None



def get_image_temperaturalac3():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-3h&height=500&orgId=2&panelId=5&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('flac3.png', 'wb') as flac3:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, flac3)  
	return None

def get_image_temperaturalac6():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-6h&height=500&orgId=2&panelId=5&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('flac6.png', 'wb') as flac6:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f4lac6)  
	return None


def get_image_temperaturalac12():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-12h&height=500&orgId=2&panelId=5&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('flac12.png', 'wb') as flac12:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, flac12)  
	return None

def get_image_temperaturalac24():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-24h&height=500&orgId=2&panelId=5&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('flac24.png', 'wb') as flac24:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, flac24)  
	return None

def get_image_temperaturalac7d():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-7d&height=500&orgId=2&panelId=5&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	if r.status_code == 200:
		with open('flac7d.png', 'wb') as flac7d:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, flac7d)  
	return None
















def get_image_temperatura11condey1():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=19&from=now-1h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f11condey11.png', 'wb') as f11condey11:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f11condey11)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=21&from=now-1h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f11condey21.png', 'wb') as f11condey21:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f11condey21)  
	return None

	
def get_image_temperatura11condey3():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=19&from=now-3h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f11condey13.png', 'wb') as f11condey13:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f11condey13)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=21&from=now-3h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f11condey23.png', 'wb') as f11condey23:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f11condey23)  
	return None


def get_image_temperatura11condey6():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=19&from=now-6h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f11condey16.png', 'wb') as f11condey16:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f11condey16)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=21&from=now-6h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f11condey26.png', 'wb') as f11condey26:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f11condey26)  
	return None

	
def get_image_temperatura11condey12():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=19&from=now-12h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f11condey112.png', 'wb') as f11condey112:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f11condey112)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=21&from=now-12h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f11condey212.png', 'wb') as f11condey212:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f11condey212)  
	return None

	
def get_image_temperatura11condey24():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=19&from=now-24h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f11condey124.png', 'wb') as f11condey124:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f11condey124)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=21&from=now-24h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f11condey224.png', 'wb') as f11condey224:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f11condey224)  
	return None

	
	


	
	
	
	
	
	
	
def get_image_temperatura406condey1():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=15&from=now-1h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f406condey11.png', 'wb') as f406condey11:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f406condey11)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=17&from=now-1h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f406condey21.png', 'wb') as f406condey21:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f406condey21)  
	return None

	
def get_image_temperatura406condey3():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=15&from=now-3h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f406condey13.png', 'wb') as f406condey13:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f406condey13)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=17&from=now-3h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f406condey23.png', 'wb') as f406condey23:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f406condey23)  
	return None


def get_image_temperatura406condey6():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=15&from=now-6h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f406condey16.png', 'wb') as f406condey16:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f406condey16)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=17&from=now-6h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f406condey26.png', 'wb') as f406condey26:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f406condey26)  
	return None

	
def get_image_temperatura406condey12():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=15&from=now-12h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f406condey112.png', 'wb') as f406condey112:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f406condey112)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=17&from=now-12h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f406condey212.png', 'wb') as f406condey212:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f406condey212)  
	return None

	
def get_image_temperatura406condey24():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=15&from=now-24h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r1.status_code == 200:
		with open('f406condey124.png', 'wb') as f406condey124:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, f406condey124)  
	r2 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/dEh43omiz/kondei?refresh=1m&orgId=2&panelId=17&from=now-24h&to=now&var-406k1=40.6K1&var-status406k1=undefined&width=1400&height=500&tz=UTC%2B03%3A00", headers=headers, stream=True,verify=False)
	if r2.status_code == 200:
		with open('f406condey224.png', 'wb') as f406condey224:
			r2.raw.decode_content = True
			shutil.copyfileobj(r2.raw, f406condey224)  
	return None

		
	
def get_image_PrintUPS406():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-1h&height=500&orgId=2&panelId=6&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	
	if r1.status_code == 200:
		with open('PrintUPS406.png', 'wb') as PrintUPS406:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, PrintUPS406)  
	return None


	
def get_image_PrintUPS11():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-1h&height=500&orgId=2&panelId=7&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	
	if r1.status_code == 200:
		with open('PrintUPS11.png', 'wb') as PrintUPS11:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, PrintUPS11)  
	return None

	
def get_image_PrintUPS406Input():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-1h&height=500&orgId=2&panelId=8&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	
	if r1.status_code == 200:
		with open('PrintUPS406Input.png', 'wb') as PrintUPS406Input:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, PrintUPS406Input)  
	return None

def get_image_PrintUPS11Input():
	headers = {"Authorization": "Bearer fsafasdfasdfasdfasfasdfasdfas"}
	r1 = requests.get("https://fsafasdfasdfasdfasfasdfasdfas/render/d-solo/0lm1iGiik/temperatura?from=now-1h&height=500&orgId=2&panelId=9&refresh=1m&to=now&tz=UTC%2B03%3A00&width=1400", headers=headers, stream=True,verify=False)
	
	if r1.status_code == 200:
		with open('PrintUPS11Input.png', 'wb') as PrintUPS11Input:
			r1.raw.decode_content = True
			shutil.copyfileobj(r1.raw, PrintUPS11Input)  
	return None
	
	
	

def log(command,message):
	title = "none"
	if message.chat.title:
		title = message.chat.title.encode('utf-8')
	username = "none"
	if message.from_user.username:
		username = str(message.from_user.username.encode('utf-8'))
	first_name = "none"
	if message.from_user.first_name:
		first_name = str(message.from_user.first_name.encode('utf-8'))
	last_name = "none"
	if message.from_user.last_name:
		last_name = str(message.from_user.last_name.encode('utf-8'))
	logging.info(command+';'+str(message.chat.type)+';'+title+';'+str(message.chat.id)+';'+str(message.from_user.id)+';'+username+';'+first_name+';'+last_name)






@bot.message_handler(commands=['start'])
def send_welcome(message):
	log('start',message)
	bot.send_message(message.chat.id, """\nПривет! Выбери действие:
Температура, возвращаемая первым и вторым кондиционерами в 1.1 за час, три часа и т.д.:
/Print11TempCondey1h
/Print11TempCondey3h
/Print11TempCondey6h
/Print11TempCondey12h
/Print11TempCondey24h
Температура, возвращаемая первым и вторым кондиционерами в 40.6 за час, три часа и т.д.:
/Print406TempCondey1h
/Print406TempCondey3h
/Print406TempCondey6h
/Print406TempCondey12h
/Print406TempCondey24h
График температуры с PDU в 1.1 за час, три часа и т.д.:
/Print11TempPDU1h
/Print11TempPDU3h
/Print11TempPDU6h
/Print11TempPDU12h
/Print11TempPDU24h
График температуры с PDU в 40.6 за час, три часа и т.д.:
/Print406TempPDU1h
/Print406TempPDU3h
/Print406TempPDU6h
/Print406TempPDU12h
/Print406TempPDU24h
График температуры с NetPing в LAC за час, три часа и т.д.:
/PrintLACTemp1h
/PrintLACTemp3h
/PrintLACTemp6h
/PrintLACTemp12h
/PrintLACTemp24h
/PrintLACTemp7d
40.6 Заряд батарей:
/PrintUPS406
1.1 Заряд батарей:
/PrintUPS11
40.6 Входное напряжение по фазам:
/PrintUPS406Input
1.1 Входное напряжение по фазам:
/PrintUPS11Input
Повторить данное меню:
/start  
Замечу, что обработка занимает не меньше 10 секунд.
Также, если данных от устройства нет (например оно ничего не возвращает по snmp) - график будет пустой.
\n""")


@bot.message_handler(commands=['Print11TempPDU1h'])
def send_Print11TempPDU1(message):
	log('Print11TempPDU1h',message)
	get_image_temperatura11pdu1() 
	f = open('f11pdu1.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")



@bot.message_handler(commands=['dash'])
def send_dash(message):
	log('dash',message)
	get_image_dash()
	f = open('dash.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['exchange'])
def send_exchange(message):
	log('exchange',message)
	get_image_exchange()
	f = open('exchange.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

	


@bot.message_handler(commands=['Print11TempPDU3h'])
def send_Print11TempPDU3(message):
	log('Print11TempPDU3h',message)
	get_image_temperatura11pdu3() 
	f = open('f11pdu3.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print11TempPDU6h'])
def send_Print11TempPDU6(message):
	log('Print11TempPDU6h',message)
	get_image_temperatura11pdu6() 
	f = open('f11pdu6.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print11TempPDU12h'])
def send_Print11TempPDU12(message):
	log('Print11TempPDU12h',message)
	get_image_temperatura11pdu12() 
	f = open('f11pdu12.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print11TempPDU24h'])
def send_Print11TempPDU24(message):
	log('Print11TempPDU24h',message)
	get_image_temperatura11pdu24() 
	f = open('f11pdu24.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print406TempPDU1h'])
def send_Print406TempPDU1(message):
	log('Print406TempPDU1h',message)
	get_image_temperatura406pdu1() 
	f = open('f406pdu1.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print406TempPDU3h'])
def send_Print406TempPDU3(message):
	log('Print406TempPDU3h',message)
	get_image_temperatura406pdu3() 
	f = open('f406pdu3.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print406TempPDU6h'])
def send_Print406TempPDU6(message):
	log('Print406TempPDU6h',message)
	get_image_temperatura406pdu6() 
	f = open('f406pdu6.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print406TempPDU12h'])
def send_Print406TempPDU12(message):
	log('Print406TempPDU12h',message)
	get_image_temperatura406pdu12() 
	f = open('f406pdu12.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['Print406TempPDU24h'])
def send_Print406TempPDU24(message):
	log('Print406TempPDU24h',message)
	get_image_temperatura406pdu24() 
	f = open('f406pdu24.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")




@bot.message_handler(commands=['PrintLACTemp1h'])
def send_PrintLACTemp1(message):
	log('PrintLACTemp1h',message)
	get_image_temperaturalac1() 
	f = open('flac1.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['PrintLACTemp3h'])
def send_PrintLACTemp3(message):
	log('PrintLACTemp3h',message)
	get_image_temperaturalac3() 
	f = open('flac3.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['PrintLACTemp6h'])
def send_PrintLACTemp6(message):
	log('PrintLACTemp6h',message)
	get_image_temperaturalac6() 
	f = open('flac6.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['PrintLACTemp12h'])
def send_PrintLACTemp12(message):
	log('PrintLACTemp12h',message)
	get_image_temperaturalac12() 
	f = open('flac12.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(commands=['PrintLACTemp24h'])
def send_PrintLACTemp24(message):
	log('PrintLACTemp24h',message)
	get_image_temperaturalac24() 
	f = open('flac24.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")


@bot.message_handler(commands=['PrintLACTemp7d'])
def send_PrintLACTemp7d(message):
	log('PrintLACTemp7d',message)
	get_image_temperaturalac7d() 
	f = open('flac7d.png', 'rb')
	bot.send_photo(message.chat.id, f)
	bot.send_photo(message.chat.id, "FILEID")

	
@bot.message_handler(commands=['Print11TempCondey1h'])
def send_Print11TempCondey1(message):
	log('Print11TempCondey1h',message)
	get_image_temperatura11condey1()
	f1 = open('f11condey11.png', 'rb')
	f2 = open('f11condey21.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)
  	
@bot.message_handler(commands=['Print11TempCondey3h'])
def send_Print11TempCondey3(message):
	log('Print11TempCondey3h',message)
	get_image_temperatura11condey3()
	f1 = open('f11condey13.png', 'rb')
	f2 = open('f11condey23.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

		
	
@bot.message_handler(commands=['Print11TempCondey6h'])
def send_Print11TempCondey6(message):
	log('Print11TempCondey6h',message)
	get_image_temperatura11condey6()
	f1 = open('f11condey16.png', 'rb')
	f2 = open('f11condey26.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

		
	
@bot.message_handler(commands=['Print11TempCondey12h'])
def send_Print11TempCondey12(message):
	log('Print11TempCondey12h',message)
	get_image_temperatura11condey12()
	f1 = open('f11condey112.png', 'rb')
	f2 = open('f11condey212.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

		
	
@bot.message_handler(commands=['Print11TempCondey24h'])
def send_Print11TempCondey24(message):
	log('Print11TempCondey24h',message)
	get_image_temperatura11condey24()
	f1 = open('f11condey124.png', 'rb')
	f2 = open('f11condey224.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

		
	
	
	
	
	
@bot.message_handler(commands=['Print406TempCondey1h'])
def send_Print406TempCondey1(message):
	log('Print406TempCondey1h',message)
	get_image_temperatura406condey1()
	f1 = open('f406condey11.png', 'rb')
	f2 = open('f406condey21.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

	
@bot.message_handler(commands=['Print406TempCondey3h'])
def send_Print406TempCondey3(message):
	log('Print406TempCondey3h',message)
	get_image_temperatura406condey3()
	f1 = open('f406condey13.png', 'rb')
	f2 = open('f406condey23.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

	
@bot.message_handler(commands=['Print406TempCondey6h'])
def send_Print406TempCondey6(message):
	log('Print406TempCondey6h',message)
	get_image_temperatura406condey6()
	f1 = open('f406condey16.png', 'rb')
	f2 = open('f406condey26.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

		
	
@bot.message_handler(commands=['Print406TempCondey12h'])
def send_Print406TempCondey12(message):
	log('Print406TempCondey12h',message)
	get_image_temperatura406condey12()
	f1 = open('f406condey112.png', 'rb')
	f2 = open('f406condey212.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

	
@bot.message_handler(commands=['Print406TempCondey24h'])
def send_Print406TempCondey24(message):
	log('Print406TempCondey24h',message)
	get_image_temperatura406condey24()
	f1 = open('f406condey124.png', 'rb')
	f2 = open('f406condey224.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	bot.send_photo(message.chat.id, f2)

		
@bot.message_handler(commands=['PrintUPS406'])
def send_PrintUPS406(message):
	log('PrintUPS406',message)
	get_image_PrintUPS406()
	f1 = open('PrintUPS406.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	
@bot.message_handler(commands=['PrintUPS11'])
def send_PrintUPS11(message):
	log('PrintUPS11',message)
	get_image_PrintUPS11()
	f1 = open('PrintUPS11.png', 'rb')
	bot.send_photo(message.chat.id, f1)

@bot.message_handler(commands=['PrintUPS406Input'])
def send_PrintUPS11(message):
	log('PrintUPS406Input',message)
	get_image_PrintUPS406Input()
	f1 = open('PrintUPS406Input.png', 'rb')
	bot.send_photo(message.chat.id, f1)
	
@bot.message_handler(commands=['PrintUPS11Input'])
def send_PrintUPS11(message):
	log('PrintUPS11Input',message)
	get_image_PrintUPS11Input()
	f1 = open('PrintUPS11Input.png', 'rb')
	bot.send_photo(message.chat.id, f1)

def send_callback_PrintUPS11(call):
	get_image_PrintUPS11Input()
	f1 = open('PrintUPS11Input.png', 'rb')
	bot.send_photo(call.message.chat.id, f1)


	
@bot.message_handler(commands=['123'])
def exchange_command(message):
	log('123',message)
	keyboard = telebot.types.InlineKeyboardMarkup()
	keyboard.list(
		telebot.types.InlineKeyboardButton('Узнать температуру', callback_data='pducondey'),
		telebot.types.InlineKeyboardButton('Данные по ИБП', callback_data='apc'),
		telebot.types.InlineKeyboardButton('Выполнить nslookup', callback_data='ns'),
		telebot.types.InlineKeyboardButton('Выполнить ping', callback_data='ping'),
		telebot.types.InlineKeyboardButton('Закрыть меню', callback_data='close')
	)
	keyboard.one_time_keyboard = True




@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	if call.data == "pducondey":
		bot.answer_callback_query(call.id)
		bot.send_chat_action(call.message.chat.id, 'typing')
		send_callback_PrintUPS11(call)
		keyboard = telebot.types.InlineKeyboardMarkup()
		keyboard.row(
			telebot.types.InlineKeyboardButton('fsdf а', callback_data='condey'),
			telebot.types.InlineKeyboardButton('Данfsdfsdf ные по ИБП', callback_data='apc')
		)
		bot.send_message(call.message.chat.id, 'fdjk;lsklf dsfsdf fd:', reply_markup = telebot.types.ReplyKeyboardRemove())

	
	
		


if __name__ == '__main__':

	logger = telebot.logger
	telebot.logger.setLevel(logging.DEBUG)
	bot.polling(none_stop=True, interval=3, timeout=20)
	
 
