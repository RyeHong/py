# Define an exception called OopsException. Raise this exception to see what happens.
# Then write the code to catch this exception and print 'Caught an oops'.

short_list = [1, 2, 3]
position = 5
try:
          raise Exception(short_list[position])
except Exception as OopsException:
        print('Caught an oops')