# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please email security concerns to the repository maintainer rather than using the public issue tracker.

**Please do not publicly disclose the vulnerability until it has been addressed.**

## Security Features

This repository implements the following security measures:

### Frontend Security
- **Content Security Policy (CSP)**: All HTML pages include a strict CSP meta tag to prevent XSS attacks
- **Referrer Policy**: All pages include `no-referrer` policy to protect user privacy
- **External Resources**: All external resources (images, libraries) are loaded from trusted sources (Unsplash, CDN)
- **No Secrets**: Repository contains no API keys, credentials, or sensitive data

### Git Security
- **Branch Protection**: Main branch is protected with the following rules:
  - Require pull request reviews before merging
  - Require status checks to pass before merging
  - Dismiss stale pull request approvals
  - Include administrators in restrictions

### GitHub Security
- **Dependabot**: Automated dependency scanning enabled (if applicable)
- **Secret Scanning**: GitHub's built-in secret scanning is enabled
- **Vulnerability Alerts**: Automatic vulnerability detection and alerts enabled

## Deployment Security

- **GitHub Pages**: Static site deployed from the `main` branch
- **HTTPS**: GitHub Pages enforces HTTPS for all connections
- **Build Process**: No server-side code or database - reduces attack surface

## Best Practices for Contributors

When contributing to this repository:
1. Never commit secrets, API keys, or credentials
2. Don't include sensitive user data
3. Follow the existing code style and security patterns
4. Run local security checks before submitting PRs
5. Review dependency updates for security vulnerabilities

## Version Information

- **Last Updated**: January 2026
- **Security Review Status**: Current

## Third-Party Dependencies

This static site uses minimal external dependencies:
- **Unsplash API**: For free stock images (read-only, no authentication required)
- **Standard HTML/CSS/JavaScript**: No npm dependencies for production

## Contact

For security concerns, please contact the repository maintainer privately.
