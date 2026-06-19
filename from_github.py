import sys

def github():
  """This is branch is created from Github."""
  response = input("Why are you here? ")

  if len(response) < 5:
    print("You're dead!")
    sys.exit(4)
  
  print("I see. Please proceed.")
  sys.exit(0)


if __name__ == "__main__":
  github()
