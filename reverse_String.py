# Reverse a string

# Slice will give us the elements back, we select -1 in the step in order to do that
# Start(Inclusive):Stop(Exclusive):Step

def rev_sting(x):
  return x[::-1]

mytxt = rev_sting("Reversing the string is fun!!")

print(mytxt)