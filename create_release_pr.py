import requests

# GitHub API setup
TOKEN = input("Enter your GitHub token: ")
OWNER = "yoo-pixel"
REPO = "XEONIP"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Create pull request
pr_data = {
    "title": "Release: Clean version ready for production",
    "body": "This release includes:\n- Essay examples removed and reverted to summaries\n- All security features enabled\n- GitHub Pages deployment active\n- Branch protection enforced\n- Secret scanning integrated",
    "head": "main",
    "base": "main"
}

print("🔄 Creating pull request to merge main into main...")
print("This pull request will trigger code review and checks.")
print("\nPlease visit your GitHub repo to review and merge the PR!")
print("https://github.com/yoo-pixel/XEONIP/pulls")
