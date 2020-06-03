from time import sleep
cont = None
ended = None
def Run():
    global cont
    global ended
    for cont in range(550, -1, -1):
        print(cont)
        sleep(0.5)
    print("ENDED")
    ended = cont
Run()