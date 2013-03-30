import gdata.docs.service
#
client = gdata.docs.service.DocsService()
client.ClientLogin('accidental.wong@gmail.com', '91503149')
#
file_to_upload = "files/docs/Lesson1.docx"
ms = gdata.MediaSource(file_path=file_to_upload, content_type=gdata.docs.service.SUPPORTED_FILETYPES["DOCX"])
client.Upload(ms, "UseThisNameLesson1.docx")