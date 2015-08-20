
#directly type "python database.py" under file's dir in terminal

class database:
	def __init__(self):
		self.cur = {} # store (key, value) pair
		self.val = {} # store (value, counter) pair 

	def set(self, key , value):
		if (key in self.cur) and (self.cur[key] is not None):
			self.val[self.cur[key]] -= 1
			self.cur[key] = value
			if value in self.val:
				self.val[value] += 1
			else:
				self.val[value] = 1
		else:
			self.cur[key] = value
			if value in self.val:
				self.val[value] += 1
			else:
				self.val[value] = 1
		return

	def get(self, key):
		if key in self.cur:
			return self.cur[key]
		else:
			return "NULL"

	def unset(self, key):
		if key in self.cur:
			self.val[self.cur[key]] -= 1
			del self.cur[key]
		return

	def count(self, value):
		if value in self.val:
			return self.val[value]
		else:
			return 0

	def excute(self, commands):
		if len(commands) < 1:
			return
		
		command = commands[0] #command represent the method of query
		
		if (command == "SET" or command == "set") and len(commands) >= 3:
			key = commands[1]
			value = commands[2]
			self.set(key, value)

		elif (command == "GET" or command == "get") and len(commands) >= 2:
			key = commands[1]
			print self.get(key)

		elif (command == "UNSET"  or command == "unset") and len(commands) >= 2:
			key = commands[1]
			self.unset(key)

		elif (command == "NUMEQUALTO"  or command == "numequalto") and len(commands) >= 2:
			val = commands[1]
			print self.count(val)

		elif command == "ROLLBACK" or command == "rollback" or command == "COMMIT" or command == "commit":
			print "NO TRANSACTION"

		elif command == "END" or command =="end":
			return "END"

		elif command == "BEGIN" or command == "begin":
			rel =  transaction(self.cur, self.val).start() 
			if rel == "END":
				return "END"
			
		else:
			print "cannot realize your query or query in a wrong format"
		
		return 

'''@inherient from database class'''
class transaction(database):

	def __init__(self, dic, val):
		#dic & oldVal are the parent dictionary pointer and cannot be changed unless commit
		self.dic = dic
		self.cur = {}
		self.oldVal = val 
		self.val = {}	

	#@override function get, unset and count for each transection
	def get(self, key):
		if key in self.cur:
			if self.cur[key] is None:
				return "NULL"
			return self.cur[key]
		elif key in self.dic:
			return self.dic[key]
		else:
			return "NULL"

	def unset(self,key):
		if key in self.cur and self.cur[key] is not None:
			self.val[self.cur[key]] -= 1
		elif key in self.dic and self.dic[key] in self.val:
			self.val[self.dic[key]] -= 1
		elif key in self.dic and self.dic[key] not in self.val:
			self.val[self.dic[key]] = -1
 		self.cur[key] = None

 	def count(self,value):
 		if value in self.val and value in self.oldVal:
			return self.val[value] + self.oldVal[value]
		elif value in self.val:
			return self.val[value]
		elif value in self.oldVal:
			return self.oldVal[value]
		else:
			return 0

	def commit(self):
		#combine all the key value pair get changed
		for key in self.cur:
			if self.cur[key] is None:
				if key in self.dic:
					del self.dic[key]
			else:
				self.dic[key] = self.cur[key]
		#combine all the value counter pair get changed
		for num in self.val:
			if num in self.oldVal:
				self.oldVal[num] += self.val[num]
			else:
				self.oldVal[num] = self.val[num]
		return

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
					self.commit()
					return "COMMIT"

				elif command == "ROLLBACK" or command == "rollback":
					return None

				elif command == "BEGIN" or command == "begin":
					rel = transaction(self.cur, self.val).start()
					if rel == "END" :
						return "END"
					elif rel == "COMMIT": #this is for transaction commitment
						self.commit()
						return "COMMIT"
				else:
					self.excute(commands)


#start point
sol =  database()
while True:
		query = raw_input('>')
		commands = query.split(' ')
		if sol.excute(commands) == "END":
			break