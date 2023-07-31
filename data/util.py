import pandas as pd

def get_data(PATH_characters, PATH_planets, PATH_species, PATH_starships, PATH_vehicles):
    df_char = pd.read_csv(PATH_characters)
    df_plan = pd.read_csv(PATH_planets)
    df_spec = pd.read_csv(PATH_species)
    df_ship = pd.read_csv(PATH_starships)
    df_vehi = pd.read_csv(PATH_vehicles)

    df_collection = pd.DataFrame()
    df_collection["title"] = ["characters", "planets", "species", "starships", "vehicles"]
    df_collection["dfs"] = [df_char, df_plan, df_spec, df_ship, df_vehi]

    return df_collection

    # df_char["mass"].fillna("unknown", inplace=True)
    # df_char["height"].fillna("unknown", inplace=True)
    # df_char["hair_color"].fillna("no hair", inplace=True)
    # df_char["birth_year"].fillna("unknown", inplace=True)
    # df_char["sex"].fillna("not applicable", inplace=True)
    # df_char["gender"].fillna("not applicable", inplace=True)
    # df_char["homeworld"].fillna("unknown", inplace=True)
    # df_char["species"].fillna("unknown", inplace=True)
    # df_char["vehicles"].fillna("", inplace=True)
    # df_char["starships"].fillna("", inplace=True)

