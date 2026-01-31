# Contributing Guidelines

Thank you for your interest in contributing to this project!

## How to Contribute

1. **Fork the repository** on GitHub
2. **Create a new branch** for your changes: `git checkout -b feature/your-feature-name`
3. **Make your changes** following the code style below
4. **Test your changes** locally
5. **Commit with clear messages**: `git commit -m "Add feature: description"`
6. **Push to your fork**: `git push origin feature/your-feature-name`
7. **Create a Pull Request** with a clear title and description

## Code Style

- **HTML**: Use semantic HTML5 tags, proper indentation (2 spaces)
- **CSS**: Follow BEM naming convention, group related properties
- **JavaScript**: Use clear variable names, add comments for complex logic
- **Security**: Always include CSP and referrer policy meta tags in new HTML files

## Security Guidelines

- ❌ Never commit secrets, API keys, or credentials
- ❌ Don't include hardcoded sensitive data
- ❌ Don't add external scripts without security review
- ✅ Always test CSP compliance
- ✅ Review dependencies for security vulnerabilities
- ✅ Include proper security headers

## Pull Request Process

1. Ensure all security checks pass
2. Include a clear description of changes
3. Reference any related issues
4. Wait for code review approval
5. Ensure CI/CD pipeline passes before merge

## Reporting Issues

- Use GitHub Issues for bug reports
- Provide clear reproduction steps
- Include browser/environment information
- For security issues, contact maintainer privately (see SECURITY.md)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Respect intellectual property
- Follow all contribution guidelines

## Questions?

Feel free to open a discussion or issue for clarification.

Thank you for contributing! 🚀
