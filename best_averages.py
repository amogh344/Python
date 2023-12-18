def get_valid_test_scores():
    while True:
        try:
            score=float(input(f'Enter the subject {i+1} test score: '))
            if 0<=score<=100:
                return score
            else:
                print('Please enter a valid test score between 0 to 100')
        except ValueError:
            print('Invalid input. Please enter a number')

test_scores=[]

for i in range(3):
    test_scores.append(get_valid_test_scores())

test_scores.sort(reverse=True)

best_test_averages=(sum(test_scores[:2]))/2

print(f'The best two averages are {best_test_averages}')
