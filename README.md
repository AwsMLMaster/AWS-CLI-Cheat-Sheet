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

3.  Create new repo from cli (after aws sso login)
    ```aws codecommit create-repository --repository-name ServiceCatalog --repository-description "Service Catalog CFN code"```

4.	Clone repo: ```git clone codecommit://MyDemoRepo my-demo-repo```.
    No need for full https/ssh link. just the remote and local repo name.
    
    Uner the directory you ran the command above, a new directory will be created with the givven name:  _my-demo-repo_

5.	Troubleshoot:

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
    
    **_Problem 3_**: ```Cloning into 'custom-control-tower-configuration'...```  
    ```git: 'remote-codecommit' is not a git command. See 'git --help'.```
    
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

## Git -  standard order of code change and push
  1. git status
  2. git add .
  3. git commit -m "message about the change"
  4. git push


## Access S3 endpoint
aws s3 --region eu-west-1 --endpoint-url https://bucket. ```s3 main endpoint``` ls s3://```bucketname```

## Upload & Download files from S3
https://towardsdatascience.com/how-to-upload-and-download-files-from-aws-s3-using-python-2022-4c9b787b15f2


## AWS CLI - get list of account and use them in another cli command
```aws cloudformation delete-stack-instances --stack-set-name <StackSetName>  --accounts `aws cloudformation list-stack-instances --stack-set-name <StackSetName> --query 'Summaries[*].Account' --output text | sed 's/\t/ /g'` --regions <region_name> --no-retain-stacks```


## Lambda - Create Lambda layer for specific python version
https://www.linkedin.com/pulse/how-create-confluent-python-lambda-layer-braeden-quirante/

## python virtual environment

create virtual environment
```python3 -m venv .venv```

activate virtual environment
```source .venv/bin/activate```

deactivate virtual environment
```deactivate```

install packages into virtual environment
```pip install -r requirements.txt```

## VS Code Jupyter Notebook AWS credentials

### Jupyter credentials alignment with terminal/AWS profile for boto3 functions - maybe the easiest
```boto3.setup_default_session(profile_name='ML-US-WEST-2')```

### Jupyter credentials alignment with terminal/AWS profile for boto3 functions

to align jupyter credentials with VS Code terminal (```export AWS_PROFILE=ML-US-WEST-2```), To exit the AWS profile in your command prompt: ```unset AWS_PROFILE```

```
session = boto3.Session(profile_name="ML-US-WEST-2")  # Replace with your profile name
boto3_bedrock = session.client(service_name="bedrock-runtime", region_name="us-west-2")
```

in jupyter notebook check alignment with the terminal:
```
import os

os.system("echo $VIRTUAL_ENV")
os.system("pwd")
os.chdir("/Users/username/path/to/working/dir")
print(os.getcwd())
```

### Jupyter credentials alignment with terminal/AWS profile for 3rd party functions (e.g: langchain)

#### Initialize
```
# Load the specific AWS profile
profile_name = "ML-US-WEST-2"
session = boto3.Session(profile_name=profile_name)
```
#### Use
```
# Get the credentials from the session
credentials = session.get_credentials()
aws_access_key_id = credentials.access_key
aws_secret_access_key = credentials.secret_key
aws_session_token = credentials.token

from langchain_aws import ChatBedrock
llm = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={
        "max_tokens": 200,
        "temperature": 0,  # Using 0 to get reproducible results
        "stop_sequences": ["\n\nHuman:"]
    },
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name="us-west-2"
)
```
