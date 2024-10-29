count = 0
def incremnt (n):
    """Increases by one"""
    global count
    if n > 0:
        count += 1
        incremnt(n-1)
incremnt(5)   
print(count)