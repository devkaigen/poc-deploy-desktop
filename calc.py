class Calc:

    def add(self,x, y):
        # Add fundition
        return x + y

    def subtract(self,x,y):
        # Subtract function
        return x - y

    def multiply(self,x,y):
        # Multiply Function
        return x * y

    def divide(self,x,y):
        # Divide function
        if y ==0: 
            raise ValueError('Can not divide by zero!')
        return x / y
    
    def calculate(self, expression):
        try:
            result =eval(expression)
        except:
            result='Error'
        return result