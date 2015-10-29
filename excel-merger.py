import  sys
import  pandas as pd
import  os
def main(argv):
    if len(argv) != 2:
        print "EXCEL MERGER:"
        print "    Usage: python <EXCEL DIR>"
        print ""
        print argv[1]
        sys.exit(1)

    import glob

    files = glob.glob(argv[1]+"/*.xls")
    print argv[1]+"/*.xls"
    print files
    Count =  0
    all_data = pd.DataFrame()
    for f in files:
        df = pd.read_excel(f)
        # all_data = all_data.append(df,ignore_index=True)
        all_data = all_data.append(df)
        Count += 1
    print Count ,'Files have been Merged!'
    all_data = all_data.dropna(axis=0)
    # print all_data.head(30)
    all_data.to_excel(str(Count)+ ' Merged files'+'-'+os.path.basename(argv[1])+'-' +'.xls')



if __name__ == "__main__":
    main(sys.argv)

