alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'blue', 'points': '6'}
print(alien_0['color'])
print(alien_0['points'])
for key, value in alien_0.items():
    print("key: " + key)
    print("value: " + value)
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'edward': 'ruby',
                      'phil': 'python'}

for l in favorite_languages.keys():
    print(l)
for name in favorite_languages:
    print(name)
print(favorite_languages.keys()) # keys
print(favorite_languages.values())   # values
# sorted
for name in sorted(favorite_languages.keys()):
    print(name)
