import numpy as np
from github import Github
import json
import paginate as pa

class GithubAccess:
    def __init__(self):
        self.g = Github("skv62138@eoopy.com", "DUDBcMpBJJV5YAf")
        self.repoName = ""

    def getRepo(self, repoName):
        data = self.g.get_repo(repoName)
        pr = data.get_pulls()
        print (data)
        print (pr)
        print(pr.totalCount)
        return 'lol'
    
    def getGroup(self, name):
        self.repoName = name
        data = self.g.get_organization(name)
        data = data.get_repos()
        repoList = []
        count=0
        for repo in data:
            if count < 3:
                repoList.append(self.extractRepoDetails(repo))
                count = count + 1
        return repoList
    
    def extractRepoDetails(self, repo):
        respons = {}
        respons['full_name'] = repo.full_name
        respons['name'] = repo.full_name.replace(self.repoName + '/', '')
        # pullrequests = repo.get_pull(2)
        # print(pullrequests)
        respons['pullrequests'] = [] 
        pullrequests =repo.get_pulls(state='open', base='master')
        for pr in pullrequests:
           respons['pullrequests'].append({'title': pr.title, 'user': pr.user.name, 'state':pr.state})
        return respons
    
    def searchGroup(self, name):
        data = self.g.get_organization(name)
        return 'lol'
    
