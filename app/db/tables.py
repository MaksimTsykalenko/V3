import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Chanel(Base):
    __tablename__='chanels'
    id = sa.Column(sa.Integer,primary_key=True)
    title = sa.Column(sa.String(256))
    icon = sa.Column(sa.String(256))
    disabled = sa.Column(sa.Boolean, server_default=sa.sql.expression.false())


class Show(Base):
    __tablename__='shows'
    id = sa.Column(sa.BigInteger, primary_key=True)
    title = sa.Column(sa.String(256))
    description = sa.Column(sa.Text)
    start_t = sa.Column(sa.DateTime)
    end_t = sa.Column(sa.DateTime)
    chanel_id = sa.Column(sa.Integer)
