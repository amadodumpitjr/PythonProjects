from github import Github

# First create a Github instance:

# using username and password
#guser = "amadodumpitjr"
#gpass = "AmAd0@$25365"
#g = Github(guser,gpass)

# or using an access token
g = Github("ba55212ebb142c7db85c62ba513fe19b3f337daa")

# Github Enterprise with custom hostname
#g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
    #print(g.get_repo("amadodumpitjr/"+repo.name).name)
    repo1 = g.get_repo("amadodumpitjr/" + repo.name)
    contents = repo1.get_contents("")
    for content_file in contents:
        print(content_file.name)
    # for repo1 in g.get_repo("amadodumpitjr/PythonDev"):
    #     print(repo1)
    #     contents = repo1.get_contents("")
    #     for content_file in contents:
    #         print(content_file)

# REPOS = [ _ for _ in g.get_user().get_repos()]
# print(REPOS)
# repo = g.get_repo("amadodumpitjr/PythonDev")
# contents = repo.get_contents("")
# for content_file in contents:
#     print(content_file)