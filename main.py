# python 2 
# coding: utf-8

import boto.ec2

# Some attributes needed

access_key_id = ''   # access id
secret_access_key = '' # access key
ami_image_id = 'ami-97785bed'
security_group_name = 'my_sec_group'
security_group_explaination = 'A new security group'
new_keypair_name = 'mynewkeypair'
key_path = "" # directory to save the key_pairs .pem file


# Create a connection. Specify the region

conn = boto.ec2.connect_to_region("us-east-1", # Not us-east-1a, us-east-1b...
                                  aws_access_key_id = access_key_id,
                                  aws_secret_access_key = secret_access_key)

# Create a new security group
mygroup = conn.create_security_group(security_group_name, security_group_explaination)


# Create key pairs
newKey = conn.create_key_pair(new_keypair_name)

print(newKey.name)

# newKey.delete()

newKey.save(key_path)

# Launch your ec2 instance.

resv = conn.run_instances(ami_image_id,
                   key_name = 'mynewkeypair',
                   instance_type = 't2.micro',
                   security_groups = [security_group_name])

# show some attributes

inst = resv.instances[0]
print("Instance region:", inst.placement)
print("Instance ID", inst.id)
print("Instance IP address", inst.private_ip_address)


# Stop instance

conn.stop_instances(instance_ids=[inst.id])


# Terminate instance

conn.terminate_instances(instance_ids=[inst.id])

