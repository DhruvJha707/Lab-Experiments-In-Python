'''Create multiple suitable exceptions for a file handling program. '''

# Program to demonstrate multiple exceptions in file handling

try:
    # Ask user for file name
    filename = input("Enter file name: ")

    # Open the file
    f = open(filename, "r")

    # Read and display file content
    content = f.read()
    print("\nFile Content:\n")
    print(content)

    f.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: You do not have permission to access this file.")

except IOError:
    print("Error: Problem occurred while reading the file.")

except Exception as e:
    print("Unexpected Error:", e)

finally:
    print("\nProgram execution completed.")
