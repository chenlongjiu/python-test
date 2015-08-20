'''
	directly type "python database.py" under file's dir in terminal
'''
import copy

class database:
	def __init__(self):
		self.cur = {}

	def excute(self, commands):
		if len(commands) < 1:
			return
		
		command = commands[0] #command represent the method of query
		
		if (command == "SET" or command == "set") and len(commands) >= 3:
			key = commands[1]
			value = commands[2]
			self.cur[key] = value

		elif (command == "GET" or command == "get") and len(commands) >= 2:
			key = commands[1]
			if key in self.cur:
				print self.cur[key]
			else:
				print "NULL"

		elif (command == "UNSET"  or command == "unset") and len(commands) >= 2:
			key = commands[1]
			if key in self.cur:
				del self.cur[key]

		elif (command == "NUMEQUALTO"  or command == "numequalto") and len(commands) >= 2:
			key = commands[1]
			count = 0
			for key in self.cur:
				if self.cur[key] == commands[1]:
					count += 1
			print count

		elif command == "ROLLBACK" or command == "rollback" or command == "COMMIT" or command == "commit":
			print "NO TRANSACTION"

		elif command == "END" or command =="end":
			return "END"

		elif command == "BEGIN" or command == "begin":
			rel =  transaction(self.cur).start() 
			if rel == "END":
				return "END"
			elif rel is not None:
				self.cur = rel
		else:
			print "cannot realize your query or query in a wrong format"
		
		return 

class transaction(database):
	#now it has the excution method

	def __init__(self, dic):
		#dic is the orginial db and cannot be changed unless commit
		self.cur = copy.deepcopy(dic)

	def start(self):
		
		while True:
			query = raw_input('>')
			commands = query.split(' ')
			if len(commands) < 1:
				pass
			else:
				command = commands[0]
				if command == "END" or command =="end":
					return "END"
				elif command == "COMMIT" or command == "commit":
					return self.cur

				elif command == "ROLLBACK" or command == "rollback":
					return None

				elif command == "BEGIN" or command == "begin":
					rel = transaction(self.cur).start()
					if rel == "END" :
						return "END"
					elif rel is not None: #this is for transaction commitment
						return rel
				else:
					self.excute(commands)


#start 
sol =  database()
while True:
		query = raw_input('>')
		commands = query.split(' ')
		if sol.excute(commands) == "END":
			break