from django.shortcuts import render
import os
import requests
from collections import Counter
from django.core.cache import cache

def index(request):
    data = cache.get('github_data')
    if data:
        total_repos, top_languages, pr_count, total_commits = data
    else:
        token = os.environ.get('Github_token')
        headers = {'Authorization': 'Token ' + token}
        # Get total number of repositories
        repos_url = 'https://api.github.com/user/repos?type=all&per_page=100&page=1'
        repos_res = requests.get(repos_url, headers=headers)
        repos = repos_res.json()
        total_repos = len(repos)
        # Count top two most used languages in repos
        languages = []
        for repo in repos:
            languages.append(repo['language'])
        language_count = Counter(languages)
        top_languages = language_count.most_common(2)
        # Get total count of PR
        pr_url = 'https://api.github.com/search/issues?q=is:pr+author:pritiyadav888'
        pr_res = requests.get(pr_url, headers=headers)
        pr_count = len(pr_res.json()['items'])
        # Get total number of commits
        total_commits = 0
        for repo in repos:
            commits_url = f'https://api.github.com/repos/pritiyadav888/{repo["name"]}/commits'
            commits_res = requests.get(commits_url, headers=headers)
            total_commits += len(commits_res.json())
        cache.set('github_data', (total_repos, top_languages, pr_count, total_commits), 86400)
    return render(request, 'index.html', {'total_repos': total_repos, 'top_languages': top_languages, 'pr_count': pr_count, 'total_commits': total_commits})

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def blog_single(request):
    return render(request, 'blog-single.html')