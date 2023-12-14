# # # # account_sid='AC02d5e5074e97f0fdf7e2e57320f8a197'

# # # # auth_token='8b5b4a2caadc10a0d63d47af8a612d08'

# # # # twilio_number='+12243026410'

# # # # my_phone_number='+91 7983896942'

# # # # from twilio.rest import Client


# # # # client = Client(account_sid,auth_token)

# # # # message=client.messages.create(
# # # #     body="  Motion is detected  ",
# # # #     from_=twilio_number,
# # # #     to=my_phone_number
# # # # )

# # # # print(message.body)

# # # from twilio.rest import Client

# # # account_sid = 'ACb2d8a9688aa71d047d1e49b8bff69f1e'
# # # auth_token = 'e614f64eb91b0996d5f1ae0c90692189'
# # # client = Client(account_sid, auth_token)

# # # message = client.messages.create(
# # #   from_='+12057723353',
# # #   to='+917983896942'
# # # )

# # # print(message.sid)

# # from twilio.rest import Client

# # account_sid = 'ACb2d8a9688aa71d047d1e49b8bff69f1e'
# # auth_token = '[AuthToken]'
# # client = Client(account_sid, auth_token)

# # message = client.messages.create(
# #   from='+12057723353',
# #   body='hello',
# #   to='+917983896942'
# # )

# # print(message.sid)

# from twilio.rest import Client

# account_sid = 'ACb2d8a9688aa71d047d1e49b8bff69f1e'
# auth_token = 'e614f64eb91b0996d5f1ae0c90692189'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from='+12057723353',
#   body='hello',
#   to='+917983896942'
# )

# print(message.sid)

account_sid='ACb2d8a9688aa71d047d1e49b8bff69f1e'

auth_token='e614f64eb91b0996d5f1ae0c90692189'

twilio_number='+12057723353'

my_phone_number='+91 7983896942'

from twilio.rest import Client


client = Client(account_sid,auth_token)

message=client.messages.create(
    body="  Motion is detected  ",
    from_=twilio_number,
    to=my_phone_number
)

print(message.body)