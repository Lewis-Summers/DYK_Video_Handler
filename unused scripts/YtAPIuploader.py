import httplib
import httplib2
import os
import random
import sys
import time

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


def get_authenticated_service(args):
    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                   scope=YOUTUBE_UPLOAD_SCOPE,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        credentials = run_flow(flow, storage, args)

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))


def initialize_upload(youtube, options):
    tags = None
    if options.keywords:
        tags = options.keywords.split(",")

    body = dict(
        snippet=dict(
            title=options.title,
            description=options.description,
            tags=tags,
            categoryId=options.category
        ),
        status=dict(
            privacyStatus=options.privacyStatus
        )
    )

    # Call the API's videos.insert method to create and upload the video.
    insert_request = youtube.videos().insert(
        part=",".join(body.keys()),
        body=body,
        media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
    )
    print(insert_request)
    # resumable_upload(insert_request)


def upload(file, title, desc, cat=24, keywords=""):
    argparser.add_argument("--file", default=file)
    argparser.add_argument("--title", default=title)
    argparser.add_argument("--description", default=desc)
    argparser.add_argument("--category", default=cat)
    argparser.add_argument("--keywords", default=keywords)
    argparser.add_argument("--privacyStatus", default=VALID_PRIVACY_STATUSES[0])
    args = argparser.parse_args()
    print(args)

    if not os.path.exists(args.file):
        exit("Please specify a valid file using the --file= parameter.")

    youtube = get_authenticated_service(args)
    try:
        initialize_upload(youtube, args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content.decode()))


CLIENT_SECRETS_FILE = "client_secrets.json"
VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file"""

upload("file/test.mp4", "facts", "fun facts")


def upload(file, title, desc, cat=24, keywords=""):
    argparser.add_argument("--file", default=file)
    argparser.add_argument("--title", default=title)
    argparser.add_argument("--description", default=desc)
    argparser.add_argument("--category", default=cat)
    argparser.add_argument("--keywords", default=keywords)
    argparser.add_argument("--privacyStatus", default=VALID_PRIVACY_STATUSES[0])
    args = argparser.parse_args()
    print(args)

    if not os.path.exists(args.file):
        exit("Please specify a valid file using the --file= parameter.")

    youtube = get_authenticated_service(args)
    try:
        initialize_upload(youtube, args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content.decode()))