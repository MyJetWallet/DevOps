# !/usr/bin/python3

import requests, os, subprocess

settings = (('page', '0'), ('per_page', '100'), ('type', 'all'))
personal_user = 'user'  # personal account
personal_token = 'token'  # generate from github


def get_all_repos(user, token, params):
    res = requests.get('https://api.github.com/orgs/MyJetWallet/repos', params=params, auth=(user, token))
    res.headers.get('link', None)
    repos = res.json()
    while 'next' in res.links.keys():
        res = requests.get(res.links['next']['url'], headers={"Authorization": token})
        repos.extend(res.json())
    return repos


os.chdir('/Users/admin/github')
for ssh_url in get_all_repos(personal_user, personal_token, settings):
    try:
        subprocess.run('git clone %s' % ssh_url['ssh_url'], shell=True)
    except:
        continue

