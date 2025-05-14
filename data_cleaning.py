import pandas as pd
import re


def load_raw_data(filepath):
    return pd.read_csv(filepath)

def extract_field(text, pattern, group=1, default=None, cast=None):
    match = re.search(pattern, text, re.MULTILINE)
    if match:
        value = match.group(group)
        if cast:
            try:
                return cast(value.replace(',', ''))
            except Exception:
                return default
        return value.strip()
    return default

def clean_calfire_data(df):
    # Extract variables from CAL FIRE updates page content
    df['Incident Name'] = df['Page Content'].apply(lambda x: extract_field(x, r'Name\s*\n(.+)', 1))
    df['Page DateTime'] = df['Page Title'].apply(lambda x: extract_field(x, r'Update on ([\d/]+) at ([\d: ]+[APM]+)', 0))
    df['Start DateTime'] = df['Page Content'].apply(lambda x: extract_field(x, r'Start Date/Time\s*\n([\d\-: ]+)', 1))
    df['Incident Status'] = df['Page Content'].apply(lambda x: extract_field(x, r'Incident Status\s*\n(.+)', 1))
    df['Location'] = df['Page Content'].apply(lambda x: extract_field(x, r'Location\s*\n(.+)', 1))
    df['Type'] = df['Page Content'].apply(lambda x: extract_field(x, r'Type\s*\n(.+)', 1))
    df['Cause'] = df['Page Content'].apply(lambda x: extract_field(x, r'Cause\s*\n(.+)', 1))
    df['Counties'] = df['Page Content'].apply(lambda x: extract_field(x, r'Counties\s*\n(.+)', 1))
    df['Acres Burned'] = df['Page Content'].apply(lambda x: extract_field(x, r'Size\s*\n([\d,]+)', 1, cast=int))
    df['Containment'] = df['Page Content'].apply(lambda x: extract_field(x, r'Containment\s*\n([\d]+%)', 1))
    df['Structures Threatened'] = df['Page Content'].apply(lambda x: extract_field(x, r'Structures Threatened\s*\n([\d,]+)', 1, cast=int))
    df['Structures Destroyed'] = df['Page Content'].apply(lambda x: extract_field(x, r'Structures Destroyed\s*\n([\d,]+)', 1, cast=int))
    df['Structures Damaged'] = df['Page Content'].apply(lambda x: extract_field(x, r'Structures Damaged\s*\n([\d,]+)', 1, cast=int))
    df['Civilian Injuries'] = df['Page Content'].apply(lambda x: extract_field(x, r'Civilian Injuries\s*\n([\d,]+)', 1, cast=int))
    df['Firefighter Injuries'] = df['Page Content'].apply(lambda x: extract_field(x, r'Firefighter Injuries\s*\n([\d,]+)', 1, cast=int))
    df['Civilian Fatalities'] = df['Page Content'].apply(lambda x: extract_field(x, r'Civilian Fatalities\s*\n([\d,]+)', 1, cast=int))
    df['Total Personnel'] = df['Page Content'].apply(lambda x: extract_field(x, r'Total Personnel\s*\n([\d,]+)', 1, cast=int))
    df['Engines'] = df['Page Content'].apply(lambda x: extract_field(x, r'Engines\s*\n([\d,]+)', 1, cast=int))
    df['Water Tenders'] = df['Page Content'].apply(lambda x: extract_field(x, r'Water Tenders\s*\n([\d,]+)', 1, cast=int))
    df['Hand Crews'] = df['Page Content'].apply(lambda x: extract_field(x, r'Hand Crews\s*\n([\d,]+)', 1, cast=int))
    df['Other Resources'] = df['Page Content'].apply(lambda x: extract_field(x, r'Other\s*\n([\d,]+)', 1, cast=int))
    df['Administration Unit'] = df['Page Content'].apply(lambda x: extract_field(x, r'Administration Unit\s*\n(.+)', 1))
    df['Unified Command Agency(s)'] = df['Page Content'].apply(lambda x: extract_field(x, r'Unified Command Agency\(s\)\s*\n(.+)', 1))
    return df

def main():
    raw_filepath = "calfire_updates_raw_data.csv"
    cleaned_filepath = "calfire_updates_cleaned.csv"
    df = load_raw_data(raw_filepath)
    df = clean_calfire_data(df)
    output_columns = [
        'Incident Name', 'Page DateTime', 'Start DateTime', 'Incident Status', 'Location', 'Type', 'Cause', 'Counties',
        'Acres Burned', 'Containment', 'Structures Threatened', 'Structures Destroyed', 'Structures Damaged',
        'Civilian Injuries', 'Firefighter Injuries', 'Civilian Fatalities', 'Total Personnel', 'Engines',
        'Water Tenders', 'Hand Crews', 'Other Resources', 'Administration Unit', 'Unified Command Agency(s)'
    ]
    df[output_columns].to_csv(cleaned_filepath, index=False)
    print(f"Cleaned data saved to {cleaned_filepath}")

if __name__ == "__main__":
    main()