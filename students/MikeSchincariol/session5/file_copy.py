import os.path

def file_copy(src, dst):

    CHUNK_SIZE = 128

    # Open the files for reading and writing. Don't try
    # and catch any errors as we want the caller to get the exception
    # and deal with it.
    num_bytes_copied = 0
    with open(src, "rb") as src_fd:
        with open(dst, "wb") as dst_fd:
            while True:
                # Read in at most CHUNK_SIZE bytes and then write them
                # to the output stream. Keep track of how many byes
                # have been transferred.
                buf = src_fd.read(CHUNK_SIZE)
                if len(buf) == 0:
                    break
                else:
                    num_bytes_copied += len(buf)
                    dst_fd.write(buf)
    print("{0} bytes copied".format(num_bytes_copied))


if __name__ == "__main__":
    file_copy("students.txt", "students_copy.txt")