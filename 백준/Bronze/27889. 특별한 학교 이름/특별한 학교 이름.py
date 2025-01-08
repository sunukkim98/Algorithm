import sys

name = ['NLCS', 'BHA', 'KIS', 'SJA']
input_name = sys.stdin.readline().strip()
if input_name == name[0]:
    print('North London Collegiate School')
elif input_name == name[1]:
    print('Branksome Hall Asia')
elif input_name == name[2]:
    print('Korea International School')
elif input_name == name[3]:
    print('St. Johnsbury Academy')