
# TASK: WRITE A PROGRAM TO VALIDATE USERNAME USEING REGULAR EXPRESSIONs.
# the program should check if a given username meets specific criteria and print an appropriate message 
# indicating weather username is valid or not 


# Criteria for valid usenrame:
# Username length 3 to 15 characters 
# allowed characters only alphanumeric characters, dashes(-), and underscores(_),
# starting characters must start with a letter (either uppercase or lowercase)
#ending characters must not end with an underscore or dash 


# Regular expression 
# '^[a-zA-Z][a-zA-Z0-9_-]{2,14}[a-zA-Z0-9]$'



# 2........................................
# TASK:
# Must contain at least one leteter and at least one number 
# At least eight characters long(symbol also included)

# Positive lookahead ?=
# ^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d\S]{8,}$