from github import Github


def create(dirname):
    g = Github("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")
    for repo in g.get_user().get_repos():
        print(repo.name)
    u = g.get_user()
    #repo = u.create_repo("dirname")
