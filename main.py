import hashlib

file1="file1.pdf"
file2 ="file2.pdf"

def generate_hash(input_file_path):
    m =  hashlib.sha1()
    with open(input_file_path, "rb") as f:
        file_content =  f.read()
        print(f"File content, {file_content}")
        m.update(file_content)
    return m.hexdigest()


def main():
    print("Welcome to PDF file compare app")
    file1_hash = generate_hash(file1)
    file2_hash =  generate_hash(file2)
    if file1_hash == file2_hash:
        print("The file is Identical")
    else:
        print("The file is diffrent")
    


if __name__ == "__main__":
    main()