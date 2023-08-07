from io import StringIO
import sys 


# def chunk_data(input_string, buffer_size):
#     # Create a StringIO object to read the input string
#     input_stream = StringIO(input_string)

#     while True:
#         # Read the next chunk of data with the specified buffer size
#         chunk = input_stream.read(buffer_size)
#         if not chunk:
#             # If there is no more data to read, break out of the loop
#             break

#         # Process the current chunk (you can modify this part according to your requirements)
#         print("Processing chunk:", chunk)

# if __name__ == "__main__":
#     # Sample input string (you can replace this with your actual input data)
#     input_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at justo vitae elit feugiat venenatis."
    
#     # Set the buffer size (adjust this according to your needs)
#     buffer_size = 20

#     # Call the chunk_data function with the input string and buffer size
#     chunk_data(input_string, buffer_size)


def chunking(input_string, buffer=10):
    input_stream = StringIO(input_string)
    print(sys.getsizeof(input_stream) )
    
    while True:
        chunk = input_stream.read(buffer)
        
        if not chunk:
            break

        print("Processing chunk:", chunk)

# def 


if __name__ == "__main__":
    istring = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam at justo vitae elit feugiat venenatis. Here is one more sentence. Are we loading in there this first...."
    
    buffer_size = 20 
    
    chunking(input_string=istring, buffer=buffer_size)