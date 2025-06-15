from langchain_community.document_loaders import CSVLoader, YoutubeLoader
# from langchain_community.tools import You

# Each row is a document
loader = CSVLoader(
    file_path='Social_Network_Ads.csv'
)


docs = loader.load()

print(len(docs))


# loader = YoutubeLoader.from_youtube_url(
#     "https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=False
# )

# doc = loader.load()

# print(doc)