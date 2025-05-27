try:
    #n=int(input("enter n1"))
    res = 100 / e

except ZeroDivisionError:
    print("You can't divide by zero!")

except NameError:
    print("not defined")
except ValueError:
    print("Enter a valid number!")
except TypeError:
    print("Type is not correct")

else:
    print("Result is", res)

finally:
    print("Execution complete.")