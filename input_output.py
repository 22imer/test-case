import random

# Function to get user input for the range of test cases
def lay_2_so():
    print('Trong khoang [a,b]')
    a = int(input('a = '))
    b = int(input('b = '))
    return a, b

# Function to get the type of a particular input
def dang_ky_tu():
    i = int(input('Chon kieu du lieu (0:int, 1:float, 2:string): '))
    switch = {
        0: 'int',
        1: 'float',
        2: 'string',
    }
    return switch.get(i, "Nhap lai")

# Function to choose a calculation type
def tinh_toan():
    print(f'Gia tri N trong khoang [a,b]')
    data_type = dang_ky_tu()
    while True:
        if data_type == 'int':
            print('Nhap phan tu (int): trong khoang [a,b]')
            a, b = lay_2_so()
            element = random.randint(a, b)
            break
        elif data_type == 'float':
            print('Nhap phan tu (float): trong khoang [a,b]')
            a, b = lay_2_so()
            element = random.uniform(a, b)
            break
        else:
            print("Loai du lieu khong hop le. Thu lai.")
            data_type = dang_ky_tu()
    return element

# Function to get the number of test cases
def number_of_test():
    a, b = lay_2_so()
    test = random.randint(a, b)
    return test

# Function to write the test case count and results to a file
def write_to_file(test, data, choice):
    seed = random.randint(1, 1000)
    with open(f'output{seed}.txt', 'w') as file:
        file.write(f'Test case: {test}\n')
        file.write(f'Choice: {choice}\n')
        file.write(f'Result: {data}\n')

# Function to create a 1D array based on user input
def mang_1():
    N = int(input('So luong phan tu N: '))
    print('Phan tu la dang')
    data_type = dang_ky_tu()

    array = []
    for _ in range(N):
        if data_type == 'int':
            print('Nhap phan tu (int): trong khoang [a,b]')
            a, b = lay_2_so()
            element = random.randint(a, b)
        elif data_type == 'float':
            print('Nhap phan tu (float): trong khoang [a,b]')
            a, b = lay_2_so()
            element = random.uniform(a, b)
        else:
            print("Loai du lieu khong hop le. Thu lai.")
            return []

        array.append(element)
    
    return array

# Function to display the UI and handle user choice
def ui():
    print('So luong test case:')
    test = number_of_test()
    print("Dang bai:")
    print("1. Tinh toan a,b")
    print("2. Mang 1 chieu")
    print("3. Mang 2 chieu")
    print("4. Dang Xau")

    choice = int(input('Chon dang bai (1-4): '))

    if choice == 1:
        for _ in range(test):
            result = tinh_toan()
            write_to_file(test, result, choice)
            print('Ket qua tinh toan:')
            print(result)
        
    elif choice == 2:
        for _ in range(test):
            array = mang_1()
            if array:
                write_to_file(test, array, choice)
                print('Mang vua nhap:')
                print(array)
        
    else:
        print("Chuc nang chua duoc ho tro.")

# Main function
def main():
    ui()

if __name__ == "__main__":
    main()
