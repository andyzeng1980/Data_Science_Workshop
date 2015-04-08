from BanditGame import BanditGame

def play():
	bandit = BanditGame()
	total_money = bandit.money()
	money =  total_money
	arm_num = bandit.arm_num()
	for arm in range(1, arm_num+1):
		while money >= 1.0*total_money*(arm_num-arm)/arm_num:
			_, gain, money = bandit.play(arm)
			if money <= 0:
				return 0
			if money >= bandit.celling():
				return 1
def main():
	win = 0
	for i in range(0, 1000):
		win += play()
	print "Times played: 1000; Times won: ", win,

if __name__ == '__main__':
	main()