from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
import os, re, sys, time, json, requests, textwrap, socket
from email_validator import validate_email, EmailNotValidError
from googlesearch import search
from lxml.html import fromstring
from getpass import getpass
from shutil import which
import os
import pandas as pd 
from .models import CSVMaster
import csv

# Create your views here.

class UsernameList(APIView):

	def post(self, request):
		# username = str(input(f"{space}{w}{b}>{w} enter username:{b} ").lower())
		user_name = str(request.data["username"]).lower()
		print(user_name)
		urllist = [
			"https://facebook.com/{}",
			"https://instagram.com/{}",
			"https://twitter.com/{}",
			"https://youtube.com/{}",
			"https://vimeo.com/{}",
			"https://github.com/{}",
			"https://plus.google.com/{}",
			"https://pinterest.com/{}",
			"https://flickr.com/people/{}",
			"https://vk.com/{}",
			"https://about.me/{}",
			"https://disqus.com/{}",
			"https://bitbucket.org/{}",
			"https://flipboard.com/@{}",
			"https://medium.com/@{}",
			"https://hackerone.com/{}",
			"https://keybase.io/{}",
			"https://buzzfeed.com/{}",
			"https://slideshare.net/{}",
			"https://mixcloud.com/{}",
			"https://soundcloud.com/{}",
			"https://badoo.com/en/{}",
			"https://imgur.com/user/{}",
			"https://open.spotify.com/user/{}",
			"https://pastebin.com/u/{}",
			"https://wattpad.com/user/{}",
			"https://canva.com/{}",
			"https://codecademy.com/{}",
			"https://last.fm/user/{}",
			"https://blip.fm/{}",
			"https://dribbble.com/{}",
			"https://en.gravatar.com/{}",
			"https://foursquare.com/{}",
			"https://creativemarket.com/{}",
			"https://ello.co/{}",
			"https://cash.me/{}",
			"https://angel.co/{}",
			"https://500px.com/{}",
			"https://houzz.com/user/{}",
			"https://{}.blogspot.com/",
			"https://{}.tumblr.com/",
			"https://{}.wordpress.com/",
			"https://{}.devianart.com/",
			"https://{}.slack.com/",
			"https://{}.livejournal.com/",
			"https://steamcommunity.com/id/{}",
			"https://www.wikipedia.org/wiki/User:{}",
			"https://www.freelancer.com/u/{}",
			"https://www.dailymotion.com/{}",
			"https://www.etsy.com/shop/{}",
			"https://www.scribd.com/{}",
			"https://www.patreon.com/{}",
			"https://www.behance.net/{}",
			"https://www.goodreads.com/{}",
			"https://www.gumroad.com/{}",
			"https://www.instructables.com/member/{}",
			"https://www.codementor.io/{}",
			"https://www.reverbnation.com/{}",
			"https://www.designspiration.net/{}",
			"https://www.bandcamp.com/{}",
			"https://www.colourlovers.com/love/{}",
			"https://www.ifttt.com/p/{}",
			"https://www.trakt.tv/users/{}",
			"https://www.okcupid.com/profile/{}",
			"https://www.trip.skyscanner.com/user/{}",
			"http://www.zone-h.org/archive/notifier={}",
			]
		final_urllist = []
		for url in urllist:
			try:
				keys = ['response','url']
				values = []
				req = requests.get(url.format(user_name))
				values.append(req.status_code)
				final_urls=url.format(user_name)
				print(final_urls)
				values.append(final_urls)
				zip_iterator = zip(keys, values)
				dictionary = dict(zip_iterator)
				final_urllist.append(dictionary)
				values.clear()

			except requests.exceptions.Timeout: continue
			except requests.exceptions.TooManyRedirects: break
			except requests.exceptions.ConnectionError: break
		print(len(final_urllist))
		return Response({'success':True,'urllist':final_urllist})


class EmailList(APIView):

	def post(self, request):
		fullname = str(request.data["email"]).lower()
		data = [
			"gmail.com",
			"yahoo.com",
			"hotmail.com",
			"aol.com",
			"msn.com",
			"comcast.net",
			"live.com",
			"rediffmail.com",
			"ymail.com",
			"outlook.com",
			"cox.net",
			"googlemail.com",
			"rocketmail.com",
			"att.net",
			"facebook.com",
			"bellsouth.net",
			"charter.net",
			"sky.com",
			"earthlink.net",
			"optonline.net",
			"qq.com",
			"me.com",
			"gmx.net",
			"mail.com",
			"ntlworld.com",
			"frontiernet.net",
			"windstream.net",
			"mac.com",
			"centurytel.net",
			"aim.com",
			]
		listuser = [
			fullname.replace(" ",""),
			# fullname.replace(" ","")+"123",
			# fullname.replace(" ","")+"1234",
			]
		for name in fullname.split(" "):
			listuser.append(name)
			# listuser.append(name+"123")
			# listuser.append(name+"1234")
		f = open("result_mailfinder.txt","w")
		ok = []
		try:
			for user in listuser:
				for domain in data:
					email = user + "@" + domain
					api = "0c6ad1fd-f753-4628-8c0a-7968e722c6c7"
					response = requests.get(
						"https://isitarealemail.com/api/email/validate",
						params = {'email': email},
						headers = {'Authorization': "Bearer " + api })
					status = response.json()['status']
					if status == "valid":
						ok.append(email)
						f.write(email+"\n")
					else: pass
		except KeyboardInterrupt:
			print("\r"),;sys.stdout.flush()
			pass
		f.close()
		final_list = []
		for i in ok:
			if i not in final_list:
				final_list.append(i)
		return Response({'success':True,'emails':final_list})


def EmailCSV(request):
	context={}
	if request.POST:
		CSVMaster.objects.create(CsvName=request.FILES["file"])
		csv_file = request.FILES["file"]
		data=pd.read_csv(str(request.FILES["file"]),encoding="ISO-8859-1")
		count=1
		email_list = []
		for index,row in data.iterrows():
			Email=row[0]
			email_list.append(Email)
		print(len(email_list))
		ok = []
		try:
			for one_email in email_list:
				email = one_email
				api = "0c6ad1fd-f753-4628-8c0a-7968e722c6c7"
				response = requests.get(
					"https://isitarealemail.com/api/email/validate",
					params = {'email': email},
					headers = {'Authorization': "Bearer " + api })
				status = response.json()['status']
				if status == "valid":
					ok.append(email)
				else: pass
		except KeyboardInterrupt:
			print("\r"),;sys.stdout.flush()
			pass
		final_list = []
		for i in ok:
			if i not in final_list:
				final_list.append(i)
		print(len(final_list))
		context['final_list'] = final_list
		file = open('Email.csv', 'w', newline ='')
		with file:  
		    header = ['Email']
		    writer = csv.DictWriter(file, fieldnames = header)
		    writer.writeheader()
		    for x in final_list:
		    	writer.writerow({'Email' : x})
		return render(request,'table.html',context)
	return render(request,'index.html',context)






























