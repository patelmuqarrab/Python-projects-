def main():
    print("Thank You for using the Email slicer built by patelmuqarrab")
    print("")

    in_email = input("Please enter your email: ")

    (username,domain_name) = in_email.split("@")
    (domain_name,extention) = domain_name.split(".")
    
    print("Username: ",username)
    print("Domain: ",domain_name)
    print("Extention: ",extention)

while True:
    main()