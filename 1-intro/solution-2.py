from BanditGame import BanditGame

class PlayBandit(object):
	def __init__(self):
		self.__bandit = BanditGame()
		self.__celling = self.__bandit.celling()
		self.__arm_num = self.__bandit.arm_num()
		self.__stat = {}
		for arm in range(1, self.__arm_num+1):
			self.__stat[arm] = [0, 0, 0] # total, win, profit

	def play_chosen(self, arm):
		'''Play the chosen arm till win or lose'''
		money = self.__bandit.money()
		while money > 0 and money < self.__celling:
			_, gain, money = self.__bandit.play(arm)

	def find_best_and_play(self):
		best_e = self.__stat[1][2] / self.__stat[1][0]
		best_arm = 1
		for arm in range(1, self.__arm_num+1):
			current_e = self.__stat[arm][2] / self.__stat[arm][0]
			if current_e > best_e:
				best_e = current_e
				best_arm = arm
		self.play_chosen(best_arm)

	def has_positive_ones(self):
		for arm in range(1, self.__arm_num+1):
			if self.__stat[arm][1] >= 10 and (self.__stat[arm][2] / self.__stat[arm][0]) > 0:
				return True
		return False

	def find_insufficient_ones(self):
		insufficient_ones = []
		for arm in range(1, self.__arm_num+1):
			if self.__stat[arm][1] < 10:
				insufficient_ones.append(arm)
		return insufficient_ones


	def play_budget_on_insufficient_arms(self, insufficient_arms):
		money = self.__bandit.money()
		budgit_per_arm = money / len(insufficient_arms)
		for arm in insufficient_arms:
			start_money = money
			enough_stat = False
			while money > max((start_money - budgit_per_arm), 0) and money < self.__celling and not enough_stat:
				_, gain, money = self.__bandit.play(arm)
				self.__stat[arm][0] += 1
				self.__stat[arm][2] += gain
				if gain > 0:
					self.__stat[arm][1] += 1
				if self.__stat[arm][1] >= 10 and self.__stat[arm][2] < 0:
					enough_stat = True

	def play(self):
		money = self.__bandit.money()
		while money > 0 and money < self.__celling:
			if self.has_positive_ones():
				self.find_best_and_play()
			else:
				insufficient_arms = self.find_insufficient_ones()
				if len(insufficient_arms) > 0:
					self.play_budget_on_insufficient_arms(insufficient_arms)
				else:
					self.find_best_and_play()
			money = self.__bandit.money()
		# Check win or lose and return
		if money <= 0:
			return 0
		else:
			return 1

def main():
	win = 0
	for i in range(0, 1000):
		bandit = PlayBandit()
		print type(bandit)
		res = bandit.play()
		win += res
	print "Times played: 1000; Times won: ", win

if __name__ == '__main__':
	main()