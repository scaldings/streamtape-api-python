# Streamtape API for Python
Streamtape is a service used for storing media with size up to 15GB. 

## Getting started
To use the API, you will need a Streamtape account and the API credentials.
You can get those at from https://streamtape.com/accpanel#accsettings
Here is the list of functions you can use with this API:

## Account
**account_info**: returns information about your account
```
{
  'status': 200,
  'msg': 'OK',
  'result':
     {
      'apiid': '7a97a5ab635e6cce48f6',
      'email': 'example@gmail.com',
      'signup_at': '2020-09-15 15:57:26'
     }
}
```

## Stream
**get_download_ticket**: returns a ticket which is needed to get a download link for a certain file



