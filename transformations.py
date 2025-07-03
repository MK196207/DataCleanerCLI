# transformations.py

def remove_before(df, col, char):
    df[col] = df[col].astype(str).apply(lambda x: x.split(char)[-1] if char in x else x)
    return df

def remove_after(df, col, char):
    df[col] = df[col].astype(str).apply(lambda x: x.split(char)[0] if char in x else x)
    return df

def remove_char(df, col, char):
    df[col] = df[col].astype(str).str.replace(char, '', regex=False)
    return df

def to_lower(df, col):
    df[col] = df[col].astype(str).str.lower()
    return df

def to_upper(df, col):
    df[col] = df[col].astype(str).str.upper()
    return df

def trim_spaces(df, col):
    df[col] = df[col].astype(str).str.strip()
    return df
