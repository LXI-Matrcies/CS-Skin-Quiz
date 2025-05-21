import os
from os.path import isfile, join
location = ".\All CS Knives"
pictures = [file for file in os.listdir(location) if isfile(join(location, file))]
print('\n\n')
print('Files: ')
print('[' + ', '.join(map(lambda x: f'"{x}"', pictures)) + ']')
print('')