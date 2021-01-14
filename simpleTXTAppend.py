import os

# small hack to avoid dev time
# uses input.txt file
# generates emails
# output given as 'output.txt' file

# '@' is automatically added later
domain = 'gmail.com'

ip = open('input.txt', 'r')


lines = ip.readlines()

mails = list()

for line in lines:
	mails.append(line.strip('\n')+'@'+domain+'\n')

op = open('output.txt','w')
op.writelines(mails)
op.close()
