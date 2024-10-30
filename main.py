import random

def main():
    while True:
        print('歡迎來到四則運算練習')
        print('1. 加')
        print('2. 減')
        print('3. 乘')
        print('4. 除')
        print('0. 結束練習')

        try:
            operator_str = str(input('請輸入您要練習的運算符代碼：'))
        except ValueError:
            print('輸入無效，請重新輸入')
            continue

        # 檢查使用者是否選擇結束
        if operator_str == '0':
            print('感謝您的使用，再見！')
            break

        # 檢查輸入的運算符是否有效
        if operator_str not in ['1', '2', '3', '4']:
            print('無效的選項，請重新輸入')
            continue

        while True:
            operation = convert_operator(operator_str)
            if not get_check_number(f'練習{operation}法，正確請按 \'1\'，重新選擇運算符號請按 \'0\'： '):
                break

            digits_of_first_number, digits_of_second_number = get_digit_numbers_with_confirmation()
            print(f'已確認的第一個數字位數：{digits_of_first_number}，第二個數字位數：{digits_of_second_number}')

            first_numbers = get_random_numbers(digits_of_first_number)
            second_numbers = get_random_numbers(digits_of_second_number)

            if operation == '/':
                while True:
                    try:
                        user_quotient = int(input(f'{first_numbers} / {second_numbers} 的商為：'))
                        user_remainder = int(input(f'{first_numbers} / {second_numbers} 的餘數為：'))
                        correct_quotient, correct_remainder = compute(first_numbers, second_numbers, '/')
                        if user_quotient == correct_quotient and user_remainder == correct_remainder:
                            if input(f'恭喜您答對了，繼續請按 \'1\'，重新選擇數字位數請按 \'0\'： ') == '1':
                                first_numbers = get_random_numbers(digits_of_first_number)
                                second_numbers = get_random_numbers(digits_of_second_number)
                                continue
                            else:
                                break
                        else:
                            print('很抱歉您答錯了，請重新作答')
                            continue
                    except ValueError:
                        print("請輸入數字！")
            else:
                while True:
                    try:
                        if int(input(f'{first_numbers}{operation}{second_numbers}=')) == compute(first_numbers, second_numbers, operation):
                            if input(f'恭喜您答對了，繼續請按 \'1\'，重新選數字擇位數請按 \'0\'： ') == '1':
                                first_numbers = get_random_numbers(digits_of_first_number)
                                second_numbers = get_random_numbers(digits_of_second_number)
                                continue
                            else:
                                break
                        else:
                            print('很抱歉您答錯了，請重新作答')
                            continue
                    except ValueError:
                        print("請輸入數字！")

# 轉換運算符
def convert_operator(operator_str: str) -> str:
    """
    將運算符選擇數字轉換為對應的運算符號。

    參數:
    operator_str (str): 代表運算符的字串數字，取值為 '1'、'2'、'3' 或 '4'。

    返回:
    str: 對應的運算符號。選擇 '1' 返回 '+'，'2' 返回 '-'，'3' 返回 '*'，'4' 返回 '/'。

    若 `operator_str` 的值不在 '1'、'2'、'3' 或 '4' 之中，將引發 MatchError。
    """
    match operator_str:
        case '1':
            return '+'
        case '2':
            return '-'
        case '3':
            return '*'
        case '4':
            return '/'

