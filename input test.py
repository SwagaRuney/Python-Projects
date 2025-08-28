import time

mad_lib_custom = """                                                                      "The Curse of Professor Bugsworth"
It was a(n) {0} day at [school name], and everyone was excited for {1} class—except for one reason: Professor Bugsworth.
Rumor had it that Professor Bugsworth once coded a(n) {3} so powerful, it crashed every {4} in the world. With their {5} always twitching and their {6} glare, Bugsworth would enter the classroom wearing a {7} cloak and muttering about {8}.
“Today,” Bugsworth hissed, “we’ll be programming a(n) {9} simulator using {10}. If anyone forgets a semicolon, they’ll be turned into a(n) {11}!”
I nervously opened my {12}, only to find it had been replaced with a {13}. My partner, {14}, whispered, “I think Bugsworth is trying to summon the ancient algorithm of {15}!”
Suddenly, the lights flickered, and the code on the screen began to spell out: “{16}”. That’s when we knew—we had to debug the evil spell before {17} o’clock, or we’d be trapped in an infinite loop of {18} forever.

"""
madlib = mad_lib = """ "The Curse of Professor Bugsworth" [adjective] day at [school name], and everyone was excited for [subject] class—except for one reason: Professor Bugsworth. Rumor had it that Professor Bugsworth once coded a(n) [noun] so powerful, it crashed every [plural noun] in the world. With their [body part] always twitching and their [adjective] glare, Bugsworth would enter the classroom wearing a [color] cloak and muttering about [plural noun]. “Today,” Bugsworth hissed, “we’ll be programming a(n) [animal] simulator using [programming language]. If anyone forgets a semicolon, they’ll be turned into a(n) [silly noun]!” I nervously opened my [electronic device], only to find it had been replaced with a [gross object]. My partner, [friend’s name], whispered, “I think Bugsworth is trying to summon the ancient algorithm of [mythical name]!” Suddenly, the lights flickered, and the code on the screen began to spell out: “[creepy phrase]”. That’s when we knew—we had to debug the evil spell before [number] o’clock, or we’d be trapped in an infinite loop of [plural noun] forever. """

print('you are about to read a madlib, please observe the whole story and write the inputs accordingly!')
time.sleep(3)
print('press enter when you are ready!')
input()
print(mad_lib)

table = input('input an adjective!: ' ), input('school name: '), input('subject: '), input('noun: '), input('plural noun: '), input('body part: '), input('adjective: '), input('color: '), input('plural noun: '), input('animal: '), input('programming language: '), input('silly noun: '), input('electronic device: '), input('gross object: '), input('friend''s name: '), input('mythical name: '), input('creepy phase: '), input('number: '), input('plural noun: ')

print("\nHere’s your completed Mad Lib:\n")
print(mad_lib_custom.format(*table))
