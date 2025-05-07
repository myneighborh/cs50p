text = input()
face_map = {
    ":)": "🙂",
    ":(": "🙁"
}

face_text = text
for key, value in face_map.items():
    face_text = face_text.replace(key, value)

print(face_text)
