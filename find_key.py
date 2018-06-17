# written by Gavin Kim
# 2018.06.17
LOWER_KEY = 'abcdefghijklmnopqrstuvwxyz'
UPPER_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def brute_force(cipher_text):
    for key in range(1, 26):
        result = ''
        for c_msg in cipher_text:
            if c_msg.islower():
                i = (LOWER_KEY.index(c_msg) - key) % 26
                result += LOWER_KEY[i]
            elif c_msg.isupper():
                i = (UPPER_KEY.index(c_msg) - key) % 26
                result += UPPER_KEY[i]
        print('FIND_KEY[%d]: %s' %(key, result))


if __name__ == '__main__':
    # find key from Encrypted_Result.txt file
    sample_cipher_text = 'Xypqoxzq'
    brute_force(sample_cipher_text)