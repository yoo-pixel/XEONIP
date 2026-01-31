import requests
import time

# GitHub API credentials
TOKEN = "YOUR_GITHUB_TOKEN_HERE"  # Replace with your token
OWNER = "yoo-pixel"
REPO = "XEONIP"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

print("🔍 Checking GitHub Pages status...\n")

# Check if repo is public
repo_url = f"https://api.github.com/repos/{OWNER}/{REPO}"
repo_response = requests.get(repo_url, headers=headers)
if repo_response.status_code == 200:
    repo_data = repo_response.json()
    is_private = repo_data.get('private', False)
    if is_private:
        print("⚠️  Repository is PRIVATE - GitHub Pages requires PUBLIC repo")
        print("Making repository public...")
        
        # Make repo public
        update_url = f"https://api.github.com/repos/{OWNER}/{REPO}"
        update_data = {"private": False}
        update_response = requests.patch(update_url, headers=headers, json=update_data)
        
        if update_response.status_code == 200:
            print("✅ Repository is now PUBLIC\n")
        else:
            print(f"Error making public: {update_response.status_code}\n")
    else:
        print("✅ Repository is PUBLIC\n")

# Check GitHub Pages status
pages_url = f"https://api.github.com/repos/{OWNER}/{REPO}/pages"
pages_response = requests.get(pages_url, headers=headers)

if pages_response.status_code == 200:
    pages_data = pages_response.json()
    status = pages_data.get('status', 'unknown')
    
    print(f"📊 GitHub Pages Status: {status}")
    print(f"🌐 URL: https://{OWNER}.github.io/{REPO}/")
    
    if status == "building":
        print("\n⏳ Site is still building... (typically takes 30-60 seconds)")
        print("Please wait a moment and try again.")
    elif status == "built":
        print("\n✅ Site built successfully!")
        print("The site should be live now.")
    elif status == "errored":
        print("\n❌ There was a build error")
        print(f"Details: {pages_data.get('error', {})}")
else:
    print(f"❌ Could not get Pages status: {pages_response.status_code}")
    print(f"Response: {pages_response.text}")

# Check for recent deployments
deployments_url = f"https://api.github.com/repos/{OWNER}/{REPO}/deployments"
deployments_response = requests.get(deployments_url, headers=headers)

if deployments_response.status_code == 200:
    deployments = deployments_response.json()
    if deployments:
        print("\n📋 Recent Deployments:")
        for deploy in deployments[:3]:
            print(f"  - Environment: {deploy.get('environment')}")
            print(f"    Created: {deploy.get('created_at')}")
            print(f"    Status: {deploy.get('status')}")
