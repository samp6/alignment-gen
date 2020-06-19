from alignment import create_alignment

def lambda_handler(event, context):
    create_alignment()

lambda_handler("","")