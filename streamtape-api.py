import requests
import hashlib


# Account
def account_info(login, key):
    url = f'https://api.streamtape.com/account/info?login={login}&key={key}'
    data = requests.get(url).json()
    return data


# Stream
def get_download_ticket(file_id, login, key):
    url = f'https://api.streamtape.com/file/dlticket?file={file_id}&login={login}&key={key}'
    data = requests.get(url).json()
    return data


def get_download_link(file_id, download_ticket):
    url = f'https://api.streamtape.com/file/dl?file={file_id}&ticket={download_ticket}'
    data = requests.get(url).json()
    return data


def check_file(file_id, login, key):
    url = f'https://api.streamtape.com/file/info?file={file_id}&login={login}&key={key}'
    data = requests.get(url).json()
    return data


# Upload
def upload(folder_id, login, key, file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        sha256 = sha256_hash.hexdigest()
    url = f'https://api.streamtape.com/file/ul?login={login}&key={key}&folder={folder_id}&sha256={sha256}'
    data = requests.get(url).json()
    upload_url = data['result']['url']
    file = {'file': open(file_path, 'rb')}
    upload_request = requests.post(upload_url, files=file)
    upload_response = upload_request.json()
    return upload_response


# Remote upload
def add_remote_upload(login, key, file_url, folder_id, name):
    url = f'https://api.streamtape.com/remotedl/add?login={login}' \
          f'&key={key}&url={file_url}&folder={folder_id}amp;name={name}'
    data = requests.get(url).json()
    return data


def remove_remote_upload(login, key, upload_id):
    # To remove all the uploads, enter 'all' instead of an actual upload ID
    url = f'https://api.streamtape.com/remotedl/remove?login={login}&key={key}&id={upload_id}'
    data = requests.get(url).json()
    return data


def check_remote_upload_status(login, key, upload_id):
    url = f'https://api.streamtape.com/remotedl/status?login={login}&key={key}&id={upload_id}'
    data = requests.get(url).json()
    return data


# File / folder management
def folder_contnent(login, key):
    url = f'https://api.streamtape.com/file/listfolder?login={login}&key={key}'
    data = requests.get(url).json()
    return data


def subfolder_conent(login, key, folder_id):
    url = f'https://api.streamtape.com/file/listfolder?login={login}&key={key}&loder={folder_id}'
    data = requests.get(url).json()
    return data


def create_folder(login, key, folder_name, parent_folder_id):
    url = f'https://api.streamtape.com/file/createfolder?login={login}&key={key}&name={folder_name}' \
          f'&pid={parent_folder_id}'
    data = requests.get(url).json()
    return data


def rename_folder(login, key, folder_id, new_name):
    url = f'https://api.streamtape.com/file/renamefolder?login={login}&key={key}&folder={folder_id}&name={new_name}'
    data = requests.get(url).json()
    return data


def delete_folder(login, key, folder_id):
    url = f'https://api.streamtape.com/file/deletefolder?login={login}&key={key}&folder={folder_id}'
    data = requests.get(url).json()
    return data


def rename_file(login, key, file_id, new_name):
    url = f'https://api.streamtape.com/file/rename?login={login}&key={key}&file={file_id}&name={new_name}'
    data = requests.get(url).json()
    return data


def move_file(login, key, file_id, destination_folder_id):
    url = f'https://api.streamtape.com/file/rename?login={login}&key={key}&file={file_id}' \
          f'&folder={destination_folder_id}'
    data = requests.get(url).json()
    return data


def delete_file(login, key, file_id):
    url = f'https://api.streamtape.com/file/delete?login={login}&key={key}&file={file_id}'
    data = requests.get(url).json()
    return data


# Converting files
def running_conversions(login, key):
    url = f'https://api.streamtape.com/file/runningconverts?login={login}&key={key}'
    data = requests.get(url).json()
    return data


def failed_conversions(login, key):
    url = f'https://api.streamtape.com/file/failedconverts?login={login}&key={key}'
    data = requests.get(url).json()
    return data


def get_thumbnail(login, key, file_id):
    url = f'https://api.streamtape.com/file/getsplash?login={login}&key={key}&file={file_id}'
    data = requests.get(url).json()
    return data