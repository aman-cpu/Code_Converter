import math
import random
import statistics


# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * (radius**2)


# Function to generate a random number between 1 and 100
def random_number():
    return random.randint(1, 100)


# Function to calculate the mean of a list of numbers
def calculate_mean(numbers):
    return statistics.mean(numbers)


# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


# Function to generate a list of prime numbers
def generate_primes(up_to):
    primes = []
    for num in range(2, up_to + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Function to calculate the factorial of a number
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
