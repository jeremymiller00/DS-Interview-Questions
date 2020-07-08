
def rev(s: str) -> str:
    new = []
    for i in range(1, len(s)+1):
        new.append(s[-i])
    return ''.join(new)

def rev_list(l: list) -> list:
    out = []
    for s in l:
        out.append(rev(s))
    return out


##############

if __name__ == '__main__':
    l = ['rac', 'talf', 'tot', 'tob']
    print(rev('rac'))
    print(rev_list(l))