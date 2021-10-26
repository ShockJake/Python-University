
# 1):
# L = [3, 5, 4] ; L = L.sort()
# - nowe instrukcje powinni zaczynać się z nowej linii:

L = [3, 5, 3]
L = L.sort()

# 2):
# x, y = 1, 2, 3
# - powinna być trzecia zmienna:

x, y, z = 1, 2, 3

# 3):
# X = 1, 2, 3 ; X[1] = 4
# - trzeba dodać nawiasy, żeby X była krotką lub listą

X = [1, 2, 3]
X[1] = 4

# lub

X = (1, 2, 3)
X[1] = 4

# 4):
# X = [1, 2, 3] ; X[3] = 4
# - elementy listy zaczynają się liczyć z 0, więc podana lista nie ma elementu na pozycji [3].

# 5):
# X = "abc" ; X.append("d")
# - X jest stringem, a oni nie mają metody append()

# 6):
# L = list(map(pow, range(8)))
# - pow powinien przyjmować dwa argumenty
# - drugim parametrem metody map() jest coś co jest typu Iterable