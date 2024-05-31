# NOTE
# REMOVE PREVIOUS DATABASE.DB BEFORE LOADING DATA
#IMPORT
from nepseRequestParser import nepseReqParser
from responseParser import responseParser
from datetime import date,timedelta

# PROGRESSBAR
def progressbar(progress, total):
    percentage = 100 * (progress / float(total))
    bar = '█' * int(percentage) + '-' * (100 - int(percentage))
    print(f"\r|: {bar} :| {percentage:.2f}%", end="\r")
# MAIN
def main() :
    _stockCount = 5
    for i in range(_stockCount):
        _date = date.today()-timedelta(days=i)
        response = nepseReqParser(_date)
        if len(response.text) < 300:
            pass
        else:
            responseParser(response=response,_date=_date)
        progressbar(i+1,_stockCount)

if __name__ == "__main__":
    main()
