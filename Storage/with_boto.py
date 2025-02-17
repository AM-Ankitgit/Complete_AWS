import boto3
import os

# lets use the amazon simple storage service

artifact= "D:/Brainwired/FarmTestDataClean/images/lowpass.png"

s3 = boto3.resource('s3')
# print the bucket name
for bucket_name in s3.buckets.all():
    bucket_name_ = bucket_name.name # print all the bucket present in s3 servies

data = open(artifact,'rb')
s3.Bucket(bucket_name_).put_object(Key='lowpass.png',Body=data)





# method -2
# os.system(f"aws s3 cp {artifact} s3://testbotos3")  # this is use to copy the local file to s3 bucket
#os.system(f"aws s3 sync {artifact_folder} s3:/{bucket_name}/artifact") # this to sync articats