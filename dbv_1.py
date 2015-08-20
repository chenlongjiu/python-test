#Creator: Longjiu Chen

#database is the main class for storing all the data 
class database:
	def __init__(self):
		self.cur = {} # store (key, value) pair
		self.val = {} # store (value, counter) pair 
		self.parent = None # indicate reach the root


	#------------------------------Functions----------------------------------#
	#setting the (key value) pair in db
	def set(self, key , value):
		index = self.get(key) #indecate the value of the old key
		if index != "NULL":
			#this value has been define before
			if index in self.val:
				#this is exist in cur db
				self.val[index] -= 1
			else:
				self.val[index] = -1
		if value in self.val:
			self.val[value] += 1
		else:
			self.val[value] = 1
		self.cur[key] = value
		
		return


	#getting value based on key
	def get(self, key):
		if key in self.cur:
			if self.cur[key] is None:
				return "NULL"
			return self.cur[key]
		else:
			return "NULL"


	#unset existing (key value) pair
	def unset(self, key):
		if key in self.cur:
			self.val[self.cur[key]] -= 1
			#clean the empty value in self.val
			if self.val[self.cur[key]] == 0:
				del self.val[self.cur[key]]
			del self.cur[key]
		return


	#count the numbers of one specific value in DB
	def count(self, value):
		if value in self.val:
			return self.val[value]
		else:
			return 0


	# all function start to work from excute()
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
			rel =  transaction(self).start() 
			if rel == "END":
				return "END"
			
		else:
			print "cannot recognize your request or query in a wrong format"
		
		return 


#@inherient from database class
#transaction class used for temporary data processing and recording

class transaction(database):

	def __init__(self, parent):
		#self.parent is the parent pointer and cannot be changed unless commit
		self.parent = parent
		self.cur = {}
		self.val = {}	

	#--------@override function get, unset and count for each transection---------#

	#Override get function adding traceback function to 
	#get the nearest transaction which contians the value 
	#of one specific key
	def get(self, key):
		if key in self.cur:
			if self.cur[key] is None:
				return "NULL"
			return self.cur[key]
		else:
			return self.parent.get(key)

	#Override unset function to deal with the existing (key, value) pair
	#existing in before transaction
	def unset(self,key):
		flag = self.get(key)
		if flag != "NULL":
			if flag in self.val:
				self.val[flag] -= 1
			else:
				self.val[flag] = -1
 		self.cur[key] = None
 		return

 	#Override count function for counting all the transaction values 
 	def count(self,value):
 		if value in self.val:
 			return self.val[value] + self.parent.count(value)
 		else:
 			return self.parent.count(value)

 	#commit function for combine all the changes happened in each trasaction by order
	def commit(self):
		#combine all the key value pair get changed
		for key in self.cur:
			self.parent.cur[key] = self.cur[key]
			if self.parent.parent is None and self.cur[key] is None:
				del self.parent.cur[key]
			
		#combine all the value counter pair get changed
		for num in self.val:
			if num in self.parent.val:
				self.parent.val[num] += self.val[num]
			else:
				self.parent.val[num] = self.val[num]

			#clean empty item	
			if self.parent.val[num] == 0:
				del self.parent.val[num]
		print self.parent.cur
		print self.parent.val
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
					#sub-transaction starts here
					rel = transaction(self).start()
					if rel == "END" :
						return "END"
					elif rel == "COMMIT": 
						self.commit()
						return "COMMIT"
				else:
					self.excute(commands)

#----------------------------------start----------------------------------#

sol =  database()
while True:
		query = raw_input('>')
		commands = query.split(' ')
		if sol.excute(commands) == "END":
			break