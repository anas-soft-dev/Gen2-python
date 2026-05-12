
def fun():
    count=5
    count-=1
    if count>0:
        fun()
    print(count)

fun()