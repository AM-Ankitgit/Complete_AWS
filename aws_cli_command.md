aws --version
aws configure

# List all S3 buckets
aws s3 ls

# Upload a file to an S3 bucket
aws s3 cp localfile.txt s3://yourbucketname/

# Launch an EC2 instance
aws ec2 run-instances --image-id ami-0abcdef1234567890 --count 1 --instance-type t2.micro --key-name YourKeyName

# Start an EC2 instance
aws ec2 start-instances --instance-ids i-1234567890abcdef0

# Stop an EC2 instance
aws ec2 stop-instances --instance-ids i-1234567890abcdef0

# Describe all EC2 instances
aws ec2 describe-instances

# Filter results when describing instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name,Tags]'

# Check the status of an instance
aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0

# Resize an instance
aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --instance-type "{\"Value\": \"t2.large\"}"

# Tag an instance
aws ec2 create-tags --resources i-1234567890abcdef0 --tags Key=Name,Value=MyInstance

# Create a security group
aws ec2 create-security-group --group-name my-security-group --description "My security group" --vpc-id vpc-12345678

# Add a rule to a security group
aws ec2 authorize-security-group-ingress --group-id sg-903004f8 --protocol tcp --port 22 --cidr 0.0.0.0/0

# Create a key pair
aws ec2 create-key-pair --key-name MyKeyPair --query 'KeyMaterial' --output text > MyKeyPair.pem

# Delete a key pair
aws ec2 delete-key-pair --key-name MyKeyPair

# Create a snapshot of a volume
aws ec2 create-snapshot --volume-id vol-1234567890abcdef0 --description "This is my volume snapshot"

# Create a new volume from a snapshot
aws ec2 create-volume --availability-zone us-west-2b --snapshot-id snap-1234567890abcdef0 --size 10

# Create an AMI from an instance
aws ec2 create-image --instance-id i-1234567890abcdef0 --name "My server backup" --description "An AMI for my server"

# Deregister an AMI
aws ec2 deregister-image --image-id ami-1234567890abcdef0

# Allocate a new Elastic IP
aws ec2 allocate-address --domain vpc

# Associate an Elastic IP with an instance
aws ec2 associate-address --instance-id i-1234567890abcdef0 --public-ip 203.0.113.0
