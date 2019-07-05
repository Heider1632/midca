from __future__ import print_function
import time as ctime 
import json
from indexed import IndexedOrderedDict
from collections import OrderedDict

class Goaltime:

	def __init__(self):
		self.data = {}
		self.id = 0
		self.data['goaltimes'] = []
		self.myMidca = None # pointer to MIDCA objects

	def StartIntend(self, goal, startime, endtime, state):

		if len(self.data['goaltimes']) == 0:

			self.data['goaltimes'].append({
				'id' : 0, 
				'name' : goal,
				'startime' : startime,
				'endtime' : endtime,
				'state' : state,
				'duration': 0,
			})

		else:	

			lastgoal = self.data['goaltimes'][-1]

			if(lastgoal['state'] == 'current'):

				#change state for pause
				lastgoal['state'] = 'paused'
				self.id = lastgoal['id']

			self.data['goaltimes'].extend([{
				'id' : self.data['goaltimes'][-1]['id'] + 1, 
				'name' : goal,
				'startime' : startime,
				'endtime' : endtime,
				'state' : state,
				'duration': 0,
			}])

			for x in range(0, len(self.data['goaltimes'])):
				if self.data['goaltimes'][x]['name'] == goal:
					print(self.data['goaltimes'][x])

		with open('data.json', 'w') as file:
			json.dump(self.data, file, indent=4)
			

	def StartEval(self, goal, startime, endtime, state):

		id = self.data['goaltimes'][-1]['id']

		for goaltime in self.data['goaltimes']:
			if goaltime['id'] == id or goaltime['name'] == goal:
				goaltime["endtime"] = endtime
				goaltime["state"] = state
				goaltime["duration"] = endtime - goaltime['startime']


		with open('data.json', 'w') as f:
			json.dump(self.data, f, indent=4)

	def getGoalTimes(self):
		with open('data.json') as file:
			data = json.load(file)

			for goaltime in data['goaltimes']:
				print('Goal id:', goaltime['id'])
				print('Goal name:', goaltime['name'])
				print('Goal startime', goaltime['startime'])
				print('Goaltime endtime', goaltime['endtime'])
				print('Goaltime duration', goaltime['duration'])
				print('Goaltime state', goaltime['state'])
				print('')