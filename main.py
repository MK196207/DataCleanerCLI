# main.py

import pandas as pd
from transformations import (
    remove_before, remove_after, remove_char,
    to_lower, to_upper, trim_spaces
)

def column_menu(df, col):
    def show_sample(col_data):
        print(f"Podgląd kolumny '{col}':")
        print(col_data.head(5))
        print(f"Typ danych: {col_data.dtype}")

        # Sprawdź, czy są różnice w długości
        lengths = col_data.astype(str).str.len()
        unique_lengths = lengths.head(10).nunique()
        if unique_lengths > 1:
            print("Różne długości danych wykryte. Dodatkowa próbka:")
            print(col_data.iloc[5:10])
    print(f"Podgląd kolumny '{col}':")
    print(df[col].head(5))
    print(f"Typ danych: {df[col].dtype}")
    show_sample(df[col])
    while True:
        print(f"\nOperacje dla kolumny: {col}")
        print("1. Usuń wszystko PRZED znakiem")
        print("2. Usuń wszystko PO znaku")
        print("3. Usuń konkretny znak")
        print("4. Zamień na małe litery")
        print("5. Zamień na wielkie litery")
        print("6. Przytnij spacje")
        print("7. Zamień znak lub ciąg znaków na inny")
        print("0. Dalej (przejdź do następnej kolumny)")

        choice = input("Wybierz operację: ")

        if choice == '0':
            break
        elif choice in ['1', '2', '3']:
            char = input("Podaj znak: ")
            if choice == '1':
                df = remove_before(df, col, char)
            elif choice == '2':
                df = remove_after(df, col, char)
            elif choice == '3':
                df = remove_char(df, col, char)
        elif choice == '4':
            df = to_lower(df, col)
        elif choice == '5':
            df = to_upper(df, col)
        elif choice == '6':
            df = trim_spaces(df, col)
        elif choice == '7':
            old = input("Podaj znak lub ciąg do zamiany: ")
            new = input("Podaj nowy znak lub ciąg: ")
            df[col] = df[col].astype(str).str.replace(old, new, regex=False)
        else:
            print("Nieprawidłowa opcja.")
        show_sample(df[col])  # pokaż efekt po każdej operacji
    return df

def main():
    path = input("Podaj ścieżkę do pliku CSV: ")
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"Błąd podczas wczytywania pliku: {e}")
        return

    print("\nZaładowano dane. Oto kolumny:")
    print(df.columns.tolist())

    for col in df.columns:
        df = column_menu(df, col)

    save_path = input("\nPodaj nazwę pliku do zapisania (np. cleaned.csv): ")
    df.to_csv(save_path, index=False)
    print(f"\nZapisano oczyszczony plik jako: {save_path}")

if __name__ == "__main__":
    main()
