import boto3


def demo (event, context):
    
    sts_connection = boto3.client('sts')
    acct_b = sts_connection.assume_role(
        RoleArn="arn:aws:iam::237918227349:role/jenkins-instance-role",
        RoleSessionName="jenkins-instance-role"
    )
    

    return "Hello from Lambda"
