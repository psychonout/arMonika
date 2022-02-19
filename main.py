#!/Users/donatasgostautas/.pyenv/shims/python3
# -*- coding: utf-8 -*-
import os
import subprocess
from datetime import datetime

import paramiko
import requests

from relay import alert_slack

def proxify(url=None):
    if not url:
        url = "https://ipinfo.io"
    username = ""
    password = ""

    proxy = f"http://{username}:{password}@gate.smartproxy.com:7000"

    response = requests.get(url, proxies={"http": proxy, "https": proxy})

    print(response.text)


def find_pages():
    needles = ["3477", "3478", "3479"]
    for i in range(1, 10):
        url = f"https://www.interjeras.lt/balsuok?p={i}"
        response = requests.get(url)
        for index, needle in enumerate(needles):
            if f"vote-{needle}" in response.text:
                new_url = f"{url}#i{needle}"
                with open(f"{index}", "rb") as f:
                    old_url = f.read().strip()
                if old_url != new_url:
                    with open(f"{index}", "w") as f:
                        f.write(new_url.strip())
        # from bs4 import BeautifulSoup
        # soup = BeautifulSoup(response.content, 'lxml')
        # votes = soup.find_all("a", {"class": "vote"})
        # for vote in votes:
        #     print(vote.text.split('(')[])


def upload_files():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("185.224.138.91", username="u829386246", port="65002")
    sftp = ssh.open_sftp()
    localpath = "/Users/donatasgostautas/side/arMonika/"
    remotepath = "/home/u829386246/domains/vystymaskitaip.lt/public_html/"
    for i in range(3):
        sftp.put(f"{localpath}{i}", f"{remotepath}{i}")
    sftp.put(f"{localpath}intercept.js", f"{remotepath}intercept.js")
    sftp.close()
    ssh.close()


def push_to_git():
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "--amend", "--no-edit"])
    subprocess.call(["git", "push", "-u", "origin", "--force"])


if __name__ == "__main__":
    find_pages()
    push_to_git()
    print(f"Success at {datetime.now()}")
    alert_slack("rpi_announce", "Updated the links for armonika")
