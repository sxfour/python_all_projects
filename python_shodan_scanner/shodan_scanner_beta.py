import shodan

# Api key Shodan.
key = 'WBcYpPr9OoEcXQX0usLSiDSBXpBEg1M5'
api = shodan.Shodan(key)
# Header variables.
b_design = '=' * 33
s_design = '-' * 19


# First function on search api shodan block: try, except (because, need two choices).
def api_func():
    try:
        print(b_design + '\n      1. API Shodan scanner\n' + b_design)
        set_search = input('Set passphrase: ')
        results = api.search(set_search)
        print('Results found: {}'.format(results['total']))
        # Loop through the elements of structures
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    # Condition to be executed on error or input of a different value
    except:
        print('Error, wrong command, check Shodan commands!')


# Last function, similar to the first one, there is a format and the use of triple quotes.
def host_func():
    try:
        print(b_design + '\n      2. IPr Shodan scanner\n' + b_design)
        set_search_ip = input('Set host: ')
        host = api.host(set_search_ip)
        print("""
            IP: {}
            Organization: {}
            OS: {}
            """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        for item in host['data']:
            print("""
                    Port: {}
                    Banner: {}
                    """.format(item['port'], item['data']))
    # Condition to be executed on error or input of a different value
    except:
        print('\nWrong passphrase!')


print(b_design + '\n   Shodan scanner service v0.1\n'
      + b_design, '\n1. API scan\n2. Host scan\n3. CVE exploit scan')

# Basic selection tool or branch,functions are executed if they are equal to the value of the variable
user_choice = int(input('\nSet mode: '))
if user_choice == 1:
    api_func()
elif user_choice == 2:
    host_func()
elif user_choice == 4:
    print('Egor Levashov, 31.08.2022, v0.1')
else:
    print('Please set valid number!')
