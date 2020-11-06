# Определить является ли число палиндромом.Число является палиндромом если прочитанное справа налево равно
# исходному числу.
#
# Пример: 12121 - палиднром 1212 - не палиндром
#
# Важное требование: запрещается исходное число конвертировать в строку и применять к ней функцию реверсирования.
# Проверку требуется проводить применяя математические операции кисходному числу!

def main():
    input_number: int = 12121
    investigated_number: int = input_number
    reverse_numbers: [int] = []

    while investigated_number > 0:
        num_part: int = investigated_number % 10
        investigated_number = investigated_number // 10
        reverse_numbers.append(num_part)

    result: int = 0

    for num_part in reverse_numbers:
        result = result * 10
        result = result + num_part
        print(f"num_part: {num_part} result: {result}")

    print(f"result: {result} is palindrome: {input_number == result}")

    if input_number == result:
        print("Palindrome")
    else:
        print("No Palindrome")


if __name__ == "__main__":
    main()
