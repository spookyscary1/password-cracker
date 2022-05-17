import argparse
import sys
import crypt
import timeit

begin = timeit.default_timer()


parser = argparse.ArgumentParser(description='A program to crack passwords')

parser.add_argument("hash", help="The hash to be cracked")
parser.add_argument('wordlist', type=argparse.FileType('r'),default=sys.stdout,help='The wordlist to use')
args = parser.parse_args()

# print(type(args.wordlist))

wordlist=args.wordlist.readlines()

for word in wordlist:
    word = word.replace('\n','')
    attempt=crypt.crypt(word, str(args.hash))
    # //print(attempt)
    if (attempt== args.hash):
        print("cracked: "+ str(word))
        break


end = timeit.default_timer()

print('Time: ', end - begin) 

