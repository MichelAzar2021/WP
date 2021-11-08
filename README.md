# Whiteshield Test Task

In order to run this code on a local directory:

1- Use the terminal to run the following code to create a local directory and pull the data to it:

mkdir <directory name> ;  //Same directory name as the one you want to pull <br>
cd <directory name>;<br>
git remote add origin GIT_URL;<br>
git checkout -b 'branch name';<br>
git config core.sparsecheckout true;<br>
echo directory name/ >> .git/info/sparse-checkout;<br>
git pull origin 'pull branch name' <br>

2- In order to deploy the environment, please run the below code:

pip install -r requirements.txt

3- At last, please run main.py:

The code is expected to run 2 graphs on a single dashboard on the browser.

