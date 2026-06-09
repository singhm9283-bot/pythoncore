# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# # Original dataset
# data = {
#     'team_strength': [85, 90, 88, 75, 92, 78, 95, 80, 84, 86],
#     'player_performance': [80, 85, 82, 76, 88, 74, 90, 78, 81, 85],
#     'home_away': [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
#     'team_stats': [100, 95, 97, 80, 105, 70, 110, 85, 90, 95],
#     'match_result': [1, 0, 1, 0, 1, 0, 1, 1, 0, 1]
# }
# # convert the data into frames
# df = pd.DataFrame(data)

# #convert the input dataframe and output dataframe into list......
    
# X = df[['team_strength','player_performance','home_away','team_stats']]
# y=df['match_result']
# # call the model to predict the data....
# model = LogisticRegression()


# # Train and test the given dataset.....
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model.fit(X_train, y_train)

# #predict the next match winning.....
# print(model.predict(X_test))

# new_match= np.array([[30,60,0,70]])
# new_prediction=model.predict(new_match)
# print(new_prediction)



# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# data = {
#     'height': [5.4, 5.9, 6.3, 5.8, 5.5, 5.2, 5.6, 5.0, 5.1, 5.7],  # Example feature 1
#     'salary': [8, 10, 6, 12, 9, 11, 3, 0, 15, 35],  # Example feature 2
#     'intelligence': [10, 5, 3, 4, 7, 8, 9, 3, 2, 8],  # 1 for home, 0 for away
#     'maturity': [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],  # Example feature 4
#     'dressing': [1,0,1,0,1,0,1, 0, 1, 1],
#     'date': [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]  # 1 for win, 0 for loss
# }
# df=pd.DataFrame(data)
# X = df[['height','salary','intelligence','maturity','dressing']]
# y=df['date']
# # call the model to predict the data....
# model = LogisticRegression()


# # Train and test the given dataset.....
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# model.fit(X_train, y_train)

# #predict the next match winning.....
# print(model.predict(X_test))

# new_match= np.array([[5.8,12,5,1,1,]])
# new_prediction=model.predict(new_match)
# print(new_prediction)



