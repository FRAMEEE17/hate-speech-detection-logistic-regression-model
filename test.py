def main():
    number = get_number()
    meow(number)
def get_number():
    n = int(input("Enter the times of meow :"))
    print(n)
    if n > 0:
        return n
def meow(n):
    for i in range(n):
        print("Meow")
print(main())