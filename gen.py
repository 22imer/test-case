import random
import os

# Ensure the output directory exists
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Generate a unique file name within the output directory
seed = random.randint(1, 1000)
file_path = os.path.join(output_dir, f'output{seed}.txt')
file = open(file_path, 'w')

def number_of_test():
    a, b = lay_2_so()
    test = random.randint(a, b)
    return test

def dang_ky_tu():
    i = int(input('Chon kieu du lieu (0:int, 1:float): '))
    switch = {
        0: 'int',
        1: 'float',
    }
    return switch.get(i, "Nhap lai")

def lay_2_so():
    print('Trong khoang [a,b]')
    a = int(input('a = '))
    b = int(input('b = '))
    if a > b:
        a, b = b, a
    return a, b

def lay_so_thap_phan():
    return int(input('Nhap so chu so thap phan: '))

def format_float(value, decimals):
    formatted_value = f"{value:.{decimals}f}"
    return formatted_value.replace('.', ',')

def tinh_toan(a, b, data_type):
    if data_type == 'int':
        element = random.randint(a, b)
    elif data_type == 'float':
        element = random.uniform(a, b)
        decimals = lay_so_thap_phan()
        element = round(element, decimals)
        element = f"{element:.{decimals}f}"  # Format float to specified decimal places
    return element

def mang_1(a, b, data_type):
    N = int(input('So luong phan tu N: '))
    array = []
    for _ in range(N):
        if data_type == 'int':
            element = random.randint(a, b)
        elif data_type == 'float':
            decimals = lay_so_thap_phan()
            element = random.uniform(a, b)
            element = round(element, decimals)
            element = f"{element:.{decimals}f}"
        array.append(element)
        file.write(f'{element} ')
    file.write(f'\n')
    return array

def mang_2(a, b, data_type):
    rows = int(input('So hang: '))
    cols = int(input('So cot: '))
    file.write(f'{rows} {cols}')
    array = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if data_type == 'int':
                element = random.randint(a, b)
            elif data_type == 'float':
                decimals = lay_so_thap_phan()
                element = random.uniform(a, b)
                element = round(element, decimals)
                element = f"{element:.{decimals}f}"
            row.append(element)
            file.write(f'{element} ')  # Write elements in a row separated by space
        array.append(row)
        file.write('\n')  # New line after each row
    return array

def xau():
    print('Xau dai khoang [a,b]')
    a, b = lay_2_so()
    length = random.randint(a, b)
    result = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
    file.write(f'{result}\n')
    return result

def ui():
    test_en = int(input('Co can test case Co:1 Khong:0 '))
    if test_en == 1:
        print('So luong test case:')
        test = number_of_test()
        file.write(f'{test}\n')
    else:
        test = 1
    print("Dang bai:")
    print("1. Tinh toan N")
    print("2. Mang 1 chieu")
    print("3. Mang 2 chieu")
    print("4. Dang Xau")
    choice = int(input('Chon dang bai (1-4): '))

    # Get the range [a, b] and data type only once for all test cases
    a, b = lay_2_so()
    data_type = dang_ky_tu()

    if choice == 1:
        for _ in range(test):
            result = tinh_toan(a, b, data_type)
            print('Gia tri da tao:', result)
            file.write(f'{result}\n')
    elif choice == 2:
        for _ in range(test):
            result = mang_1(a, b, data_type)
            print('Mang 1 chieu:', result)
    elif choice == 3:
        for _ in range(test):
            result = mang_2(a, b, data_type)
            print('Mang 2 chieu:', result)
    elif choice == 4:
        for _ in range(test):
            result = xau()
            print('Xau da tao:', result)
    else:
        print('Chuc nang chua duoc ho tro.')

def main():
    ui()
    file.close()

if __name__ == "__main__":
    main()
