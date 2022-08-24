'''
クラス
__init__ 初期化を行うメソッド(コンストラクタ)
Pythonではメソッドの第一引数に自分自身(自身のインスタンス)を表すselfを明示的に書く
'''

class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized")
        
    def hello(self):
        print("Hello " + self.name)
        
    def goodbye(self):
        print("Good-bye" + self.name)

m = Man("David")
m.hello()
m.goodbye()

print(type(m))
print(m)