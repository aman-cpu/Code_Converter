import java.util.*;
import java.lang.Math;

public class Test {

    // Function to calculate the area of a circle
    public static double circleArea(double radius) {
        return Math.PI * Math.pow(radius, 2);
    }

    // Function to generate a random number between 1 and 100
    public static int randomNumber() {
        Random rand = new Random();
        return rand.nextInt(100) + 1;
    }

    // Function to calculate the mean of a list of numbers
    public static double calculateMean(List<Double> numbers) {
        double sum = 0;
        for (double num : numbers) {
            sum += num;
        }
        return sum / numbers.size();
    }

    // Function to check if a number is prime
    public static boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }

    // Function to generate a list of prime numbers
    public static List<Integer> generatePrimes(int upTo) {
        List<Integer> primes = new ArrayList<>();
        for (int num = 2; num <= upTo; num++) {
            if (isPrime(num)) {
                primes.add(num);
            }
        }
        return primes;
    }

    // Function to calculate the factorial of a number
    public static long factorial(int number) {
        if (number == 0)
            return 1;
        else
            return number * factorial(number - 1);
    }

    // Function to convert Celsius to Fahrenheit
    public static double celsiusToFahrenheit(double celsius) {
        return (celsius * 9.0 / 5.0) + 32;
    }

    // Function to convert Fahrenheit to Celsius
    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5.0 / 9.0;
    }
}
