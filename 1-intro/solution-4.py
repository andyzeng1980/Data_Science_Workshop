from BanditGame import BanditGame
from scipy.stats import beta

def play_one_till_win(arm, bandit):
	money = bandit.money()
	spend = 0
	gain = 0
	while money > 0 and money < bandit.celling() and gain <= 0:
		_, gain, money = bandit.play(arm)
		if gain <= 0:
			spend -= gain
	return spend, gain

def play():
	bandit = BanditGame()
	total_money = bandit.money()
	money =  total_money
	arm_num = bandit.arm_num()
	prior = []
	win = []
	total = []
	for arm in range(0, arm_num):
		prior.append([1,1])
		win.append(0)
		total.append(0)
	
	while money > 0 and money < bandit.celling():
		def find_best_one(selected_arms):
			best_e = float('-inf')
			best_arm = None
			for arm in selected_arms:
				current_e = (prior[arm][0] - prior[arm][1])*1.0/total[arm]
				if current_e > best_e:
					best_e = current_e
					best_arm = arm
			return best_arm

		def sample_an_arm():
			max_sample = float('-inf')
			best_arm = None
			mature_ones = []
			for arm in range(0, arm_num):
				if win[arm] >= 10 and prior[arm][0] < prior[arm][1]:
					continue
				if win[arm] >= 10 and prior[arm][0] > prior[arm][1]:
					mature_ones.append(arm)
					continue
				r = beta.rvs(prior[arm][0], prior[arm][1])
				# print r
				if r > max_sample:
					max_sample = r
					best_arm = arm
			if len(mature_ones) > 0:
				return find_best_one(mature_ones)
			if best_arm is not None:
				return best_arm
			else:
				return find_best_one(range(bandit.arm_num()))
		arm_chosen = sample_an_arm()
		spend, gain = play_one_till_win(arm_chosen+1, bandit)
		money = bandit.money()
		prior[arm_chosen][1] += spend
		total[arm_chosen] += (spend+1)
		if gain > 0:
			prior[arm_chosen][0] += gain
			win[arm_chosen] += 1
		# print prior
		# print win
	if money > bandit.celling():
		return 1
	else:
		return 0

def main():
	win = 0
	for i in range(0, 1000):
		win += play()
	print win




if __name__ == '__main__':
	main()