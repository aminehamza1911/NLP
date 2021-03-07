from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)

from tqdm import tqdm

with open('sentences', 'r') as f:
    contents = f.read()

google_translated = []

for line in tqdm(contents.split('\n')):
    google_translated.append(GoogleTranslator(source='english', target='french').translate(line)


with open('google_trans', 'w') as f:
    f.write('\n'.join(google_translated))