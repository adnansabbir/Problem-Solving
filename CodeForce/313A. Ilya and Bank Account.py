def llya_bank_account():
    balance_str = input()

    if balance_str[0] == '-':
        balance_str = '0' + balance_str[1:]
        return int(balance_str[:-1] if balance_str[-1] > balance_str[-2] else balance_str[:-2] + balance_str[-1]) * -1
    else:
        return balance_str


if __name__ == '__main__':
    print(llya_bank_account())
