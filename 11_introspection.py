
def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    attrs = [attr for attr in attributes if not callable(getattr(obj, attr))]
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__

    intr_info = {'type': obj_type, 'attributes': attrs,
                    'methods': methods, 'module': module}

    return intr_info


class Myclass:
    def __init__(self):
        self.name = 'Myclass'
        self.description = 10
        self.attributes = 10

    def my_method(self):
        pass

obj = Myclass()

number_info = introspection_info(42)
print(number_info)