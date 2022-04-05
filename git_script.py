from github import Github


g = Github("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")
user = g.get_user()
print(user)
repo = user.create_repo("test_repo")
print(repo)
