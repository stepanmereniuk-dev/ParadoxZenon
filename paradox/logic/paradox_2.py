import time

if __name__ == "__main__":
    s = 0
    d = 0.5
    f = 1
    while s <= 1:
        
        s = s + d
        d = d/2
        time.sleep(1)
        print(s)
        pass

