# encapsulation method
# first we create class whith some name
class Example:
# after we create function for take our atribut
    def __init__(self,name):
# now will be add privet atribut
      self.__name = name
# now publick methods give the assses priver attribute
    def get_name (self):
      return self.__name

# now its publik method just modifai our privet method
    def set_name (self,new_name):
      self.__name = new_name


ex = Example ('Raii')
print(ex.get_name())
      

      








        
        
        
    



        






