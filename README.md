# What is this?

This is an automation. With one command, you will be able to create a new, blank local repository with your desired project name and push it up to your remote github repository.

## Get me going!!

1. clone the repository
```bash
git clone https://github.com/aaronlamtran/create-project-github-automation.git
```

2. navigate into repository
```bash
cd create-project-github-automation
```

3. install requirements
```bash
pip install -r requirements.txt
```

4. create your .env file
```bash
touch .env
```
 - (template provided - .example.env)

5. run bash script to initialize
```bash
source initialize.sh
```

6. anytime we want to create a local + remote project, run command:
```bash
create <desired project name>
```
 - this will:
   - create your local repo
   - push to your remote repo
   - open up your local repo in vscode

7. one less hurdle to jump through before building! enjoy!# README
# README
