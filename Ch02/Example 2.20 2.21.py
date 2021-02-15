import sys
print(sys.getrefcount(1921))

getre_val_1 = 1921

print(sys.getrefcount(1921))

getre_val_2 = 1921

print(sys.getrefcount(1921))

getre_val_3 = [1921, 1922, 1923]

print(sys.getrefcount(1921))

getre_val_3[0] = 1924

print(sys.getrefcount(1921))

del getre_val_1

print(sys.getrefcount(1921))

getre_val_2 = 1924
print(sys.getrefcount(1921))