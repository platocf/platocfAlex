class A(object):
    _count=0
    def __init__(self):
        self._o = 88
        self.__private()
        self.public()
        pass
    def __private(self):
        print 'A.__private()'

    def public(self):
        print 'A.public()'


class B(A):
    def __private(self):
        print 'B.__private()'

    def public(self):
        print 'B.public()'
        print self._o

b = B()