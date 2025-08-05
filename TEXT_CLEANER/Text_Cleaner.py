import string

def text_cleaner(text):
    text=text.title()
    text=text.strip()
    text=text.translate(str.maketrans("","",string.punctuation))
    text=[i for i in text if not i.isdigit()]
    text=''.join(text)
    return text
text=input("Enter text to clean:")
text_cleaned=text_cleaner(text)
print("Cleaned text:", text_cleaned)
