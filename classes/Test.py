class Comparator:
    x = 4
    def print_max(self, a, b):
        if a > b:
            print(a," is bigger")
        elif a < b:
            print(b,"is bigger")
        else:
            print("they are equale")   

comp = Comparator()
comp2 = Comparator()
comp.print_max(5,5)
comp2.print_max(33,44)
comp.x = 67
print(comp.x)
print(comp2.x)

