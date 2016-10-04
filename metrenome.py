import time

def ratelimited(maxpersecond):
    mintInterval = 1.0
    def decorate (func):
    LastTimeCalled = [0.0]
    elapsed = time.clock()
LeftToWait = minInterval - elapsed
            if leftToWait>0:
                time.sleep(leftToWait)
            ret = func(*args,**kargs)
            lastTimeCalled[0] = time.clock()
            return ret
        return rateLimitedFunction
    return decorate
