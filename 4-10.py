# Define a decorator called test that prints 'start' when a function is called and
# 'end' when it finishes.

def document_it():
        def new_function():
            return 'start'
        print(new_function())
        return 'end'

print(document_it())

