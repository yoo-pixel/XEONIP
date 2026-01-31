import requests
import json

# GitHub API credentials
TOKEN = "YOUR_GITHUB_TOKEN_HERE"  # Replace with your token
OWNER = "yoo-pixel"
REPO = "XEONIP"

# API endpoint for enabling GitHub Pages
url = f"https://api.github.com/repos/{OWNER}/{REPO}/pages"

# Headers with authentication
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# GitHub Pages configuration - deploy from main branch, root directory
data = {
    "source": {
        "branch": "main",
        "path": "/"
    }
}

try:
    print("🚀 Deploying to GitHub Pages...")
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("✅ SUCCESS! GitHub Pages is now LIVE!")
        result = response.json()
        print(f"\n📍 Your site is live at: https://{result['cname'] if 'cname' in result else OWNER}.github.io/{REPO}/")
        print("\n🎉 Deployment Details:")
        print(f"  ✓ Branch: main")
        print(f"  ✓ Path: root directory (/)")
        print(f"  ✓ Status: Published")
    elif response.status_code == 409:
        print("ℹ️ GitHub Pages already enabled. Checking status...")
        # Try to get current pages config
        get_response = requests.get(url, headers=headers)
        if get_response.status_code == 200:
            result = get_response.json()
            print(f"✅ GitHub Pages is LIVE!")
            print(f"📍 Your site: https://{OWNER}.github.io/{REPO}/")
            print(f"\n🎉 Current Configuration:")
            print(f"  ✓ Status: {result.get('status', 'unknown')}")
            print(f"  ✓ Branch: {result.get('source', {}).get('branch', 'main')}")
            print(f"  ✓ URL: {result.get('html_url', 'N/A')}")
    elif response.status_code == 422:
        print("⚠️  Configuration issue. Retrying with POST...")
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in [201, 204]:
            print("✅ GitHub Pages deployed successfully!")
            print(f"📍 Your site: https://{OWNER}.github.io/{REPO}/")
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Response: {response.json()}")
        
except Exception as e:
    print(f"❌ Error: {str(e)}")
