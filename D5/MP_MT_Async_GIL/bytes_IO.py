import io
from io import StringIO, BytesIO

def create_file():
    with open("test1.txt", "wb") as f:
        f.write(b"Hello World \n")
        f.write(b"Hello World \n")
        f.write(b"Hello World \n")


def stringIO_file():
    op = StringIO()
    
    
    with StringIO() as s:
        s.write("Helloo")
        s.write("Helloo again from StringIO \n")
        s.write("Helloo the third time from StringIO .. \n")
        s.write("How to write to a file")


def bytesIO_function():
    with BytesIO() as f:
        f.write(b"Hello world from BytesIO \n")
        f.write(b"74 65 73 74 69 6e 67 20 73 74 75 66 66 20 6f 75 74")







'''
output = StringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

'''


def main():        
    create_file() # plain old with open() file...



'''from io import BytesIO

from io import StringIO
from D5.MP_MT_Async_GIL.bytes_IO import stringIO_file

def create_file():
    with open("../data/test_file.txt", "wb") as f:
        f.write(b"test string 1\n")
        f.write(b"test string 2\n")
        f.write(b"test string 3\n")
    print("File test_file.txt created")
# Load data into buffer in Bytes format
def load_data_buffer_bytesio():
    with BytesIO() as f:
        f.write(b"test string buffer 1")
        f.write(b"test string buffer 2")
        f.write(b"test string buffer 3")
        print("Output buffer from BytesIO: ")
        print(f.getvalue())
# similar can be achieved using bytes append but above is faster
def load_data_buffer():
    buffer = b""
    buffer += b"test string 1"
    buffer += b"test string 2"
    buffer += b"test string 3"
    print("Output from append Buffer: ")
    print(buffer)

def load_data_stringio():
    with StringIO() as s:
        s.write("test string StringIO 1")
        s.write("test string StringIO 2")
        s.write("test string StringIO 3")
        print("Output from StringIO: ")
        print(s.getvalue())

def main():

    test_string = "Test string data to load into StringIO object"
    #open create a file and write data to it
    create_file()

    # Instead of writing data to file, load it in buffer as bytes format using bytesio
    load_data_buffer_bytesio()

    # similar can be achieved using bytes append but above is faster
    load_data_buffer()

    # StringIO
    load_data_stringio()

    # Use StringIO object to use as a file
    in_file = StringIO(test_string)

    # Set the cursor at index 0
    in_file.seek(0)

    out_file = BytesIO(b"test_string 1")
    out_file.seek(0)
    print("byteio", out_file.read())
    print ("Writing data from StringIO file object:", in_file.read())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Error while loading data to buffer: " + str(e))'''