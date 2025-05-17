# Unpacks a list using *
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]
print(total(*coins))


# Unpacks a dict using **
def total2(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total2(**coins))


# Prints positional arguments using args
def f(*args, **kwargs):
    print("Positional:", args)


f(*coins.values())
f(300, 300, 500, 123)
f(100, 50, 25, 100, 300, 50)


# Prints named arguments using kwargs
def f(*args, **kwargs):
    print("Names: ", kwargs)


f(**coins)
f(galleons=100, sickles=50, knuts=25, hello=30, hi=100)
f(galleons=9999)
