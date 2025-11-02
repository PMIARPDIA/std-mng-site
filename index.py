import os
import json
import random

FILE_NAME = "users.js"

def load_users():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write("let data = ")
        json.dump(users, f, ensure_ascii=False, indent=4)

def generate_id(users):
    existing_ids = {u["id"] for u in users}
    while True:
        new_id = random.randint(1000, 9999)
        if new_id not in existing_ids:
            return new_id

def input_name(prompt):
    while True:
        name = input(prompt).strip()
        if all(ch.isalpha() for ch in name) and name:
            return name.capitalize()
        print("Yalnız hərflərdən ibarət ad/soyad daxil edin.")

def input_age(prompt):
    while True:
        yas = input(prompt).strip()
        if yas.isdigit() and int(yas) > 0:
            return int(yas)
        print("Yaş yalnız müsbət tam ədəd olmalıdır.")

def add_user(users):
    ad = input_name("Ad daxil edin: ")
    soyad = input_name("Soyad daxil edin: ")
    yas = input_age("Yaş daxil edin: ")

    new_user = {
        "id": generate_id(users),
        "ad": ad,
        "soyad": soyad,
        "yas": yas
    }
    users.append(new_user)
    save_users(users)
    print("İstifadəçi əlavə olundu.")

def delete_user(users):
    try:
        uid = int(input("Silinəcək istifadəçinin ID-sini daxil edin: "))
    except ValueError:
        print("Yanlış ID.")
        return
    for u in users:
        if u["id"] == uid:
            users.remove(u)
            save_users(users)
            print(f"İstifadəçi (ID {uid}) silindi.")
            return
    print("Belə ID tapılmadı.")

def show_users(users):
    try:
        choice = int(input("İstifadəçi ID-si (hamısı üçün 0 yaz): "))
    except ValueError:
        print("Yanlış giriş.")
        return
    if choice == 0:
        if not users:
            print("İstifadəçi siyahısı boşdur.")
        else:
            print("\n--- Bütün istifadəçilər ---")
            for u in users:
                print(f"ID: {u['id']}, {u['ad']} {u['soyad']}, Yaş: {u['yas']}")
    else:
        for u in users:
            if u["id"] == choice:
                print(f"ID: {u['id']}, Ad: {u['ad']}, Soyad: {u['soyad']}, Yaş: {u['yas']}")
                return
        print("Belə ID tapılmadı.")

def update_user(users):
    try:
        uid = int(input("Yenilənəcək istifadəçinin ID-sini daxil edin: "))
    except ValueError:
        print("Yanlış ID.")
        return
    for u in users:
        if u["id"] == uid:
            print(f"Hal-hazırki məlumatlar: {u['ad']} {u['soyad']}, {u['yas']} yaş")
            ad = input("Yeni ad (boş buraxmaq üçün Enter): ").strip()
            soyad = input("Yeni soyad (boş buraxmaq üçün Enter): ").strip()
            yas = input("Yeni yaş (boş buraxmaq üçün Enter): ").strip()

            if ad:
                if all(ch.isalpha() or ch in "- " for ch in ad):
                    u["ad"] = ad.capitalize()
                else:
                    print("Ad yalnız hərflərdən ibarət olmalıdır, dəyişiklik tətbiq edilmədi.")

            if soyad:
                if all(ch.isalpha() or ch in "- " for ch in soyad):
                    u["soyad"] = soyad.capitalize()
                else:
                    print("Soyad yalnız hərflərdən ibarət olmalıdır, dəyişiklik tətbiq edilmədi.")

            if yas.isdigit() and int(yas) > 0:
                u["yas"] = int(yas)
            elif yas:
                print("Yaş yalnız rəqəmlərdən ibarət olmalıdır, dəyişiklik tətbiq edilmədi.")

            save_users(users)
            print("İstifadəçi məlumatları yeniləndi.")
            return
    print("Belə ID tapılmadı.")

def main():
    users = load_users()
    while True:
        print("\n--- MENYU ---")
        print("1 - İstifadəçi əlavə et")
        print("2 - İstifadəçini sil")
        print("3 - İstifadəçiləri göstər (0 = hamısı)")
        print("4 - İstifadəçini yenilə (ID ilə)")
        print("5 - Çıxış")

        secim = input("Seçiminizi daxil edin: ").strip()

        if secim == "1":
            add_user(users)
        elif secim == "2":
            delete_user(users)
        elif secim == "3":
            show_users(users)
        elif secim == "4":
            update_user(users)
        elif secim == "5":
            print("Proqram bitdi.")
            break
        else:
            print("Yanlış seçim. 1–5 arası rəqəm daxil edin.")

if __name__ == "__main__":
    main()
