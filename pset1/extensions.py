def main():
    extension = input("File name: ")
    print(transform(extension))

def transform(extension):
    extension = extension.strip().lower()

    if '.' in extension:
        _, ext = extension.rsplit('.', 1)
        ext = '.' + ext
    else:
        ext = ''

    match ext:
        case ".gif":
            return "image/gif"
        case ".jpg" | ".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

if __name__ == "__main__":
    main()
