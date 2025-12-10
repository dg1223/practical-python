from abc import ABC, abstractmethod

class ParentInterface(ABC):
    @abstractmethod
    def parent_interface_method(self):
        pass

class MyInterface(ParentInterface):
    @abstractmethod
    def method_to_implement(self):
        pass

class InterfaceImplementer(MyInterface):
    def method_to_implement(self):
        print("method_to_implement() called.")

    # def parent_interface_method(self):
    #     print("parent_interface_method() called.")

interface = InterfaceImplementer()
interface.method_to_implement()
interface.parent_interface_method()