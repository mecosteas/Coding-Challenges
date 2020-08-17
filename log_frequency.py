"""
You are given a stream of logging statements for a server as a list. Your product manager wants to know what categories
of error are the most common, as well as what errors in the most common categories are the most common.

Here are a few log lines, each is a string structured similarly to this:
[
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 Login Successful',
'[INFO] 200 User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]

Return a dictionary with logging statistics, that is formatted like so ( don't worry about spacing or formatting, only
 the data matters )

{
	'WARNING': {
		'403': {
			'Forbidden': {
				'No token in request parameters': 1
			}
		}
	},
	'ERROR': {
		'500': {
			'Server Error': {
				'int is not subscriptable': 2
			}
		}
	},
	'INFO': {
		'200': {
			'OK': {
				'Login Successful': 1,
				'User sent a message': 1
			}
		}
	}
}

When printed it will more likely look like this:

{'WARNING': {'403': {'Forbidden': {'No token in request parameters': 1}}}, 'ERROR': {'500': {'Server Error': {'int is
not subscriptable': 2}}}, 'INFO': {'200': {'OK': {'Login Successful': 1, 'User sent a message': 1}}}}
"""


def log_stats(logs):
    logs_dict = {}
    for log in logs:
        bracket_index = 0
        colon_index = 0
        # assuming there will be no other ] or : in the string
        for i in range(len(log)):
            if log[i] == ']':
                bracket_index = i
            elif log[i] == ':':
                colon_index = i

        label = log[1: bracket_index]
        three_digits = log[bracket_index + 2: bracket_index + 5]
        desc_label = log[bracket_index + 6: colon_index]
        desc = log[colon_index + 2:]

        # if the label is not on there, then nothing else will be on there, so add all of it
        if logs_dict.get(label) == None:
            logs_dict[label] = {three_digits: {desc_label: {desc: 1}}}
        # if it is there, then check if the three digits are already in there, if it's not, then add the rest
        elif logs_dict[label].get(three_digits) == None:
            logs_dict[label][three_digits] = {desc_label: {desc: 1}}
        # if the three digits are there, then check if the desc label is there, if it isn't then add the rest
        elif logs_dict[label][three_digits].get(desc_label) == None:
            logs_dict[label][three_digits][desc_label] = {desc: 1}
        # if the desc label is there, then see if the description is there, if it is not, then add the rest init with 1
        elif logs_dict[label][three_digits][desc_label].get(desc) == None:
            logs_dict[label][three_digits][desc_label][desc] = 1
        # if it is, then increase the desc + 1
        else:
            logs_dict[label][three_digits][desc_label][desc] += 1
    return logs_dict


test_data = [
    '[WARNING] 403 Forbidden: No token in request parameters',
    '[ERROR] 500 Server Error: int is not subscriptable',
    '[INFO] 200 OK: Login Successful',
    '[INFO] 200 OK: User sent a message',
    '[ERROR] 500 Server Error: int is not subscriptable'
]

print(log_stats(test_data))