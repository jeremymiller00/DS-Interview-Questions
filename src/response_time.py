'''
You are given a dataset with information around messages sent between users in a P2P messaging application. Below is the dataset's schema:

Column Name	Data Type	Description
date	    string	    date of the message sent/received, format is 'YYYY-mm-dd'
timestamp	integer	    timestamp of the message sent/received, epoch seconds
sender_id	integer	    id of the message sender
receiver_id	integer	    id of the message receiver

Given this, write code to find the fraction of messages that are sent between the same sender and receiver within five minutes (e.g. the fraction of messages that receive a response within 5 minutes).

Solution will be written in Python for premium users.'''

time_delta = 300 # 5 minutes in seconds

# sort by time stamp
# search the 5 minute window

data = pd.load_the_data...
total_mssg = data.shape[0]
sorted_data = data.sort('timestamp', ascending=True)

quick_reply = 0
for msg in sorted_data.iterrows():
    ts = msg['timestamp']
    if sorted_data[ (sorted_data['timestamp'] < ts) & (sorted_data['sender_id'] == msg['receiver_id']) & (sorted_data['receiver_id'] == msg['sender_id']) ].shape[0] > 0:
        quick_reply += 1

print("Proportion of messages with quick response: {}".format( quick_reply / total_mssg))

