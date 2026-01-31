import requests
import json

# GitHub API credentials
TOKEN = "YOUR_GITHUB_TOKEN_HERE"  # Replace with your token
OWNER = "yoo-pixel"
REPO = "XEONIP"
BRANCH = "main"

# API endpoint
url = f"https://api.github.com/repos/{OWNER}/{REPO}/branches/{BRANCH}/protection"

# Headers with authentication
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Branch protection rules
data = {
    "required_status_checks": {
        "strict": True,
        "contexts": []
    },
    "enforce_admins": True,
    "required_pull_request_reviews": {
        "dismiss_stale_reviews": True,
        "require_code_owner_reviews": False,
        "required_approving_review_count": 1
    },
    "restrictions": None,
    "allow_force_pushes": False,
    "allow_deletions": False,
    "required_linear_history": False,
    "require_conversation_resolution": False
}

try:
    print("🔒 Setting up branch protection for main branch...")
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("✅ SUCCESS! Branch protection enabled on 'main' branch")
        print("\nProtection Settings:")
        print("  ✓ Require pull request reviews (1 approver)")
        print("  ✓ Require status checks to pass")
        print("  ✓ Dismiss stale pull request approvals")
        print("  ✓ Include administrators in restrictions")
        print("  ✓ Prevent force pushes")
        print("  ✓ Prevent deletions")
    elif response.status_code == 422:
        print("⚠️  Branch protection may already be configured")
        print(f"Response: {response.json()}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(f"Response: {response.json()}")
        
except Exception as e:
    print(f"❌ Error: {str(e)}")
