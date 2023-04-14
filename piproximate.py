#this program includes multiple ways of approximating pi
import math
import random

def piproximate_1(n): #this uses the newton euler convergence formula
	half_pi = 0
	fact_k = 1
	fact_2kp1 = 1
	for k in range(n):

		half_pi += ((2**k) * (fact_k ** 2)) / fact_2kp1
		fact_2kp1 = fact_2kp1 * (2 * (k + 1)) * (2 * (k + 1) + 1)
		fact_k = fact_k * (k + 1)
	return(2 * half_pi)
	


def gcd (a, b): #defines a function to return the greatest common denominator of two integers 
	if a == b:
		gcd = a
	elif a > b:
		for i in range(1, b + 1):
			if a%i == 0 and b%i == 0:
				gcd = i
	else:
		for i in range(1, a + 1):
			if a%i == 0 and b%i == 0:
				gcd = i
	return gcd


def piproximate_2(n, k): #this method uses the probability of two numbers being coprime
	coprime_count = 0 #number of pairs of coprime integers
	for i in range(n):
		a = random.randint(1, k)
		b = random.randint(1, k)
		if gcd(a,b) == 1:
			coprime_count += 1
	chi = coprime_count / n 
	print(str(coprime_count) + ' coprime pairs')
	my_pi = math.sqrt(6 / chi)
	return my_pi



def main():
	instruction = input('0) Exit \n 1) Newton / Euler Convergence Transformation \
		\n 2) Using coprime probabilities \n choose method: ')
	if instruction == '0':
		return quit()
	if instruction == '1':
		print(piproximate_1(int(input('Using terms up to: '))))
	if instruction == '2':
		n = int(input('How many trials?: '))
		k = int(input('Using random integers up to: '))
		my_pi = piproximate_2(n, k)
		print(my_pi)
		error = round((((my_pi - math.pi) / math.pi) * 100), 2)
		print('error of ' + str(error) + '%')


main()
