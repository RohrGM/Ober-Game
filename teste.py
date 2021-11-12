from abc import ABC, abstractmethod


class ITest(ABC):

    @abstractmethod
    def test1(self):
        pass

    @abstractmethod
    def test2(self):
        pass


class ITest2(ITest, ABC):

    @abstractmethod
    def test3(self):
        pass

    @abstractmethod
    def test4(self):
        pass


class ConcreteTeste(ITest2):

    def test3(self):
        pass

    def test4(self):
        pass

    def test1(self):
        pass

    def test2(self):
        pass


concrete = ConcreteTeste()

print(concrete.test4())
