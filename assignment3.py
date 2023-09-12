
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def multiply(numbers):
    result = 1
    for x in numbers:
        result = result * x
    return result

def reverse(numbers):
    new_numbers = numbers[::-1]
    return new_numbers

def main():
    
    
    s = input()
    
    n = list(map(int,s.split()))
    
    print(sum(n))
    
    print(multiply(n))
    
    print(reverse(n))
    
main()