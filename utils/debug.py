def debug_class(cls):
    class wrapper(cls):
        def __init__(self,*args,**kwargs):
            print(f"{cls.__name__} is constructed:\nUsed variables:")
            for i,arg in enumerate(args):
                print(f"Argument {i+1}: {arg}")
            for key,value in kwargs.items():
                print(f"{key}: {value}")
            super().__init__(*args,**kwargs)
            print(f"{cls.__name__}({super()})")
        
    return wrapper

def Debug(func):
    def wrapper(*args,**kwargs):
        print("*"*50)
        print(f"{func.__name__} is executed:\nUsed variables:")
        for i,arg in enumerate(args):
            print(f"Argument {i+1}: {arg}")
        for key,value in kwargs.items():
            print(f"{key}: {value}")
        output = func(*args,**kwargs)
        print(f"Result: {output}\n")
        print("*"*50)
        return output
    return wrapper

def cls_method_debug(cls_func):
    def wrapper(cls,*args,**kwargs):
        print("*"*50)
        print(f"{cls_func.__name__} of {type(cls).__name__} is executed:\nUsed variables:")
        for i,arg in enumerate(args):
            print(f"Argument {i+1}: {arg}")
        for key,value in kwargs.items():
            print(f"{key}: {value}")
        output = cls_func(cls,*args,**kwargs)
        print(f"Result: {cls}")
        print("*"*50)
        return output
    return wrapper