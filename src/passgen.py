import random
import string
import hashlib
import sys

M_passwrd = 0
O_passwrd = 0

if (len(sys.argv) < 4):
    print("[-]::in func::main::expected 4 arguments::recived ", len(sys.argv))

signature = sys.argv[1]
EOPsignature = sys.argv[2]
Plen = int(sys.argv[3])
store = sys.argv[4]

strs = string.ascii_letters
nums = string.digits
symb = string.punctuation

charpool = strs+symb+nums



def genpass(length):

    return ''.join(random.choice(charpool) for _ in range(length))


M_passwrd = genpass(Plen)


def sha256_hash_string(pass_to_hash):

  sha256 = hashlib.sha256()

  sha256.update(M_passwrd.encode('utf-8'))

  return sha256.hexdigest()


O_passwrd = sha256_hash_string(M_passwrd)



finale = signature + M_passwrd + O_passwrd + EOPsignature

print(f"\ngenrated pass : {M_passwrd}")
print(f"\ngenrated hashed pass : {O_passwrd}")
print(f"\nfinal password : {finale}")


if store == 'y':

    with open("secpass.key", 'w') as wr:
        wr.write(finale)
else:
    pass
