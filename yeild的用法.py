"""
可以用于子函数中变量的迭代式返回
（子函数返回变量后，下次调用时程序执行位置亟需返回变量的位置执行）
"""
def computer():
	print('first strp')
	step = 'press power button'
	yield step

	print('second step')
	step = 'wait for a few minutes'
	yield step

	print('finall strp')
	step = 'play computer games'
	yield step

if __name__ == '__main__':
	for index in computer():
		print(index)
		#input("enter")

"""
first step
press power button 
second step
wait for a few minutes
finally strp
play computer games

"""