import requests
import hashlib
import os 
import subprocess
def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/vlc-3.0.18-win64.7z.sha256'
    resp_msg = requests.get(file_url)
    if resp_msg.status_code == requests.code.ok:
        file_contents = resp_msg.text 
        hash = file_contents.split()
    return 

def download_installer():
    
    installer_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64/'
    resp_msg = requests.get(installer_url)
    if resp_msg.status_code == requests.code.ok:
        file_content = resp_msg.content
    
    return 
def installer_ok(installer_data, expected_sha256):
    
    installer_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64'
    resp_msg = requests.get(installer_url)
    if resp_msg.status_code == requests.code.ok:
        file_content = resp_msg.content 
        image_hash = hashlib.sha256(file_content).hexdigest()
        print(image_hash)
    return

def save_installer(installer_data):
    
    installer_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/win64'
    resp_msg = requests.get(installer_url)
    if resp_msg.status_code == requests.code.ok:
        file_content = resp_msg.content 
    with open(r'C:\temp\vlc\3.0.18', 'wb') as file:
        file.write(file_content)
    return

def run_installer(installer_path):
   
    installer_path = r'C:\temp\vlc-3.0.18-win64.exe'
    subprocess.run([installer_path, '/L=1033', '/S'])
    
    return
    
def delete_installer(installer_path):
    
    installer_path = r'C:\temp\vlc-3.0.18-win64.exe'
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()