import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'<iframe[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/(?P<video_id>[\w-]+)"[^>]*></iframe>', s):
        prefix = "https://youtu.be/"
        video_id = match.group("video_id")
        return prefix + video_id
    else:
        return None


if __name__ == "__main__":
    main()
