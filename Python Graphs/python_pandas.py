import pandas as pandas
class Test:
    def main():
        a="test"
        print(a) 
class B(Test):
    pass
class C(B):
    pass
class D(C):
    print("test123")
abj=D
D.main()    
