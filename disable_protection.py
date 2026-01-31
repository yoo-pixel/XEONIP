import requests

TOKEN = "YOUR_GITHUB_TOKEN_HERE"  # Replace with your token
OWNER = "yoo-pixel"
REPO = "XEONIP"
BRANCH = "main"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

protection_url = f"https://api.github.com/repos/{OWNER}/{REPO}/branches/{BRANCH}/protection"

print("Checking branch protection status...")
response = requests.get(protection_url, headers=headers)
print(f"Status: {response.status_code}")

if response.status_code == 200:
    print("✅ Protection is still active")
    print("\nDisabling protection...")
    del_response = requests.delete(protection_url, headers=headers)
    print(f"Delete response: {del_response.status_code}")
    if del_response.status_code == 204:
        print("✅ Protection disabled!")
    else:
        print(f"Response: {del_response.text}")
else:
    print(f"Error: {response.text}")
