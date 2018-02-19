import json
import requests

class client:

    url = 'https://fortnitetracker.com/profile/'

    def send_request(self, platform, username):
        # Collect the content from the site
        r = requests.get(self.url + platform + '/' + username)
        response = r.text

        # Get stats
        try:

            player_data = json.loads(self.find_between(response, 'var playerData = ', ';</script>'))
            #print(player_data)
            account_info = json.loads(self.find_between(response, 'var accountInfo = ', ';</script>'))
            #print(account_info)
            lifetime_stats = json.loads(self.find_between(response, 'var LifeTimeStats = ', ';</script>'))
            #print(lifetime_stats)

        except Exception:
            return ''

        # Return a list
        return [player_data, account_info, lifetime_stats]

    # Get the characters between the two strings
    def find_between(self, s, first, last):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

    