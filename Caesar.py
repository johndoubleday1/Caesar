import string
import collections


def caesar(rotated_string, number_to_rotate_by):
    letters = collections.deque(string.ascii_letters)

    letters.rotate(number_to_rotate_by)

    letters = ''.join(list(letters))

    return rotated_string.translate(str.maketrans(string.ascii_letters, letters))


our_string = 'This is a test.'

for i in range(len(string.ascii_letters)):
    print(i, "|", caesar(our_string, i))



rotated_string = input(str('Enter text for Encrypt/Decrypt'))

n = input('Encrypt or Decrypt?')
print(n)
if n is 'E':
    print('this is the if statement')
    key = input('Select key:')
    key = int(key)
    number_to_rotate_by = key
    print(caesar(rotated_string, number_to_rotate_by))

if n is 'D':
    print('this is the elif statement')
    key = input('Select key:')
    key = int(key)
    number_to_rotate_by = key
    print(caesar(rotated_string, -(number_to_rotate_by)))

else:
    print('invalid input')
