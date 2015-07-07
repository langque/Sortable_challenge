'''

'''
import json 
import io
import json as simplejson



Company_List = {}
class result_entry:
	def __init__(self, listings, product_name):
		self.product_name = product_name
		self.listings = []

#Input the products info into Company_list dict, help for the
#later match process
f_products = open('products.txt', 'r')
for line in f_products:
	parsed_data = simplejson.loads(line)

	product_name = parsed_data['product_name']
	manufacturer = parsed_data['manufacturer']
	model = " " + parsed_data['model']

	new_entry = result_entry([], product_name)				#create each product as an object, init it with product name and empty list
	if Company_List.has_key(manufacturer) == False:			#check is the company's name already in dict, if not create it
		Company_List[manufacturer] = {}
	Company_List[manufacturer].update({model:new_entry})	#store the prodcut object in dict by using the company name and model as the key

#read from the listings file to find the prop object to be stored.
f_price = open('listings.txt', 'r')					
for line in f_price:
	parsed_data = simplejson.loads(line)
	title = parsed_data['title']
	manufacturer = title.split(" ")[0]
	if Company_List.has_key(manufacturer): 
		key_list = Company_List[manufacturer].keys()
		for key in key_list:
			if (key in title) or (key.replace(" ","") in title):
				Company_List[manufacturer][key].listings.append(json.loads(line))



#Convert dict objects to json object and write them into a file called result.txt

data = []
manufacturer_key_list = Company_List.keys()
for manufacturer_key in manufacturer_key_list:
	model_key_list = Company_List[manufacturer_key].keys()
	for model_key in model_key_list:
		data.append(Company_List[manufacturer_key][model_key].__dict__)

with open('result.txt', 'w') as feedsjson:
	for obj in data:
		json.dump(obj, feedsjson,sort_keys=False)
		feedsjson.write('\n')





