from cdshandler import requestBulk
years = ['2016']
months = ['06']
days = ['01'] #all
output_path = './bulk_files'
output_filename = f'bulk_file_{years[0]}-{months[0]}.nc'

# ================request data===============
request = {
    'year': years,
    'months': months,
    'days': days,
    'output_path': output_path,
    'output_filename': output_filename}

requestBulk(request)