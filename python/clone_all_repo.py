# !/usr/bin/python3

import requests, os, subprocess

# page: 1-5
settings = (('page', '0'), ('per_page', '100'), ('type', 'all'))
personal_user = 'user'  # personal account
personal_token = 'token'  # generate from github
directory = '/Users/admin/github'
git_url = 'https://api.github.com/orgs/MyJetWallet/repos'


def get_all_repos(user, token, params):
    res = requests.get(git_url, params=params, auth=(user, token))
    res.headers.get('link', None)
    repos = res.json()
    while 'next' in res.links.keys():
        res = requests.get(res.links['next']['url'], headers={"Authorization": token})
        repos.extend(res.json())
    return repos


os.chdir(directory)
for ssh_url in get_all_repos(personal_user, personal_token, settings):
    try:
        subprocess.run('git clone %s' % ssh_url['ssh_url'], shell=True)
    except:
        continue

