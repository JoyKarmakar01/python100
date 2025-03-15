print("Exception Handling Starting....")
try:
    1/0
except:
    error = "Error Found .."
    print(error)
else:
    text = "Try block working fines"
    print(text)
finally:
    print("Exception Handling Done....")