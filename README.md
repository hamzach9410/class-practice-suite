# Class Projects Collection

Complete project structure for learning and development.

## 📁 Project Structure

- **frontend/** - Frontend applications
- **backend/** - Backend services  
- **login-service/** - Authentication service
- **utilities/** - Utility applications
  - file-converter/
  - calculator/
  - humanizer/
  - chatbot/
- **class-projects/** - Academic projects

## 🚀 Quick Start for Students

### 1. Clone Repository
```bash
git clone https://github.com/hamzach9410/class-practice-suite.git
cd class-practice-suite
```

### 2. Create Your Project Branch
```bash
# Create your own branch for your project
git checkout -b frontend-yourname
# OR
git checkout -b backend-yourname
# OR
git checkout -b calculator-yourname
# OR
git checkout -b chatbot-yourname
# etc...

# Examples:
git checkout -b frontend-hamza
git checkout -b calculator-sara
git checkout -b chatbot-ali
```

### 3. Work on Your Code
- Add your files in the respective folder
- Make your changes
- Test your code

### 4. Save Your Work
```bash
# Add all changes
git add .

# Commit with meaningful message
git commit -m "Add: your feature description"

# Push your branch to main
git push origin frontend-yourname
```

### 5. Create Pull Request
1. Go to GitHub repository
2. Click "Compare & pull request"
3. Select base branch as `main`
4. Add description of your work
5. Submit pull request

## 📋 Branch Guidelines

### Naming Convention
- `projectname-yourname`
- Examples: `frontend-john`, `calculator-sara`, `chatbot-ali`

### Commit Messages
- `Add: new feature`
- `Fix: bug description`
- `Update: what you changed`
- `Remove: what you deleted`

## 🔄 Sync with Latest Changes
```bash
# Switch to main branch
git checkout main

# Pull latest changes
git pull origin main

# Switch back to your branch
git checkout frontend-yourname

# Merge latest changes
git merge main
```

## 📝 Project-Specific Instructions

### Frontend Projects
- Use `frontend/` folder
- Branch: `frontend-yourname`
- Technologies: HTML, CSS, JavaScript, React

### Backend Projects
- Use `backend/` folder
- Branch: `backend-yourname`
- Technologies: Node.js, Python, Java

### Utility Projects
- Use respective `utilities/project-name/` folder
- Branch: `projectname-yourname`
- Add your implementation files

### Class Projects
- Use `class-projects/` folder
- Branch: `class-projects-yourname`
- Organize by assignment/topic

## ⚠️ Important Rules

1. **Never push directly to main branches**
2. **Always create your personal branch**
3. **Test your code before committing**
4. **Write clear commit messages**
5. **Ask for help if stuck**

## 🆘 Common Commands

```bash
# Check current branch
git branch

# Check status
git status

# See all branches
git branch -a

# Delete local branch
git branch -d branchname

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

## 📞 Need Help?

- Check existing branches: `git branch -a`
- Ask instructor for guidance
- Review other students' pull requests for examples