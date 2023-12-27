park_data = pd.read_csv('30_Training Dataset_V2/external_data/Park.csv')

# 去除重複的經緯度
park_data.drop_duplicates(subset=['lat', 'lng'], inplace=True)

# 創建 BallTree
park_tree = BallTree(np.deg2rad(park_data[['lat', 'lng']].values), metric='haversine')


for idx, row in enumerate(all_data.itertuples()):
    lat = coordinates.loc[idx, 'lat']
    lng = coordinates.loc[idx, 'lng']

    # 新增特徵
    all_data.at[idx, 'num_park_3km'] = count_facilities(park_tree, lat, lng, km=3)
    all_data.at[idx, 'num_park_5km'] = count_facilities(park_tree, lat, lng, km=5)
    all_data.at[idx, 'distance_to_nearest_park'] = distance_to_nearest_facilities(park_tree, lat, lng)
    all_data.at[idx, 'avg_distance_to_nearest_5_park'] = average_distance_to_nearest_facilities(park_tree, lat, lng)
# 查看更新後的 DataFrame
print(all_data[['num_park_3km', 'num_park_5km', 'distance_to_nearest_park', 'avg_distance_to_nearest_5_park']].describe())