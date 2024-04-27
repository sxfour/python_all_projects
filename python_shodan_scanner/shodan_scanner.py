import shodan

# Api key
key = 'Pe3YdGks3juloSfWPRy3RK0OSqXdY7Jt'
api = shodan.Shodan(key)

# country: страна, в формате RU, UK, US и т.д., например: nginx country:RU
# city: город, например: nginx city:«Moscow» country:RU
# os: операционная система, например: microsoft-iis os:«windows 2003»
# port: порт в формате 21, 80, 443 и тд, например: proftpd port:21
# hostname: позволяет искать с учетом домена, например: nginx hostname:.de

# Try and except block, need for print error (except) and combine api information (for, in)

# try:
#     # Set passphrase to search with api
#     print('-' * 29), print('   API SHODAN SCANNER V0.1'), print('-' * 29)
#     print('Commands: ')
#     set_search = input('Set passphrase: ')
#     results = api.search(set_search)
#     print('Results found: {}'.format(results['total']))
#     for result in results['matches']:
#         print('IP: {}'.format(result['ip_str']))
#         print(result['data'])
#         print('')
# except:
#     print('Error, wrong command')



# Search information a host
try:
        set_search_ip = input('Set host: ')
        host = api.host(set_search_ip)
        print("""
        IP: {}
        Organization: {}
        OS: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os','n/a')))
        for item in host['data']:
                print("""
                Port: {}
                Banner: {}
                """.format(item['port'], item['data']))
except ValueError:
        print()


# set_search_ip = input('Set host: ')
# host = api.host(set_search_ip)
# print("""
#   IP: {}
#   Organization: {}
#   OS: {}
# """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
# # All banners
# for item in host['data']:
#         print("""
#   Port: {}
#   Banner: {}
#         """.format(item['port'], item['data']))