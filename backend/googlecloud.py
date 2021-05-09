import os
import json
import re
from google.cloud import vision
from google.cloud import storage

""" INPUT PATH TO JSON API KEY"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"

def async_detect_document(gcs_source_uri, gcs_destination_uri="gs://tohacks-buc/pdf_results/"):
    """OCR with PDF/TIFF as source files on GCS"""

    gcs_destination_uri = gcs_destination_uri + gcs_source_uri
    gcs_source_uri = "gs://tohacks-buc/" + gcs_source_uri
    # Supported mime_types are: 'application/pdf' and 'image/tiff'
    mime_type = 'application/pdf'

    # How many pages should be grouped into each json output file.
    batch_size = 2

    client = vision.ImageAnnotatorClient()

    feature = vision.Feature(
        type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)

    gcs_source = vision.GcsSource(uri=gcs_source_uri)
    input_config = vision.InputConfig(
        gcs_source=gcs_source, mime_type=mime_type)

    gcs_destination = vision.GcsDestination(uri=gcs_destination_uri)
    output_config = vision.OutputConfig(
        gcs_destination=gcs_destination, batch_size=batch_size)

    async_request = vision.AsyncAnnotateFileRequest(
        features=[feature], input_config=input_config,
        output_config=output_config)

    operation = client.async_batch_annotate_files(
        requests=[async_request])

    # print('Waiting for the operation to finish.')
    operation.result(timeout=420)

    # Once the request has completed and the output has been
    # written to GCS, we can list all the output files.
    storage_client = storage.Client()

    match = re.match(r'gs://([^/]+)/(.+)', gcs_destination_uri)
    bucket_name = match.group(1)
    prefix = match.group(2)

    bucket = storage_client.get_bucket(bucket_name)

    # List objects with the given prefix.
    blob_list = list(bucket.list_blobs(prefix=prefix))
    # print('Output files:')
    # for blob in blob_list:
    #     print(blob.name)

    # Process the first output file from GCS.
    # Since we specified batch_size=2, the first response contains
    # the first two pages of the input file.
    output = blob_list[0]

    json_string = output.download_as_string()
    response = json.loads(json_string)

    # The actual response for the first page of the input file.
    first_page_response = response['responses'][0]
    annotation = first_page_response['fullTextAnnotation']

    # Here we print the full text from the first page.
    # The response contains more information:
    # annotation/pages/blocks/paragraphs/words/symbols
    # including confidence scores and bounding boxes
    # print('Full text:\n')
    return annotation['text']

# gcs_source_uri = "claimletter-converted.pdf"
# gcs_destination_uri = "gs://tohacks-buc/pdf_results/"
# print(async_detect_document(gcs_source_uri))

def upload_blob(source_file_name, bucket_name="tohacks-buc", destination_blob_name=""):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    destination_blob_name = os.path.split(source_file_name)[1]

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

    # create pdf to text already
    async_detect_document(destination_blob_name)

    return "OK"

# bucket_name = "tohacks-buc"
# source_file_name = "/home/niyon/Downloads/claim-letter-05-converted.pdf"
# upload_blob(source_file_name)

def get_pdf_text(source_blob_name, bucket_name="tohacks-buc"):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    source_blob_name = "pdf_results/"+ source_blob_name + "output-1-to-1.json"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    # blob = bucket.blob(source_blob_name)
    # blob.download_to_filename(destination_file_name)

    blob = bucket.get_blob(source_blob_name).download_as_string()

    response = json.loads(blob)

    # The actual response for the first page of the input file.
    first_page_response = response['responses'][0]
    annotation = first_page_response['fullTextAnnotation']

    return annotation['text']

    # print(
    #     "Blob {} downloaded to {}.".format(
    #         source_blob_name, destination_file_name
    #     )
    # )

# print(get_pdf_text("pdf_results/claimletter-converted.pdfoutput-1-to-1.json"))
