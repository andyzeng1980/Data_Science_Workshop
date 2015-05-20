def main():
	original_file = 'data/ratings.txt'
	training_file = 'data/training.txt'
	testing_file = 'data/testing.txt'
	with open(original_file, 'r') as input_file:
		with open(training_file, 'w') as output_training:
			with open(testing_file, 'w') as output_testing:
				line_counter = 0
				for line in input_file:
					if line_counter % 3 == 0:
						output_testing.write(line)
					else:
						output_training.write(line)
					line_counter += 1

if __name__ == '__main__':
	main()