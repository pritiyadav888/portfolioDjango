from django.shortcuts import render
# import configparser
import requests
from collections import Counter
from django.core.cache import cache
# token = os.environ.get('Github_token') 
import os 
def index(request):
    data = cache.get('github_data')
    if data:
        total_repos, pr_count = data
    else:
        token = os.environ.get('Github_token') 
        # headers = {'Authorization': 'Token ' + token}
        # Get total number of repositories
        # config = configparser.ConfigParser()
        # config.read('config.ini')
        # token = config['Github']['token']
        headers = {'Authorization': 'Token ' + token}
        # Get total number of repositories
        repos_url = 'https://api.github.com/user/repos?type=all&per_page=100&page=1'
        repos_res = requests.get(repos_url, headers=headers)
        repos = repos_res.json()
        total_repos = len(repos)
        # Get total count of PR
        pr_url = 'https://api.github.com/search/issues?q=is:pr+author:pritiyadav888'
        pr_res = requests.get(pr_url, headers=headers)
        pr_json = pr_res.json()
        if "items" in pr_json:
            pr_count = len(pr_json["items"])
        else:
            pr_count = 0
        # Get total number of commit
        cache.set('github_data', (total_repos, pr_count), 86400)
        print("total_repos'pr_count'commits_count", total_repos,pr_count)
    return render(request, 'index.html', {'total_repos': total_repos, 'pr_count': pr_count})
    
def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def blog_single(request):
    return render(request, 'blog-single.html')