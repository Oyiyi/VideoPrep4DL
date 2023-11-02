from pypinyin import pinyin, Style

# Function to translate Chinese characters to Pinyin and replace spaces with underscores
def convert_title(text):
    pinyin_text = ''
    for char in text:
        # Check if the character is Chinese
        if '\u4e00' <= char <= '\u9fff':
            # Convert Chinese character to Pinyin using default style
            pinyin_result = pinyin(char, style=Style.NORMAL)
            pinyin_text += pinyin_result[0][0]  # Extract the Pinyin result
        else:
            pinyin_text += char  # Keep non-Chinese characters as is
    
    # Replace spaces with underscores
    pinyin_text = pinyin_text.replace(' ', '_')
    pinyin_text = pinyin_text.replace('|', '')
    pinyin_text = pinyin_text.replace('__', '_')
    return pinyin_text

# Mixed Chinese and English text
#mixed_text = "甄嬛传 01 高清 Empresses in the Palace 01"

# Translate and replace Chinese words with Pinyin
#translated_text = convert_title(mixed_text)

# Print the translated text
#print(translated_text)
