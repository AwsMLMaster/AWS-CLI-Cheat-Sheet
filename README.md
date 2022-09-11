# Liran’s AWS CLI Cheat Sheet

## Identity and credentials

1.	List all configuration data. 
  
    ```aws configure list```

2.	switch between profiles
 
    ```export AWS_PROFILE=160177016713_reposname_codecommit_powerusers_```

3.	List profiles. 

    ```aws configure list-profiles```

4.	Who am I  

    default:  
    ```aws sts get-caller-identity```  
      
    for a specific profile:  
    ```aws sts get-caller-identity --profile <profile name>```  

5.	Enable command completion

    ```$ which aws_completer```
    ```$ complete -C '/usr/local/bin/aws_completer' aws```

6.	To get a return code to confirm the status of the command

    ```$ echo $?```
7.	

## Git -  CodeCommit (Working with code-commit remote repos)

1.	Save your programmatic access key and secret typically found at ~/.aws/credentials.
      (Learn more: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html?icmpid=docs_sso_user_portal)

2.	Install git-remote-codecommit: pip3 install git-remote-codecommit. Validate the installation path in in your $PATH.
    (See More: https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html)

3.	Clone repo: ```git clone codecommit://MyDemoRepo my-demo-repo```.
    No need for full https/ssh link. just the remote and local repo name.

4.	Troubleshoot:

    •	**git clone**:
    
    ```Cloning into 'local-repo-name'...```
    ```fatal: repository 'https://account.eu-west1.amazonaws.com/v1/repos/remotereponame/' not found```
    
    **_Problem 1_**: your credentials are probably not active.
    
    **_Resolution 1_**:
    
    option 1: export AWS_PROFILE=user2 (use your relevant profile as default)
    
    option 2: copy from the SSO webpage the Command line or programmatic access environment variables (copy text under option1 on web page)
    
    **_Problem 2_**: git-remote-code commit not accessible
    
    **_Resolution 2_**: add installation path to PATH environment variable

    ```export PATH="/Users/username/Library/Python/3.8/bin:$PATH"```
    
    **_Problem 3_**: Cloning into 'custom-control-tower-configuration'...
    git: 'remote-codecommit' is not a git command. See 'git --help'.
    
    **_Resolution 3_**: reinstall git-remote-codecommit

    ```brew install git-remote-codecommit```

    •	**git push** (local origin to remote master branch)
    
    ```git push -u origin master```
    
    ```fatal: unable to access 'https://gitcodecommit.euwest1.amazonaws.com/v1/repos/reposname/': The requested URL returned error: 403```
    
    **_Problem_ 1**: credential helper wasn’t set up
    
    **_Resolution_**:
    
    For Mac/Linux: single quote
    git config --global credential.helper '!aws codecommit credential-helper $@'
    git config --global credential.UseHttpPath true
    
    For Windows: double quote
    git config --global credential.helper "!aws codecommit credential-helper $@"
    git config --global credential.UseHttpPath true

    **_Problem 2_**: onmac -clear key chain
    
    **_Resolution_**: 

    https://stackoverflow.com/questions/34517534/running-git-clone-against-aws-codecommits-gets-me-a-403-error

    1.	Open Keychain Access
    2.	Search for CodeCommit. You should find this:

    3.	Select 'git-codecommit....' and press delete
    4.	Confirm the delete.
    Now try again. It should work. You may have to do it again next time as well when you face the error 403.
    One of the possible reason for this issue is the keychain password different than login password on your MAC.

## Terraform -  using sso
  1. Configuring the AWS CLI to use AWS SSO for a specific account and add new profile entry
    ```aws configure sso```
  2. Relogin using:  
     ```aws sso login```  
     or with the relevant profile:  
     ```aws sso login --profile AWSAdministratorAccess-12345678```
  3. Use terraform :)
      ```terraform init```
      ```terraform plan```
      ```terraform apply```
      ```terraform destroy```

    ![image](https://user-images.githubusercontent.com/105966482/169641694-6daee9cd-cafa-44f2-9312-a1272e423629.png)
