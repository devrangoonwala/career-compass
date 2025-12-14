# Security Policy

## Reporting Security Issues

If you discover a security vulnerability in this project, please report it by emailing the maintainer or opening a private security advisory on GitHub.

**Please do not report security vulnerabilities through public GitHub issues.**

## Secure Configuration

### Environment Variables

This project uses environment variables to store sensitive information like API keys. **Never commit these to version control.**

1. **Setup**: Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```

2. **Configure**: Add your actual API keys to `.env`
   ```bash
   GROQ_API_KEY=your_actual_key_here
   ```

3. **Verify**: Ensure `.env` is in `.gitignore` (already configured)

### Protected Files

The following files are protected and should **never** be committed:
- `.env`
- `.env.local`
- `*.env` (any file ending in .env)
- Any file containing API keys or secrets

### API Keys

This project requires the following API keys:

- **Groq API Key**: Get one at [console.groq.com](https://console.groq.com/)
  - Environment variable: `GROQ_API_KEY`
  - Used for: AI-powered job analysis via Kestra workflows

### Best Practices

1. ✅ **Use environment variables** for all secrets
2. ✅ **Never hardcode** API keys in source code
3. ✅ **Keep `.gitignore` updated** to exclude sensitive files
4. ✅ **Use `.env.example`** as a template (without actual keys)
5. ✅ **Rotate keys** if accidentally exposed
6. ✅ **Use different keys** for development and production

### If You Accidentally Commit a Secret

1. **Immediately rotate** the compromised key/token
2. **Remove it from git history** using tools like `git-filter-repo` or BFG Repo-Cleaner
3. **Force push** to update the remote repository
4. **Notify** anyone who may have pulled the compromised version

## Deployment Security

When deploying to Vercel or other platforms:

1. Use platform environment variables (not `.env` files)
2. Enable environment variable encryption where available
3. Restrict access to production environment variables
4. Use separate keys for staging and production

## Dependencies

- Regularly update dependencies to patch security vulnerabilities
- Review `npm audit` and `pip-audit` outputs
- Use dependabot or similar tools for automated updates

## Questions?

If you have questions about security in this project, please open a discussion or contact the maintainers.
