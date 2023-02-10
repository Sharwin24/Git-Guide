import git

repo = git.Repo("path/to/repository")

for branch in repo.branches:
    print(branch)