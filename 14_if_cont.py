# we can combine boolean statements
i = 6

True and True == True
True and False == False
False and False == False
True or True == True
True or False == True
False or False == False

if i < 10 and i > 5:
    print("i is less than 10 and greater than five")

if i < 5 or i < 10:
    print("i is less than five or less than 10")

# We can group logical statements together with paranetheses
if (i > 5 and i < 10) or i > 100:
    print("i fits the criteria")

# there are useful boolean expressions for strings as well
if "run" in "I run the team":
    print("found 4un")

if "run" not in "I run the team":
    print("didn't find run")

if not False:
    print("hello")