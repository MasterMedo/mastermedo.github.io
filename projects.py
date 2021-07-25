import json
import requests

from github import Github

user = "MasterMedo"
max_repos = 6
token = "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"
headers = {"Authorization": f"bearer {token}"}

pinned_repos_graphql = f"""{{
"query": "{{
    user(login: \\"{user}\\") {{
        pinnedItems(first: {max_repos}, types: REPOSITORY) {{
            nodes {{
                ... on Repository {{
                    name
                }}
            }}
        }}
    }}
}}"
"""

post_header = """---
category: projects
github: https://github.com/{user}/{repo}
---
"""

response = requests.post(
    "https://api.github.com/graphql",
    headers=headers,
    data="".join(line.strip() for line in pinned_repos_graphql.split("\n")),
)
repos = json.loads(response.content)["data"]["user"]["pinnedItems"]["nodes"]

g = Github(token)

for repo in repos:
    repo = g.get_user(user).get_repo(repo["name"])
    with open(f"_posts/{repo.created_at.date()}-{repo.name}.md", "w") as f:
        print(post_header.format_map({"user": user, "repo": repo}), file=f)
        print(repo.get_readme().decoded_content.decode("UTF-8"), file=f)
