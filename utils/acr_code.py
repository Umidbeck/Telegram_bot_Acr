"""
This is a demo program which implements ACRCloud Identify Protocol V1 with the third party library "requests".
We recomment you implement your own app with "requests" too.
You can install this python library by:
1) sudo easy_install requests
2) sudo pip install requests
"""

import base64
import hashlib
import hmac
import json
import os
import shutil
import sys
import time

import requests


async def acr_cloud(dow_name):
    try:
        '''
        Replace "###...###" below with your project's host, access_key and access_secret.
        '''
        access_key = "your_key"
        access_secret = "your_secret"
        requrl = "http://identify-eu-west-1.acrcloud.com/v1/identify"

        http_method = "POST"
        http_uri = "/v1/identify"
        # default is "fingerprint", it's for recognizing fingerprint,
        # if you want to identify audio, please change data_type="audio"
        data_type = "audio"
        signature_version = "1"
        timestamp = time.time()

        string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(
            timestamp)

        sign = base64.b64encode(hmac.new(access_secret.encode('ascii'), string_to_sign.encode('ascii'),
                                         digestmod=hashlib.sha1).digest()).decode('ascii')

        # suported file formats: mp3,wav,wma,amr,ogg, ape,acc,spx,m4a,mp4,FLAC, etc
        # File size: < 1M , You'de better cut large file to small file, within 15 seconds data size is better
        f = open(sys.argv[0], "rb")
        sample_bytes = os.path.getsize(sys.argv[0])
        path_audio = f"downloads/{dow_name}/music"
        if os.path.isdir(path_audio):
            path = f"downloads/{dow_name}/music"
        else:
            path = f"downloads/{dow_name}/videos"

        for filename in os.listdir(path):
            filename = filename
        files = [
            ('sample', ('music_video.mp4', open(f'{path}/{filename}', 'rb'), 'audio/mpeg'))
        ]
        data = {'access_key': access_key,
                'sample_bytes': sample_bytes,
                'timestamp': str(timestamp),
                'signature': sign,
                'data_type': data_type,
                "signature_version": signature_version}

        r = requests.post(requrl, files=files, data=data)
        r.encoding = "utf-8"
        try:
            if r.json()['metadata']['music'][0]['external_metadata']['spotify']:
                spotify_music_1 = r.json()['metadata']['music'][0]['external_metadata']['spotify']['track']['name']
                spotify_music_2 = r.json()['metadata']['music'][0]['external_metadata']['spotify']['artists'][0]['name']
                music_name = f'{spotify_music_1}+{spotify_music_2}'
        except:
            if r.json()['metadata']['music'][0]['external_metadata']['deezer']:
                deezer_music_1 = r.json()['metadata']['music'][0]['external_metadata']['deezer']['track']['name']
                deezer_music_2 = r.json()['metadata']['music'][0]['external_metadata']['deezer']['artists'][0]['name']
                music_name = f'{deezer_music_1}+{deezer_music_2}'
        for filename1 in os.listdir(path):
            if filename1 == filename:
                fupload_folder_2 = f'downloads/{dow_name}'
                if os.path.isdir(fupload_folder_2):
                    shutil.rmtree(fupload_folder_2)
        return music_name
    except:
        for filename1 in os.listdir(path):
            if filename1 == filename:
                fupload_folder_2 = f'downloads/{dow_name}'
                if os.path.isdir(fupload_folder_2):
                    shutil.rmtree(fupload_folder_2)
