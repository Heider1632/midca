import time as ctime 
import json
from indexed import IndexedOrderedDict
from collections import OrderedDict

class Goaltime:

	def __init__(self):
		self.data = {}
		self.data['goaltimes'] = []

	def multiple_appends(listname, *element):
		listname.extend(element)

	def StartIntend(self, goal, startime, endtime, state):

		self.data['goaltimes'].extend([{
			'id' : goalid, 
			'name' : goal,
			'startime' : startime,
			'endtime' : endtime,
			'state' : state,
			'duration': 0,
		}])

		with open('data.json', 'w') as file:
			json.dump(self.data, file, indent=4)
			

	def StartEval(self, goal, startime, endtime, state):
		print(self.data)

		#for goaltime in self.data['goaltimes']:
		#	if(goaltime['id'] == goalid):
		#		goaltime["endtime"] = endtime
		#		goaltime["state"] = state
		#		goaltime["duration"] = goaltime['startime'] - endtime
		#	else:
		#		print "error no se encontro goalid asociado"

		#with open('data.json', 'w') as f:
		#	json.dump(self.data, f, indent=4)

	def getGoalTimes(self):
		with open('data.json') as file:
			data = json.load(file)

			for goaltime in data['goaltimes']:
				print('Goal id:', goaltime['id'])
				print('Goal name:', goaltime['name'])
				print('Goal startime', goaltime['startime'])
				print('Goaltime endtime', goaltime['endtime'])
				print('Goaltime state', goaltime['state'])
				print('')