import time
from ibus import IBus

ibus_in = IBus(1)


while True:
    res = ibus_in.read()
    # if signal then display immediately
    if (res[0] == 1):
        print ("Status {} Ch 1 {} Ch 2 {} Ch 3 {} Ch 4 {} Ch 5 {} Ch 6 {}".format(
            res[0],    # Status
            IBus.normalize(res[1]),
            IBus.normalize(res[2]),
            IBus.normalize(res[3]),
            IBus.normalize(res[4]),
            IBus.normalize(res[5], type="dial"),
            IBus.normalize(res[6], type="dial")),
            end="")
        print (" - {}".format(time.ticks_ms()))
    else:
        #print ("Status offline {}".format(res[0]))
        #time.sleep(0.1)
        pass