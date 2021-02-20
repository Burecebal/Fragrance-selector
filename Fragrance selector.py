import fragrance_info_from_net as info
import fragrance_randomizer as random

intro = True

while intro:
    IN = input('\nRandom = R, Add fragrance = A, See your fragrances and their ratings = P, Remove a fragrance = D, '
               'Quit = Q\n').lower()
    if IN == 'r':
        try:
            day = input('day/night\n').lower()
            season = input('winter/spring/summer/fall\n').lower()
            if season == 'winter' and day == 'day':
                q = random.winter_day()
                print(q, end='\n')
            elif season == 'winter' and day == 'night':
                q = random.winter_night()
                print(q, end='\n')
            elif season == 'spring' and day == 'day':
                q = random.spring_day()
                print(q, end='\n')
            elif season == 'spring' and day == 'night':
                q = random.spring_night()
                print(q, end='\n')
            elif season == 'summer' and day == 'day':
                q = random.summer_day()
                print(q, end='\n')
            elif season == 'summer' and day == 'night':
                q = random.summer_night()
                print(q, end='\n')
            elif season == 'fall' and day == 'day':
                q = random.fall_day()
                print(q, end='\n')
            elif season == 'fall' and day == 'night':
                q = random.fall_night()
                print(q, end='\n')
            resp = input('Would you like to send this result to your email? y/n\n').lower()
            if resp == 'y':
                some = input('Please insert your email:\n')
                info.send_email(q, some)
        except FileNotFoundError:
            print('No fragrances found.', end='\n')
    elif IN == 'a':
        x = True
        while x:
            some_input = input('Please insert the full name of the fragrance:\n')
            question = input('Would you like to add automatically (A) or manually (M) the percentages? NOTE: to '
                             'automatically add you need the newest version of Chrome installed.\n').lower()
            if question == 'a':
                try:
                    print('Getting the fragrance\'s info. Please wait...')
                    url = info.get_fragrance_site(some_input)
                    name, lst, votes = info.get_info(url)
                    night, day, fall, summer, spring, winter = info.seasons_ratings(lst)
                    nb_votes = votes.replace(',', '')
                    fragrance = info.Fragrance(name, winter, spring, summer, fall, day, night, nb_votes, url)
                    info.save_fragrance(fragrance)
                    print('\nAll done!')
                    x = False
                except:
                    print('Something happened, please try again.')
                    raise
            elif question == 'm':
                try:
                    print('Getting the fragrance url...')
                    url = info.get_fragrance_site(some_input)
                    print(f'Add the percentages in float numbers from this site {url}. Ex: If the winter chart is half '
                          f'full insert 50.00.')
                    name = some_input
                    winter = float(input('Winter percentage:\n'))
                    spring = float(input('Spring percentage:\n'))
                    summer = float(input('Summer percentage:\n'))
                    fall = float(input('Fall percentage:\n'))
                    day = float(input('Day percentage:\n'))
                    night = float(input('Night percentage:\n'))
                    votes = input('Total votes:\n')
                    nb_votes = votes.replace(',', '')
                    fragrance = info.Fragrance(name, winter, spring, summer, fall, day, night, nb_votes, url)
                    info.save_fragrance(fragrance)
                    print('\nAll done!')
                    x = False
                except ValueError:
                    print('The percentage needs to be a number.')
    elif IN == 'd':
        deleted = input('Please insert the complete and correct fragrance name (the name in the \'name\' section of '
                        'the fragrance):\n')
        info.delete_fragrance(deleted)
    elif IN == 'p':
        info.show_all()
    elif IN == 'kill':
        info.kill_all()
    else:
        intro = False
