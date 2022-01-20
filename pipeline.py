import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error,mean_absolute_percentage_error
from sklearn.impute import SimpleImputer
import pickle as pk
from columns_enhancement import add_columns
from row_enhancement import row_enhancement_fuel_type,row_enhancement_fuel_type_2


#Parameters




def pipe_car(df):
       
		
          
              
		cat_vars = df.select_dtypes(include=[object]).columns.values.tolist()
		num_vars = df.select_dtypes(exclude=[object]).columns.values.tolist()
		num_vars.remove('price')
              
              
       
       
		cat_pipe = Pipeline([ 
                       	('ordinal_encoder', OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1))
                       		])
		num_pipe = Pipeline([
      					('imputer', SimpleImputer(strategy='mean'))
							])
		preprocessing = ColumnTransformer([
			('categorical', cat_pipe, cat_vars),
			('numerical', num_pipe, num_vars)
			], remainder='drop')
       
		x = df.drop('price', axis = 1)
		y =df['price']
       
		model = ExtraTreesRegressor(criterion='absolute_error', max_features='sqrt', n_estimators=100)
		X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=23)
       
		error_rang = abs(y_train.max()) + abs(y_train.min())
       
		X_red = X_train[:0]
		X_red.head(1).to_csv('./data/export_X_red.csv', index = False)
       
       #print(X_train)
       #print('x')y
       #print(y_train)
       
		pipe = Pipeline([
              ('preprocessor', preprocessing),
              ('regressor', model)
              ])
		pipe.fit(X_train, y_train)
		y_pred = pipe.predict(X_test)
		print(type(y_pred), type(X_test))
		print(X_test.head(1))
		print(pipe.predict(X_test.head(1)))
#		print(y_pred.loc[[1]], X_test.loc[[1]])
		X_test.head(1).to_csv('test.csv')
		print(X_test.head(1).shape)
       
		results = { "MSE": mean_squared_error(y_test, y_pred),
					"MAB": mean_absolute_error(y_test, y_pred),
					"Perc. error": mean_absolute_percentage_error(y_test, y_pred)*100
                     }           
		print(results)             
       
		ans = input('Do you want to store the model? (Y/N) \n')
		if ans in ('y', 'Y'):
			model_name = './model/optimal_model.pkl'
			with open(model_name, 'wb') as file:
				pk.dump(model, file)
			model_name = './model/pipe_model.pkl'
			with open(model_name, 'wb') as file:
				pk.dump(pipe, file)

		return mean_squared_error(y_test, y_pred)

def main():
	df = pd.read_csv('./data/enhancedAssignment.csv')
	pipe_car(df)

if __name__ == '__main__':
    main()
