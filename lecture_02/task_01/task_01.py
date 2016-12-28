read_from_console = input()

if len(read_from_console) < 10:
    print(read_from_console)
else:
    print(read_from_console[0:10] + '...')
