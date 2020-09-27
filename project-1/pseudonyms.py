#! python3
'''
This module generates funny names at random based on the first and last names of
Terry Pratchett's Disc World characters
'''

import sys, random

print('Welcome to the Disc World "Sidekick Name Picker"\n')
print('A name Terry Pratchett would be proud of:\n\n')


first = ('Rince', 'Sam', 'Tiffany', 'Lord', 'Angua', 'Granny', 'Two', 'Nanny',
         'Sybil', 'Susan', 'Lily', 'Nobby', 'Magrat', 'Greebo', 'Eskarina',
         'Shawn', 'Moist von', 'Mustrum', 'Cohen', 'Conina', 'Carrot', 'Brutha',
         'Agnes', 'Cut-Me-Own-Throat', 'Cheery', 'Death', 'Fred', 'Ponder', 'Reacher',
         'Leonard', 'Adora', 'Reg', 'Great God', 'Offler', 'Ronald', 'Hex',
         'Sacharissa', 'Rob', 'Eric', 'William', 'Ahmad', 'Bloody Stupid',
         'Corporal', 'Daniel "One Drop"', 'Doctor', 'Doughnut', 'Drum', 'Ella',
         'Evadne', 'Findthee', 'Glenda', 'Hubert', 'Imp Y', 'Miss Iodine',
         'Jeremy', 'J.H.C', 'John', 'Juliet', 'Jonathan', 'Lieutenant', 'Liessa',
         'Lobsang', 'Lupine', 'Ly Tin', 'Marietta', 'Mightily', 'Nijel', 'Olaf',
         'Polly', 'Rosemary', 'Seldom', 'Sergeant-Major Jack', 'Stanley',
         'Rufus', 'Tolliver', 'Trevor', 'Victor', 'Wallace', 'Walter')

last = ('Wind', 'Vimes', 'Aching', 'Vetinari', 'Uberwald', 'Weatherwax', 'Flower',
        'Ogg', 'Helit', 'Nobbs', 'Smith', 'Lipwig', 'Ridcully', 'the Barbarian',
        'Ironfoundersson', 'Nitt', 'Dibbler', 'Littlebottom', 'of Rats',
        'Stibbons', 'Gilt', 'of Quirm', 'Dearheart', 'Om', 'Cripslock',
        'Anybody', 'de Worde', 'the Mad', 'Johnson', 'Strappi', 'Trooper',
        'Cruces', 'Jimmy', 'Billet', 'Saturday', 'Cake', 'Swing', 'Sugarbean',
        'Turvey', 'Celyn', 'Maccalariat', 'Clockson', 'Goatberger',
        '"Mossy" Lawn', 'Teatime', 'Stollop', 'Blouse', 'Dragonlady', 'Ludd',
        'Snapcase', 'Wonse', 'Wheedle', 'Cosmopolite', 'Garlick', 'Oats',
        'the Destroyer', 'Quimby', 'Perks', 'Palm', 'Drumknott', 'Jackrum', 'Howler',
        'Groat', 'Likely', 'Tugelbend', 'Sonky', 'Plinge')

while True:

    first_name = random.choice(first)

    last_name = random.choice(last)

    print('\n\n')
    print('{} {}'.format(first_name, last_name), file=sys.stderr)
    print('\n\n')

    try_again = input('\n\nTry again? (Type y/n)\n')

    if try_again.lower() == 'n':
        break

input('\nPress Enter to exit.\n')