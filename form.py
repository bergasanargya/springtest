import inspect
import greetings

class GreetingSerializer:
    @staticmethod
    def extract_source(file_path, properties=None, methods=None):
        """Extracts and prints the source code of the greetings module"""
        # Get the source code of the greetings module
        source_code = inspect.getsource(greetings)

        # Add properties if provided
        if properties:
            for prop_name, prop_value in properties.items():
                source_code += f"\n{prop_name} = {repr(prop_value)}"

        # Add methods if provided
        if methods:
            for _, method_func in methods.items(): #method_name
                source_code += f"\n\n{inspect.getsource(method_func)}"

        with open(file_path, 'w') as file:
            file.write(source_code)

    @staticmethod
    def add_properties_and_methods(original_class, properties=None, methods=None):
        # Create a new class that inherits from the original class
        class NewClass(original_class):
            pass

        # Add properties if provided
        if properties:
            for prop_name, prop_value in properties.items():
                setattr(NewClass, prop_name, prop_value)

        # Add methods if provided
        if methods:
            for method_name, method_func in methods.items():
                # Set the function as a class attribute
                setattr(NewClass, method_name, method_func)

        return NewClass
