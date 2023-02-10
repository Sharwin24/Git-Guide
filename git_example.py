import git

repo = git.Repo("https://github.com/Sharwin24/Git-Guide")

for branch in repo.branches:
    print(branch)