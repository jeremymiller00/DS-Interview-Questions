import scipy.stats as scs
import numpy as np

def make_coin():
    p_0_hidden = np.random.random()
    return p_0_hidden, scs.bernoulli(p=p_0_hidden)

def unbias(coin) -> int:
    while True:
        flips = coin.rvs(size=2)
        if (sum(flips) == 0) | (sum(flips) == 2):
            continue
        else:
            return flips[0]

def sample_coin(coin, size=1):
    output = []
    for i in range(size):
        output.append(unbias(coin))
    return output


########

if __name__ == '__main__':
    p_0, coin = make_coin()
    sample = sample_coin(coin=coin, size=10000)
    print("The uncorrected p is {}".format(p_0))  
    print("The corrected p is {}".format(np.mean(sample)))  