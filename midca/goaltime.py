from __future__ import print_function
import time as ctime 
import json
from indexed import IndexedOrderedDict
from collections import OrderedDict

class Goaltime:

	def __init__(self):
		self.time = ctime.strftime("%c")
		self.data = {}
		self.id = 0
		self.data[str(self.time)] = {}
		self.data[str(self.time)]['goaltime'] = []
		self.myMidca = None # pointer to MIDCA objects


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

				#change state for pause
				lastgoal['state'] = 'paused'
				self.id = lastgoal['id']

			self.data[str(self.time)]['goaltime'].extend([{
				'id' : self.data[str(self.time)]['goaltime'][-1]['id'] + 1, 
				'name' : goal,
				'startime' : startime, 
				'endtime' : endtime,
				'state' : state,
				'pausetime': 0,
				'duration': 0,
			}])

			for x in range(0, len(self.data[str(self.time)]['goaltime'])):
				if self.data[str(self.time)]['goaltime'][x]['name'] == goal:
					print(self.data[str(self.time)]['goaltime'][x])

		with open('data.json', 'w') as file:
			data = json.load(file)

			if(len(data) > 0)
				data.append(self.data)
				json.dump(data, file, indent=4)
			else:
				json.dump(self.data, file, indent=4)
			

	def StartEval(self, goal, startime, endtime, state):

		id = self.data[str(self.time)]['goaltime'][-1]['id']

		for x in range(0, len(self.data[str(self.time)]['goaltime'])):
			if self.data[str(self.time)]['goaltime'][x]['id'] == id or self.data[str(self.time)]['goaltime'][x]['name'] == goal:
				if(self.data[str(self.time)]['goaltime'][x -1 ]['state'] == 'paused'):
					goal_paused = self.data[str(self.time)]['goaltime'][x - 1]
					goal_paused['pausetime'] = self.data[str(self.time)]['goaltime'][x]['startime']
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