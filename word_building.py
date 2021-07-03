# Define combine_words below:
def combine_words(word, **kwargs):
    if 'prefix' in kwargs:
        return f"{kwargs['prefix']}{word}"
    elif 'suffix' in kwargs:
        return f"{word}{kwargs['suffix']}"
    else:
        return word

print(combine_words('child'))
print(combine_words('child', prefix='man'))
print(combine_words('child', suffix='ish'))
print(combine_words('work', suffix='er'))
print(combine_words('work', prefix='home'))