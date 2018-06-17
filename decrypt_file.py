# written by Gavin Kim
# 2018.06.17

LOWER_KEY = 'abcdefghijklmnopqrstuvwxyz'
UPPER_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt_file(file_name, key):
    with open('key_{0}_decrypt_file.txt'.format(key), 'w') as wf:
        with open(file_name, 'r') as rf:
            for line in rf:
                wf.write(decrypt_handler(line, int(key)))


def decrypt_handler(cipher_text, key):
    result = ''
    for c_txt in cipher_text:
        if c_txt.isalpha():
            if c_txt.islower():
                i = (LOWER_KEY.index(c_txt) - key) % 26
                result += LOWER_KEY[i]
            elif c_txt.isupper():
                i = (UPPER_KEY.index(c_txt) - key) % 26
                result += UPPER_KEY[i]
        else:
            result += c_txt
    return result


if __name__ == '__main__':
    input_key = input('Please enter key: ')
    decrypt_file('Encrypted_Result.txt',input_key)
