import pycountry
import os
import pandas as pd
import plotly.express as px


def add_alpha3_code(data):
    def make_code_column(column):
        CODE = []
        for country in column:
            try:
                code = pycountry.countries.get(name=country).alpha_3
                # .alpha_3 means 3-letter country code
                # .alpha_2 means 2-letter country code
                CODE.append(code)
            except:
                CODE.append('None')
        return CODE

    # create a column for code
    data['CODE'] = make_code_column(data.brewery_location)

    return data


def load_ratings(path_rb, path_ba):
    def load_part_of_ratings(path):
        # Import ratings data from the wrong format (txt) into a pandas DataFrame
        with open(path, 'r') as file:
            lines = file.readlines()

        data = [line.strip().split(':', 1) for line in lines]

        file_data = pd.DataFrame(data, columns=["Key", "Value"])

        file_data['Value'] = file_data['Value'].str.strip()
        selected_col = file_data['Key'].unique()
        df = pd.DataFrame(columns=selected_col, dtype=object)

        for col in selected_col:
            df[col] = file_data[file_data['Key'] == col]['Value'].values

        df = df.dropna(axis=1)

        return df

    ratings = pd.concat([load_part_of_ratings(path_rb), load_part_of_ratings(path_ba)]).drop_duplicates()

    # Set correct types
    ratings['beer_name'] = ratings['beer_name'].astype(str)
    ratings['beer_id'] = ratings['beer_id'].astype(int)
    ratings['brewery_name'] = ratings['brewery_name'].astype(str)
    ratings['brewery_id'] = ratings['brewery_id'].astype(str)
    ratings['style'] = ratings['style'].astype(str)
    ratings['abv'] = ratings['abv'].astype(float)
    ratings['date'] = ratings['date'].astype(int)
    ratings['user_name'] = ratings['user_name'].astype(str)
    ratings['user_id'] = ratings['user_id'].astype(str)
    ratings['appearance'] = ratings['appearance'].astype(float)
    ratings['aroma'] = ratings['aroma'].astype(float)
    ratings['palate'] = ratings['palate'].astype(float)
    ratings['taste'] = ratings['taste'].astype(float)
    ratings['overall'] = ratings['overall'].astype(float)
    ratings['rating'] = ratings['rating'].astype(float)
    ratings['text'] = ratings['text'].astype(str)

    return ratings


def change_country_names(data):
    # England, Wales, Norther Ireland should be United Kingdom. Ignore all states in the US
    data.loc[data['location'].str.contains('United States'), 'location'] = 'United States'
    data.loc[data['location'].str.contains('Wales'), 'location'] = 'United Kingdom'
    data.loc[data['location'].str.contains('England'), 'location'] = 'United Kingdom'
    data.loc[data['location'].str.contains('Northern Ireland'), 'location'] = 'United Kingdom'

    return data


def load_breweries(path_rb, path_ba):
    breweries_data_ba = pd.read_csv(path_ba)
    breweries_data_rb = pd.read_csv(path_rb)
    breweries_data = pd.concat([breweries_data_rb, breweries_data_ba])

    # Set correct types
    breweries_data['id'] = breweries_data['id'].astype(str)
    breweries_data['location'] = breweries_data['location'].astype(str)
    breweries_data['name'] = breweries_data['name'].astype(str)
    breweries_data['nbr_beers'] = breweries_data['nbr_beers'].astype(int)

    breweries_data = change_country_names(breweries_data)

    breweries_data = breweries_data.drop_duplicates('id')

    return breweries_data


def load_users(path_rb, path_ba):
    users_data_ba = pd.read_csv(path_ba)
    users_data_rb = pd.read_csv(path_rb)

    users_data = pd.concat([users_data_rb, users_data_ba])
    # If nbr_reviews unknown, set to -1
    users_data['nbr_reviews'] = users_data['nbr_reviews'].fillna(-1)

    # Set correct types
    users_data['joined'] = users_data['joined'].astype(str)
    users_data['location'] = users_data['location'].astype(str)
    users_data['nbr_ratings'] = users_data['nbr_ratings'].astype(int)
    users_data['nbr_reviews'] = users_data['nbr_reviews'].astype(int)
    users_data['user_id'] = users_data['user_id'].astype(str)
    users_data['user_name'] = users_data['user_name'].astype(str)

    users_data = change_country_names(users_data)

    users_data = users_data.drop_duplicates('user_id')

    return users_data


def add_user_and_brewery_location(ratings, users, breweries):
    users_location_dict = users[['user_id', 'location']].set_index('user_id').T.to_dict('list')
    users_location_dict = {x: users_location_dict.get(x)[0] for x in users_location_dict}

    breweries_location_dict = breweries[['id', 'location']].set_index('id').T.to_dict('list')
    breweries_location_dict = {x: breweries_location_dict.get(x)[0] for x in breweries_location_dict}

    ratings_final = ratings.copy()
    ratings_final['brewery_location'] = ratings_final['brewery_id'].map(breweries_location_dict)
    ratings_final['user_location'] = ratings_final['user_id'].map(users_location_dict)

    ratings_local = ratings_final[ratings_final['brewery_location'] == ratings_final['user_location']]
    ratings_international = ratings_final[ratings_final['brewery_location'] != ratings_final['user_location']]

    return ratings_final, ratings_local, ratings_international


def get_average_rating_and_count_per_brewery(ratings):
    ratings_by_brewery = ratings[['brewery_id', 'rating']]

    average_and_count = (pd.merge(left=ratings_by_brewery.groupby('brewery_id').mean(),
                                  right=ratings_by_brewery.groupby('brewery_id').count(),
                                  on='brewery_id')
                         .rename(columns={'rating_x': 'rating', 'rating_y': 'count'}))

    average_and_count = pd.merge(left=average_and_count,
                                 right=ratings[['brewery_id', 'brewery_location']],
                                 on='brewery_id')
    # Set type of count to int
    average_and_count['count'] = average_and_count['count'].astype(int)

    return average_and_count


def drop_breweries_with_less_than_n_reviews(data, n):
    return data[data['count'] >= n]


def get_average_per_country(ratings):
    return ratings.groupby('brewery_location')['rating'].mean().to_frame().sort_values(by='rating', ascending=False).reset_index()


def plot_world_map(ratings_per_country):
    fig = px.choropleth(add_alpha3_code(ratings_per_country), locations='CODE', color='rating', hover_name='brewery_location')
    fig.show()
