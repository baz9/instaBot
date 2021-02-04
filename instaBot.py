from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSessionIdException
import time
import random

#Need to update code here with path for geckodriver
class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox(executable_path = '')

#Logout process if the bot recieves a warning for excessive activity
	def testLogout(self):
		bot = self.bot
		try:
			bot.get('https://www.instagram.com/themaltlife/')
			time.sleep(2)
			bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div/button').click()
			time.sleep(2)
			bot.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[9]').click()
		except NoSuchElementException:
			pass
		except ElementClickInterceptedException:
			pass

#First login procedure
	def loginFirst(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(5)
		try:
			bot.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
		except NoSuchElementException:
			pass
		bot.find_element_by_name('username').send_keys(self.username)
		time.sleep(5)
		bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(self.password + Keys.RETURN)
		time.sleep(5)

#Additional login for list loop - the bot will log out after completing each hashtag or if it is flagged for excessive activity
	def loginSecond(self):
		bot = self.bot
		time.sleep(5)
		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(5)
		bot.find_element_by_name('username').send_keys(self.username)
		time.sleep(5)
		bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(self.password + Keys.RETURN)
		time.sleep(5)

#Hashtag searching function
	def searchHashtag(self, hashtag):
		bot = self.bot
		bot.get('https://www.instagram.com/explore/tags/' + hashtag)
		time.sleep(5)

#Liking photos function
	def likePhotos(self, amount):
		bot = self.bot
		bot.find_element_by_class_name('_9AhH0').click()
		time.sleep(randomWait)
		hasElement = True
		i = 0
		
		while i <= amount and hasElement == True:
			try:
				time.sleep(randomWait)
				bot.find_element_by_class_name('fr66n').click()
				i += 1
				time.sleep(randomWait)
				bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			except NoSuchElementException:
				hasElement = False
			except ElementClickInterceptedException:
				Keys.TAB
				Keys.TAB
				Keys.ENTER
				hasElement = False
				time.sleep(1200)
				
#Random integer between 6 and 10 to look less robotic				
randomWait = random.randint(6, 10)

#Replace with your username and password
insta = InstagramBot('username', 'password')

#replace tags with your criteria
hashtags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6']

insta.loginFirst()

for item in hashtags:
	randomWait
	insta.searchHashtag(item)
	insta.likePhotos(500)
	insta.testLogout()
	insta.loginSecond()