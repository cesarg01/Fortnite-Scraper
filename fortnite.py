from client import client

def get_squad_stats(usernames, platform):

    if not isinstance(usernames, list):
        usernames = [usernames]

    new_client = client()
    stat_friends = []

    try:

        for x in usernames:
            response = new_client.send_request(platform, x.lower())
            stat_friends.append(response[0]['p9'])
            
    except Exception:
        ''
    
    return stat_friends

def build_string_for_squad_stats(data):
    stats_friends = ''
    stats = []

    new_data = ''.join([str(i) for i in data])
    
    # Take the data off the brackets
    new_data = new_data.split('[')
    new_data = ''.join(new_data)
    new_data = new_data.split(']')

    # Convert data to string and split based on the parameters specified to easily loop throught the list
    new_data = ''.join(new_data)
    new_data = new_data.split('}, {')
    #print(new_data[0])

    for value in new_data:
        start = 'displayValue\': \''
        end = '\''
        stats.append((value.split(start))[1].split(end)[0])
    
        #stats_friends += '*'+x+'*\n'
    stats_friends += 'Played time: '+ stats[13] + '\n'
    stats_friends += 'Top 1: '+ stats[2] +'\n'
    stats_friends += 'Top 3: '+ stats[3] +'\n'
    stats_friends += 'Top 5: '+ stats[4] +'\n'
    stats_friends += 'Top 10: '+ stats[6] +'\n'
    stats_friends += 'Win Ratio: '+ stats[10] +'\n'
    stats_friends += 'Kills: '+stats[12] +'\n'
    stats_friends += 'Kills/Match: '+stats[15] + '\n\n'
    
    return stats_friends