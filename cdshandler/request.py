import os
import cdsapi

class requestBulk:
    def __init__(self, request):
        self.years = request['year']
        self.months = request['months']
        self.output_path = request['output_path']
        days = request['days']
        if days == ['all']:
            self.days = [
                "01", "02", "03",
                "04", "05", "06",
                "07", "08", "09",
                "10", "11", "12",
                "13", "14", "15",
                "16", "17", "18",
                "19", "20", "21",
                "22", "23", "24",
                "25", "26", "27",
                "28", "29", "30",
                "31"]
        else:
            self.days = days
        os.makedirs(self.output_path, exist_ok=True)
        self.output_filename = os.path.join(self.output_path, request['output_filename'])
        if os.path.exists(self.output_filename):
            sys.exit(f"Output file already exists: {self.output_filename}")
        self.getData()
        return

    def getData(self):
        dataset = "reanalysis-era5-single-levels"
        request = {
            "product_type": ["reanalysis"],
            "variable": [
                "10m_u_component_of_wind",
                "10m_v_component_of_wind",
                "2m_dewpoint_temperature",
                "2m_temperature",
                "mean_sea_level_pressure",
                "surface_pressure",
                "mean_total_precipitation_rate",
                "mean_surface_downward_short_wave_radiation_flux",
                "mean_surface_downward_long_wave_radiation_flux",
                "mean_snowfall_rate"
            ],
            "year": self.years,
            "month": self.months,
            "day": self.days,
            "time": [
                "00:00", "03:00", "06:00",
                "09:00", "12:00", "15:00",
                "18:00", "21:00"
            ],
            "data_format": "netcdf",
            "download_format": "unarchived"
        }
        target = self.output_filename
        client = cdsapi.Client()
        client.retrieve(dataset, request, target)

    def cdointerp(self):
        #note: function to remap data from source grid to target grid
        #from cdo import *
        #nco=Cdo()
        #source_data = folder + 'output_rates_2009.nc'
        #target_grid = cfg_folder + 'u_10.15JUNE2009_fill.nc'
        #output_file = folder + 'interp_2009.nc'
        #nco.remapbil(target_grid, input=source_data, output=output_file)
        pass