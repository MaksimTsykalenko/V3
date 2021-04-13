import json
from app.db import tables
from app.models.chanels import ChanelBase
from app.models.shows import ShowBase
from app.db.database import get_session


session=next(get_session())
with open("d:\export.json","r", encoding="utf-8") as json_file:
    data = json.load(json_file)


for chanel_ in data['channels']:
    chanel=ChanelBase(title=chanel_["title"], icon= chanel_["logo"], disabled= False)
    chanel = tables.Chanel(**chanel.dict())
    session.add(chanel)
    session.commit()
    for show_ in chanel_['epg']:
        show = ShowBase(title=show_["title"], description=show_["description"],
                        start_t=" ".join(show_["start"].split()[:-1]), end_t=" ".join(show_["end"].split()[:-1]), chanel_id=chanel.id)
        show=tables.Show(**show.dict())
        session.add(show)
        session.commit()