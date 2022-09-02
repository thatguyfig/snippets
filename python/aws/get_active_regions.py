import boto3

def get_active_aws_regions():

  """
  A function which gets a list of the AWS regions with VPCs present
  """

  # start by creating a client to ec2
  client = boto3.client("ec2")

  # get all region names possible
  all_regions = [x['RegionName'] for x in client.describe_regions()['Regions']]

  # create an empty list of active regions
  active_regions = []

  # iterate over all regions
  for region in all_regions:

    # create regional client to ec2
    client = boto3.client("ec2", region_name=region)

    # use client to describe VPCs
    response = client.describe_vpcs()

    # if there are more than 0 vpcs in this region
    if len(response['Vpcs']) > 0:

      # add the region to active regions
      active_regions.append(region)

  # return the active regions list
  return active_regions

if __name__ == "__main__":

  # get the active regions in the account
  regions = get_active_aws_regions()

  # log them
  print("[+] Found the following active regions:")
  print(regions)
