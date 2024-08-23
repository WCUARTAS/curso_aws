import boto3 
from keys import ACCESS_KEY,SECRET_KEY


def conectio_s3():
    session_aws = boto3.session.Session(ACCESS_KEY,SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    print("succesful connection")

    """
    print (session_s3)
    for bucket in session_s3.buckets.all():
        print(bucket.name)
        print("Archivos:")
        for obj in bucket.objects.all():
            print(f"- {obj.key}")
    """

def save_file():
    print("hola")


    