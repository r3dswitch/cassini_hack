import xarray as xr

# Load NetCDF file
ds = xr.open_dataset('/Users/soumya/Desktop/cassini_hack/no2sentinel5p.nc', group='PRODUCT', engine='netcdf4')

df = ds['nitrogendioxide_tropospheric_column'].to_dataframe().reset_index()
# Print dataset structure
print(df.head(5))

