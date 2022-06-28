if __name__ == "__main__":
    s = input()
    bolim = []
    yopish = {")":"(","]":"[","}":"{"}
    for c in s:
        if c in yopish:
            if bolim and bolim[-1] == yopish[c]:
                bolim.pop()
            else:
                print(False)
        else:
            bolim.append(c)
    print(True if not bolim else False)