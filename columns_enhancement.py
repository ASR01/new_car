import pandas as pd

def market_category(df):
    cat =[]
    for index, x in df.iterrows():
        if ((x['horsepower'] > 250 and x['aspiration'] == 'turbo' and x['peakrpm'] > 6000) or x['enginelocation'] == 'rear') and x['doornumber']==2:
            cat.append('Sport')
        elif x['horsepower'] >200 or x['carbody'] == 'convertible' or x['cylindernumber'] in [8,10,12]:
            cat.append('Luxury')
        else:
            cat.append('Normal')
    df['market category'] = pd.DataFrame((cat))

    return df


def add_columns(df):

    #df = pd.read_csv('./data/CarPrice_Assignment.csv')

    dfe = df.copy()

    get_brand = lambda x: x.split()[0].strip() if x else None

    dfe['brand'] = dfe['CarName'].apply(get_brand)


    d1 = {'alfa-romero': 'alfa-romeo',
          'maxda':'mazda',
          'Nissan' : 'nissan',
          'porcshce' : 'porsche',
          'toyouta' : 'toyota',
          'vokswagen' : 'vw',
          'volkswagen' : 'vw'
    }

    d2 = {
          'alfa-romeo' : 'Enhanced',
          'audi':'Premium',
          'bmw':'Premium',
          'chevrolet':'Normal',
          'dodge':'Normal',
          'honda':'Normal',
          'isuzu':'Normal',
          'jaguar':'Premium',
          'mazda':'Normal',
          'buick':'Premium',
          'mercury':'Premium',
          'mitsubishi':'Normal',
          'nissan':'Normal',
          'peugeot':'Normal',
          'plymouth':'Normal',
          'porsche':'Premium',
          'renault':'Normal',
          'saab':'Normal',
          'subaru':'Normal',
          'toyota':'Normal',
          'vw':'Enhanced',
          'volvo':'Enhanced'}
            
    dfe['brand'] = dfe.brand.replace(d1)
    dfe['brandtype'] = dfe.brand.replace(d2)
    dfe.drop('CarName', axis = 1, inplace=True)
    dfe.drop('brand', axis = 1, inplace=True)
    
    dfe = market_category(dfe)
    dfe = dfe.drop(['car_ID'],axis = 1)
    dfe.to_csv('./data/enhanced_data.csv', index = False, header=True)    
    return(dfe)

def getting_default_values(df):
    
	df = df.drop('price',axis = 1)

	col = list(df.columns)
	print(col)

	dfm = pd.DataFrame(columns = col, index = [0])
	dfm.append(pd.Series(), ignore_index=True)

	cat_vars = df.select_dtypes(include=[object]).columns.values.tolist()
	num_vars = df.select_dtypes(exclude=[object]).columns.values.tolist() # still not working, same error as before

	for f in cat_vars:
		sol = df[f].mode()
		dfm[f] = sol

	for f in num_vars:
		sol = df[f].mean()
		dfm[f]=sol	

	dfm.to_csv('./data/default_values.csv',index = False, header= True)
	#print(dfm)
	return dfm



def main():

	df = pd.read_csv('./data/CarPrice_Assignment.csv')
	dfm = add_columns(df)
	getting_default_values(dfm)

if __name__ == '__main__':
    main()

