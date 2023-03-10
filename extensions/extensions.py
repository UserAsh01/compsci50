import mimetypes
# imports the mimetypes module, which provides a database of file types and their corresponding media types.

#promt user for filename
filename = input("Please enter the name of a file: ").strip()

#get file suffix and convert to lower case
suffix = filename.split(".")[-1].lower() if "." in filename else ""

#determine media type based on suffix
if suffix in ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]:
    media_type = mimetypes.types_map["." + suffix]
else:
    media_type = "application/octet-stream"

#output media type
print(media_type)