
import git 

repo_url = "https://github.com/tarikgit1/test.git"

clone_dir  = "D:/python development/repo2"

output = git.Repo.clone_from(repo_url,clone_dir)

print(output)


#provide the tokem


# # g = Github(token)

# # user = g.get_user()

# # repo_name = "my_new_Python"
# # repo = user.create_repo(repo_name)
# # print(f"Repository {repo_name} created successfully")

# subprocess.run(["git","clone",repo_url,clone_url])

