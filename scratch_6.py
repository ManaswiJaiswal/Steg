from collections import defaultdict
dictionary= defaultdict(list)
"""defining user name age and rating"""

dictionary['user1'].append('Anna')
dictionary['user1'].append('22')
dictionary['user1'].append('.6')
dictionary['user2'].append('Becky')
dictionary['user2'].append('32')
dictionary['user2'].append('.8')
dictionary['user3'].append('Will')
dictionary['user3'].append('28')
dictionary['user3'].append('.7')
dictionary['user4'].append('Dan')
dictionary['user4'].append('37')
dictionary['user4'].append('.9')
dictionary['user5'].append('Sarah')
dictionary['user5'].append('36')
dictionary['user5'].append('.9')

from TextmagicRestClient import TextmagicRestClient

username = "your_textmagic_username"
token = "your_apiv2_key"
client = TextmagicRestClient(username, token)

message = client.messages.create(name="9990001001", text="Hello")
