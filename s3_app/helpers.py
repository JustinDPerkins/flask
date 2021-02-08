import boto3, botocore
from s3_app import app

ALLOWED_EXTENSIONS = set(['txt', 'zip', 'markdown', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(name):
    return "." in name and name.split(".")[1].lower() in ALLOWED_EXTENSIONS

# Connect to the s3 service
s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config["S3_KEY"],
    aws_secret_access_key=app.config["S3_SECRET"]
)
#upload file to s3 w/ acl as public  
def upload_file_to_s3(file, bucket_name, acl="public-read"):

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Unexpected Happened: ", e)
        return e
    # returns the webling to file upload to view
    return "{}{}".format(app.config["S3_LOCATION"], file.filename)
