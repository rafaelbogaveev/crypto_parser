import distutils
from ico import Ico

def getParsedFloatOrNone(strFloat):
    float = None
    try:
        float = float(strFloat)
    except:
        float = None

    return float

def getIco(ico_list, item):
    ico = Ico()
    ico.id = ico_list[item]['Id']
    ico.url = ico_list[item]['Url']
    ico.imageUrl = ico_list[item]['ImageUrl']
    ico.name = ico_list[item]['Name']
    ico.coinName = ico_list[item]['CoinName']
    ico.icoStatus = ico_list[item]['ICOStatus']
    ico.icoTokenPercentageForInvestors = ico_list[item]['ICOTokenPercentageForInvestors']
    ico.icoDate = ico_list[item]['ICODate']
    ico.icoEndDate = ico_list[item]['ICOEndDate']

    startPrice = getParsedFloatOrNone(str(ico_list[item]['ICOStartPrice']))
    ico.icoStartPriceCurrency = startPrice

    ico.icoFundingTarget = ico_list[item]['ICOFundingTarget']
    ico.icoFundingCap = ico_list[item]['ICOFundingCap']
    ico.icoFundsRaisedUSD = ico_list[item]['ICOFundsRaisedUSD']
    ico.icoTokenSupply = ico_list[item]['ICOTokenSupply']
    ico.icoJurisdiction = ico_list[item]['ICOJurisdiction']
    ico.icoLegalAdvisers = ico_list[item]['ICOLegalAdvisers']
    ico.icoLegalForm = ico_list[item]['ICOLegalForm']
    ico.icoSecurityAuditCompany = ico_list[item]['ICOSecurityAuditCompany']
    ico.icoTokenType = ico_list[item]['ICOTokenType']
    ico.fullName = ico_list[item]['FullName']
    ico.lastUpdate = ico_list[item]['LastUpdate']
    ico.algorithm = ico_list[item]['Algorithm']
    ico.proofType = ico_list[item]['ProofType']
    ico.fullyPremined = ico_list[item]['FullyPremined']
    ico.preMinedValue = ico_list[item]['PreMinedValue']
    ico.totalCoinsFreeFloat = ico_list[item]['TotalCoinsFreeFloat']
    ico.sortOrder = ico_list[item]['SortOrder']
    ico.sponsored = distutils.util.strtobool(str(ico_list[item]['Sponsored']))

    return ico