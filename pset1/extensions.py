def main():
    file_name = input("File name: ")
    print(extract_extension(file_name))


def extract_extension(file_name):
    file_name = file_name.strip().lower()

    if '.' in file_name:
        extension = file_name.rsplit('.', 1)[-1]
    else:
        extension = ''

    match extension:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


if __name__ == "__main__":
    main()
