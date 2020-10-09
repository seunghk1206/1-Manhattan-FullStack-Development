file = open('./macroFolder/macrofile_0.txt', 'r')
print([each for each in file.read().split('\n')])