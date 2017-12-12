import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ico(Base):
    __tablename__ = 'ico'

    id = Column(Integer, primary_key=True)
    url = Column(String(256))
    imageUrl = Column(String(256))
    name = Column(String(256))
    coinName = Column(String(256))
    icoStatus = Column(String(256))
    icoTokenPercentageForInvestors = Column(String(256))
    icoDate = Column(Integer)
    icoEndDate = Column(Integer)
    icoStartPrice = Column(Float)
    icoStartPriceCurrency = Column(String(256))
    icoFundingTarget = Column(String(256))
    icoFundingCap = Column(String(256))
    icoFundsRaisedUSD = Column(String(256))
    icoTokenSupply = Column(String(256))
    icoJurisdiction = Column(String(256))
    icoLegalAdvisers = Column(String(256))
    icoLegalForm = Column(String(256))
    icoSecurityAuditCompany = Column(String(256))
    icoTokenType = Column(String(256))
    fullName = Column(String(256))
    lastUpdate = Column(Integer)
    algorithm = Column(String(256))
    proofType = Column(String(256))
    fullyPremined = Column(String(256))
    preMinedValue = Column(String(256))
    totalCoinsFreeFloat = Column(String(256))
    sortOrder = Column(String(256))
    sponsored = Column(Boolean)


engine = sa.create_engine("mysql+pymysql://root:1234@127.0.0.1/crypto_coins?charset=utf8", encoding='utf8')

Base.metadata.create_all(engine)
