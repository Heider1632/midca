from __future__ import print_function
import time as ctime 
import json
import shlex, subprocess 
import os
from collections import OrderedDict

class Goaltime:

	def __init__(self):
		self.time = ctime.strftime("%c")
		self.data = {}
		self.id = 0
		self.data[str(self.time)] = {}
		self.data[str(self.time)]['goaltime'] = []
		self.myMidca = None

	def StartIntend(self, goal, startime, endtime, state):

		if len(self.data[str(self.time)]['goaltime']) == 0:

			self.data[str(self.time)]['goaltime'].append({
				'id' : 0, 
				'name' : goal,
				'startime' : startime,
				'endtime' : endtime,
				'state' : state,
				'duration': 0,
			})

		else:	

			lastgoal = self.data[str(self.time)]['goaltime'][-1]

			if(lastgoal['state'] == 'current'):
				lastgoal['state'] = 'paused'
				self.id = lastgoal['id']

			self.data[str(self.time)]['goaltime'].extend([{
				'id' : self.data[str(self.time)]['goaltime'][-1]['id'] + 1, 
				'name' : goal,
				'startime' : startime, 
				'endtime' : endtime,
				'state' : state,
				'duration': 0,
			}])

		depured_goaltime = list()
		for x in range(0, len(self.data[str(self.time)]['goaltime'])):
			if  x > 1 and self.data[str(self.time)]['goaltime'][x]['name'] == goal:
				depured_goaltime.extend([self.data[str(self.time)]['goaltime'][x]])
				if(len(depured_goaltime) >= 2):
					indice = depured_goaltime[-1]['id']
					self.data[str(self.time)]['goaltime'].pop(indice)


		with open('data.json', 'w') as file:
			json.dump(self.data, file, indent=4)
			

	def StartEval(self, goal, startime, endtime, state):

		id = self.data[str(self.time)]['goaltime'][-1]['id']

		for x in range(0, len(self.data[str(self.time)]['goaltime'])):
			if self.data[str(self.time)]['goaltime'][x]['id'] == id or self.data[str(self.time)]['goaltime'][x]['name'] == goal:
				self.data[str(self.time)]['goaltime'][x]['endtime'] = endtime
				self.data[str(self.time)]['goaltime'][x]['state'] = state
				self.data[str(self.time)]['goaltime'][x]['duration'] = endtime - self.data[str(self.time)]['goaltime'][x]['startime']


		with open('data.json', 'w') as f:
			json.dump(self.data, f, indent=4)

	def getGoalTimes(self):
		with open('data.json') as file:
			data = json.load(file)

			for goaltime in data['goaltime']:
				print('Goal id:', goaltime['id'])
				print('Goal name:', goaltime['name'])
				print('Goal startime', goaltime['startime'])
				print('Goaltime endtime', goaltime['endtime'])
				print('Goaltime duration', goaltime['duration'])
				print('Goaltime state', goaltime['state'])
				print('')

	def writeGoaltimePdf(self, filename="goaltime.txt"):

		file = open(filename, "w")

		for x in self.data[str(self.time)]['goaltime']:
			file.write(str(x))

		file.close()

