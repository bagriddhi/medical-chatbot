from deep_translator import GoogleTranslator

def translate(text, source_lang, target_lang):
    if source_lang == target_lang:
        return text
    return GoogleTranslator(source=source_lang, target=target_lang).translate(text)
