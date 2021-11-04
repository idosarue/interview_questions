info = '''
    You can work on your SQL and read about:

    S&OP.
    Demand Forecasting/Planning.
    Oracle Demand Management Cloud.
    Demand Sensing.
    Trade Promotions.
'''

with open('what_to_learn.txt', 'w') as file:
    file.write(info)

def add_underscore(name):
    print(name.replace(' ', '_'))

add_underscore(input('file name: '))