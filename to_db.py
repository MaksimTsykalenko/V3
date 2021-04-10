import json
from app.models.chanels import ChanelBase
from app.models.shows import ShowBase
from app.services.shows import ShowsService
from app.services.chanels import ChanelsService


with open("d:\export.json","r", encoding="utf-8") as json_file:
    data = json.load(json_file)


for chanel_ in data['channels']:
    chanel=ChanelBase(title=chanel_["title"], icon= chanel_["logo"], disabled= False)

    for show_ in chanel_['epg']:
        show = ShowBase(title=show_["title"], description=show_["description"],
                        start_t=" ".join(show_["start"].split()[:-1]), end_t=" ".join(show_["end"].split()[:-1]), chanel_id=chanel_["id"])
        break
    break

print (chanel)
aaa=ChanelsService()
bbb=aaa.create(chanel)
print (type(bbb))
print (bbb)