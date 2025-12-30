# How to Upload Your Flask App to GitHub

Follow these steps to upload your Flask application to GitHub:

## Prerequisites
- A GitHub account (sign up at https://github.com if you don't have one)
- Git installed on your computer

## Step 1: Check if Git is installed
Open PowerShell or Command Prompt and run:
```bash
git --version
```
If Git is not installed, download it from: https://git-scm.com/download/win

## Step 2: Initialize Git repository
In your project folder, run:
```bash
cd "C:\Users\sanaz\Documents\SEM7\ssd lab\flask_app"
git init
```

## Step 3: Add all files to Git
```bash
git add .
```

## Step 4: Make your first commit
```bash
git commit -m "Initial commit: Basic Flask app"
```

## Step 5: Create a new repository on GitHub
1. Go to https://github.com and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Enter a repository name (e.g., "flask-basic-app")
5. Choose Public or Private
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

## Step 6: Connect your local repository to GitHub
After creating the repository, GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```
Replace `YOUR_USERNAME` with your GitHub username and `YOUR_REPO_NAME` with your repository name.

## Step 7: Push your code to GitHub
```bash
git branch -M main
git push -u origin main
```

You'll be prompted to enter your GitHub username and password (or personal access token).

## Alternative: Using GitHub Desktop (Easier Method)

If you prefer a graphical interface:

1. Download GitHub Desktop from: https://desktop.github.com/
2. Install and sign in with your GitHub account
3. Click "File" → "Add Local Repository"
4. Browse to your flask_app folder and select it
5. Click "Publish repository"
6. Choose a name and make it public/private
7. Click "Publish repository"

## Troubleshooting

### If you get authentication errors:
- Use a Personal Access Token instead of password
- Generate one at: https://github.com/settings/tokens
- Select "repo" scope when creating the token
- Use the token as your password when pushing

### If files are not being tracked:
- Make sure you're in the correct directory
- Check that `.gitignore` is not excluding important files
- Run `git status` to see what files are tracked

## Future Updates

After making changes to your code:

```bash
git add .
git commit -m "Description of changes"
git push
```

## Your Repository Structure

Your GitHub repository will contain:
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates folder
- `static/` - Static files folder (currently empty)
- `README.md` - Project documentation
- `.gitignore` - Files to exclude from Git

---

**Note:** Make sure to change the `secret_key` in `app.py` before deploying to production!

