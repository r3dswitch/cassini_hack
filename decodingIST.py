import pandas as pd
import datetime

# Load your dataset
file_path = 'IST_corrected.csv'  
stroke_data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Month abbreviation dictionary (adjust based on your data)
month_dict = {
    'sty': '01', 'lut': '02', 'mar': '03', 'kwi': '04', 'maj': '05',
    'cze': '06', 'lip': '07', 'sie': '08', 'wrz': '09', 'paz': '10', 
    'lis': '11', 'gru': '12'
}

# Function to decode the randomized date without time
def decode_randomized_date(row):
    try:
        # Split the randomized date into month and year
        month_abbr, year = row['RDATE'].split('-')
        month = month_dict.get(month_abbr.lower(), '01')

        # Use the day from DAYLOCAL if reasonable (1-31), otherwise default to 15
        day = row['DAYLOCAL'] if 1 <= row['DAYLOCAL'] <= 31 else 15

        # Combine into standard YYYY-MM-DD without time
        decoded_date = f'1991-{month}-{str(day).zfill(2)}'
        return decoded_date
    except:
        return 'Invalid Date'

# Apply the decoding function
stroke_data['Decoded_Date'] = stroke_data.apply(decode_randomized_date, axis=1)

# Save the updated dataset with decoded dates
stroke_data.to_csv('decoded_stroke_data.csv', index=False)

print("Decoding complete. Decoded dates saved to 'decoded_stroke_data.csv'.")