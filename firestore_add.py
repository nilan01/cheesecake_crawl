import json
# firebase junk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

with open("insert_menu.json", "r") as json_file:
    data = json.load(json_file)

# for (k,v) in data.items():
#     doc_ref = db.collection(u'menu').document(f'{v["title"]}')
#     doc_ref.set({
#         #u'title': f'{str(v["title"])}',
#         u'description': f'{str(v["description"])}',
#         u'image': f'{str(v["background"][0]["image"])}',
#         u'caption': f'{str(v["background"][0]["caption"])}',
#         u'linkUrl': f'{str(v["background"][0]["linkUrl"])}',
#     })
for (k,v) in data.items():
    doc_ref = db.collection(u'menu').document(f'{v["title"]}')
    doc_ref.set({
        u'description': f'{str(v["description"])}',
        u'items': f'{str(v["background"])}'
        # u'image': f'{str(v["background"][0]["image"])}',
        # u'caption': f'{str(v["background"][0]["caption"])}',
        # u'linkUrl': f'{str(v["background"][0]["linkUrl"])}',
    })
    # for value in v['background']:
    #     doc_ref.update({
    #         u'items.caption': (f'{str(value["caption"])}'),
    #         u'items.linkUrl': (f'{str(value["linkUrl"])}'),
    #         u'items.image': (f'{str(value["image"])}')
    #         # u'linkUrl': f'{str(v["background"][0]["linkUrl"])}',
    #         # u'image': f'{str(v["background"][0]["image"])}'
    #     })


    #
    # print(f"Value (title): {str(v['title'])}")
    # print(f"Value (description): {str(v['description'])}")
    # for value in v['background']:
    #     print(value['caption'])
    #     print(value['linkUrl'])
    #     print(value['image'])
    # print("\n")

#print(data.items())
