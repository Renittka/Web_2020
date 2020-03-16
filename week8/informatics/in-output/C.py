# N школьников делят K яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому
# школьнику?
from math import floor
a = int(input())
b = int(input())
print(str(floor(b/a)))