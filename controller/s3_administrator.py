import boto3 
from keys import ACCESS_KEY,SECRET_KEY


def conectio_s3():
    session_aws = boto3.session.Session(ACCESS_KEY,SECRET_KEY)
    session_s3 = session_aws.resource('s3')
    print("succesful connection")

    return session_s3

def upload_file(session_s3,photo,photo_name):
    bucket_name="bucket-curso-aws-wc-1"
    file_s3_path="images_web/"+photo_name
    session_s3.Bucket(bucket_name).upload_fileobj(photo,file_s3_path,ExtraArgs={'ACL': 'public-read'})
    print("archivo guardado en S3")


    