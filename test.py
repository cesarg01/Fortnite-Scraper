from fortnite import get_squad_stats, build_string_for_squad_stats

print('Fortnite stat scraper. (Stats from fortnitetracker.com)')
username = input('Enter your username: ')
platform = 'psn'
squad_data = get_squad_stats(username, platform)
print(build_string_for_squad_stats(squad_data))