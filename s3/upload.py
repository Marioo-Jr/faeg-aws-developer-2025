import boto3
s3api = boto3.client("s3", region_name="us-east-1")
bucket_name = "Mariosergio1998"


s3api.create_bucket(Bucket =bucket_name)
print("Bucket criado com sucesso!")