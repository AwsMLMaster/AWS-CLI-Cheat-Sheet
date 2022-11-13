import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('ssm')
    response=client.get_parameters(Names=['/cfn/new-ec2/dev/instance-number'])

    p_value = response['Parameters'][0]['Value']
    #return "Success"
    print ("Parameter /cfn/new-ec2/dev/instance-number value is:", p_value)
    p_value_int = int(p_value)
    new_p_value_int = p_value_int + 1
    print("New parameter /cfn/new-ec2/dev/instance-number value is:", new_p_value_int)
    client.put_parameter(
        Name='/cfn/new-ec2/dev/instance-number',
        Value=str(new_p_value_int),
        Type='String',
        Overwrite=True
   )
    