# 生成隨機數
def get_random_numbers(digit_numbers: int) -> int:
    """
    根據輸入的位數生成對應範圍的隨機整數。

    參數:
    digit_numbers (int): 指定隨機數的位數。可接受的值為 1 到 5。

    返回:
    int: 生成的隨機整數。

    使用方法:
    - 若 `digit_numbers` 為 1，則返回 1 到 9 的隨機整數。
    - 若 `digit_numbers` 為 2，則返回 10 到 99 的隨機整數。
    - 若 `digit_numbers` 為 3，則返回 100 到 999 的隨機整數。
    - 若 `digit_numbers` 為 4，則返回 1000 到 9999 的隨機整數。
    - 若 `digit_numbers` 為 5，則返回 10000 到 99999 的隨機整數。
    """
    match digit_numbers:
        case 1:
            return random.randint(1, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case 4:
            return random.randint(1000, 9999)
        case 5:
            return random.randint(10000, 99999)


# 確認位數
def get_digit_numbers_with_confirmation() -> tuple[int, int]:
    """
    取得兩個數字的位數，並讓使用者確認輸入是否正確。
    若使用者確認輸入正確，返回兩個數字的位數，否則重新輸入。

    返回值:
    tuple[int, int]: 返回確認後的兩個數字位數。
    """
    while True:
        # 獲取第一個和第二個數字的位數
        digits_of_first_number = get_digit_number('請輸入第一個數字的位數 (1-5): ')
        digits_of_second_number = get_digit_number('請輸入第二個數字的位數 (1-5): ')

        # 顯示輸入的位數
        print(f'第一個數字的位數：{digits_of_first_number}，第二個數字的位數：{digits_of_second_number}。')

        # 確認輸入是否正確
        check_number = get_check_number('正確請按 \'1\'，重新選擇數字位數請按 \'0\'： ')
        if check_number:  # 若確認輸入正確
            return digits_of_first_number, digits_of_second_number


# 取得確認數字
def get_check_number(prompt: str) -> bool:
    """
    根據使用者的輸入返回布林值。
    提示使用者輸入 1 表示「正確」並返回 True，或輸入 0 表示「重新輸入」並返回 False。
    若輸入的值無效，會持續要求重新輸入，直到輸入正確的數字。

    參數:
    prompt (str): 顯示給使用者的提示訊息。

    返回值:
    bool: 如果輸入 1，返回 True；如果輸入 0，返回 False。
    """
    while True:
        try:
            check_number = int(input(prompt))
            if check_number == 1:
                return True
            elif check_number == 0:
                return False
            else:
                print('請輸入 1(正確) 或 0 (重新輸入)')
        except ValueError:
            print('請輸入 1(正確) 或 0 (重新輸入)')


# 取得位數
def get_digit_number(prompt: str) -> int:
    """
    根據使用者的輸入返回一個位數的整數值。
    提示使用者輸入 1 到 5 的整數來表示位數，若輸入無效或不在範圍內，會要求重新輸入。

    參數:
    prompt (str): 顯示給使用者的提示訊息。

    返回值:
    int: 使用者輸入的有效位數（1-5 之間的整數）。
    """
    while True:
        try:
            digit_number = int(input(prompt))
            if digit_number < 0:
                print('輸入位數不可小於0，請重新輸入')
            elif digit_number > 5:
                print('輸入位數不可大於5，請重新輸入')
            elif digit_number < 1:
                print('輸入位數不可小於1，請重新輸入')
            else:
                return digit_number
        except ValueError:
            print('輸入無效，請輸入一個有效的整數')

# 比對答案
def compute(a: int, b: int, operation: str):
    """
    根據指定的運算符號對兩個數字進行計算，並返回結果。

    參數:
    a (int): 第一個整數運算數。
    b (int): 第二個整數運算數。
    operation (str): 運算符號，支持 '+', '-', '*', '/'。

    返回:
    int 或 tuple: 根據運算符返回不同類型的結果：
        - '+' 返回 a 和 b 的加法結果。
        - '-' 返回 a 和 b 的減法結果。
        - '*' 返回 a 和 b 的乘法結果。
        - '/' 返回 divmod(a, b) 的結果，即 (商, 餘數) 的元組。

    當 operation 為不支持的運算符時，拋出 ValueError。

    拋出:
    ValueError: 如果 operation 不是 '+', '-', '*', '/' 之一。
    """
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return divmod(a, b)
        case _:
            raise ValueError("不支持的運算類型")



if __name__ == "__main__":
    main()



