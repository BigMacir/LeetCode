class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Generating an array:
        numbers = []
        for i in range(1, n+1):
            numbers.append(i)
        
        # Iterating through:
        for i, number in enumerate(numbers):

            if (number % 3 == 0) and (number % 5 == 0):
                numbers[i] = "FizzBuzz"
            elif (number % 3 == 0):
                numbers[i] = "Fizz"
            elif (number % 5 == 0):
                numbers[i] = "Buzz"
            else:
                numbers[i] = str(number)
            continue

        return numbers