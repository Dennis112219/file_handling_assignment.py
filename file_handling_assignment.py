# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1.\n")
        file.write("Line 2 contains numbers: 12345.\n")
        file.write("The third line is for demonstration.\n")
    print("File created and written successfully.")

except FileNotFoundError:
    print("Error: The file or directory does not exist.")
except PermissionError:
    print("Error: Permission denied while trying to create the file.")
except Exception as e:
    print("An unexpected error occurred:", str(e))

finally:
    # File Reading and Display
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read the contents of "my_file.txt" and display them on the console
            print("Contents of my_file.txt:")
            for line in file:
                print(line, end='')

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' does not exist.")
    except PermissionError:
        print("Error: Permission denied while trying to read the file.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

    finally:
        # File Appending
        try:
            # Open "my_file.txt" in append mode ('a')
            with open("my_file.txt", "a") as file:
                # Append three additional lines of text to the existing content
                file.write("This is an appended line.\n")
                file.write("Another appended line with numbers: 54321.\n")
                file.write("Appending more data for demonstration.\n")
            print("Data appended successfully.")

        except FileNotFoundError:
            print("Error: The file 'my_file.txt' does not exist.")
        except PermissionError:
            print("Error: Permission denied while trying to append to the file.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))
