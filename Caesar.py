import string
import collections


def caesar(rotated_string, number_to_rotate_by):
    letters = collections.deque(string.ascii_letters)

    letters.rotate(number_to_rotate_by)

    letters = ''.join(list(letters))

    return rotated_string.translate(str.maketrans(string.ascii_letters, letters))





while True:
    rotated_string = input(str('Enter text for Encrypt/Decrypt:'))

    n = input('Encrypt or Decrypt (e/d)?')
    print(n)
    if 'e' == n:
        print('Encrypting')
        key = input('Select key number:')
        key = int(key)
        number_to_rotate_by = key
        print(caesar(rotated_string, number_to_rotate_by))

    else:
        print('Decrypting')
        key = input('Select key number:')
        key = int(key)
        number_to_rotate_by = key
        print(caesar(rotated_string, -(number_to_rotate_by)))

    while True:
        answer = input('Run again?(y/n):')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break
