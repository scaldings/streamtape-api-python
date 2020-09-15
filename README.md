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
  "status": 200,
  "msg": "OK",
  "result": {
      "apiid": "<your api key>",
      "email": "user@gmail.com",
      "signup_at": "2019-12-31 23:59:59",
  }
}
```

## Stream
**get_download_ticket**: returns a ticket which is needed to get a download link for a certain file
```
{
  "status": 200,
  "msg": "OK",
  "result": {
      "ticket": "wg8ad12d3QiJRXG~~1585532987430~n~~0~q75Z2aJg-TYfQgxz8",
      "wait_time": 10,
      "valid_until": "2019-12-31 23:59:59"
  }
}
```

**get_download_link**: returns a download link for a file
```
{
  "status": 200,
  "msg": "OK",
  "result": {
    "name": "Vlog1220-Sidney.mp4",
    "size": 12345,
    "url": "https://tapecontent.net/Vlog1220-Sidney.mp4",
  }
}
```

**check_file**: returns information about a file
```
{
  "status": 200,
  "msg": "OK",
  "result": {
      "wg8ad12d3QiJRXG3": {
          "id": "wg8ad12d3QiJRXG3",
          "name": "MyMinecraftLetsPlay.mp4",
          "size": 1234,
          "type": "video/mp4",
          "converted": true,
          "status": 200
      },
      "ag8ad12d3QiJRXG4": {
          "id": "ag8ad12d3QiJRXG5",
          "name": "OutfitOfTheDay21.mp4",
          "size": 12346,
          "type": "video/mp4",
          "converted": true,
          "status": 200
      },
      "bg8ad12d3QiJRXG9": {
          "id": "bg8ad12d3QiJRXG9",
          "name": "Travel with Me - Episode 128",
          "size": 1234567,
          "type": "video/mp4",
          "converted": true,
          "status": 200
      },
      "yg8ad12d3QiJRXG1": {
          "id": "yg8ad12d3QiJRXG1",
          "name": "Reaction Video",
          "size": 12345,
          "type": "video/mp4",
          "converted": true,
          "status": 200
      },
   }
}
```

## Upload
**upload**: uploads a file from your computer

## Remote upload
**add_remote_upload**: adds a remote upload from a URL
```
{
  "status": 200,
  "msg": "OK",
  "result": {
    "id": "rbAarvRPXdYbaxY",
    "folderid": "LnvnE51P5gc"
  }
}
```

**remove_remote_upload**: removes a remote upload when given upload ID (use 'all' instead of the ID to remove all the uploads)
```
{
  "status": 200,
  "msg": "OK",
  "result": true
}
```

**check_remote_upload_status**: returns the status of a remote upload when given upload ID
```
{
  "status": 200,
  "msg": "OK",
  "result": {
    "LnvnE51P5gc": {
        "id": "LnvnE51P5gc",
        "remoteurl": "https://vid.me/myvideo123",
        "status": "new",
        "bytes_loaded": null,
        "bytes_total": null,
        "folderid": "LnvnE51P5gc",
        "added": "2019-12-31 23:59:59",
        "last_update": "2019-12-31 23:59:59",
        "extid": false,
        "url": false
    },
  }
}
```

## File / folder management
**folder_content**: returns the content of your root folder
**subfolder_content**: returns the content of a folder when given folder ID
```
{
  "status": 200,
  "msg": "OK",
  "result": {
    "folders": [
      {
        "id": "B-qlJkdHFeo",
        "name": "Subfolder"
      }
    ],
    "files": [
    {
        "name": "MyMinecraftLetsPlay.mp4",
	      "size": 7040842,
	      "link": "https://streamtape.com/v/rbAarvRPXdYbaxY/MyMinecraftLetsPlay.mp4",
	      "created_at": 1585532987430,
	      "downloads": 0,
	      "linkid": "rbAarvRPXdYbaxY",
	      "convert": "converted"
     }
    ]
  }
}
```
