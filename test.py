import os, time

def fclearscr():
	os.system('cls')

def fquestion():
	question = raw_input('What is 10 * 10?:')
	if question == '100':
		fclearscr()
		print 'Well done'
	else:
		fclearscr()
		print 'Wrong'
	time.sleep(3)
	fclearscr()
	return question

def fquestion2():
	answer2 = ['blue', 'Blue']
	question2 = raw_input('What is the color of the sky?:')
	fclearscr()
	if question2 in answer2:
		print 'Well done'
		time.sleep(3)
		fclearscr()
		return question2
	else:
		fclearscr()
		print 'Wrong'
		time.sleep(3)
		fclearscr()
		fquestion2()

answer, question = 100, 4
while int(question) != int(answer):
	question = fquestion()
fquestion2()