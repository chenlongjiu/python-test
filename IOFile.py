#! /usr/bin/python

print ("writting element to files")
f = open('text.txt', 'w')
f.write("hello")
f.write("\nworld")
f.close()
for line in open('text.txt'):
	print(line)
