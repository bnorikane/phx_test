# python script to test Portal Script Runner job
# Based on DNC Portal Script Runner training


client = bigquery.Client(project='CO Party')

# create table in BigQuery

def load_to_bq():
    rescsv = open('pct_area.csv', 'rb')  # NOTE: rb mode
    client.load_table_from_file(rescsv, 'demscosp.sbx_norikaneb.script_test')


# Check script arguments and dump for debug run
# if len(sys.argv) > 1:
#     if sys.argv[1] == 'dump':C
#         dump_pdf()
# else:
#     #run job
load_to_bq()

