from flask import Flask,jsonify,render_template,request,redirect, url_for
from get_rent import get_rent
from get_latlng import get_latlng
from get_facility import get_nearby_places
import time
from datetime import timedelta
import pickle
import json

app = Flask(__name__)

#設置
#緩衝的調快
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=1)



# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.get_json()
      
#       print(result['Name'])

     
#       return render_template("result.html",result = result)

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#    return 'Blog Number %d' % postID

# @app.route('/hello/<user>')
# def hello_name(user):
   
#    return render_template('hello.html', name = user)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/address')
def address():
    return render_template('address.html')

@app.route('/keyAddress', methods=['POST'])
def keyAddress():

   user =  request.form['username']
    # password = request.form['password']
   if user:
      try:
         new_array=[]
         latlng=[]
         #抓經緯度
         # latlng = get_latlng(user)
         # newlatlng = str(latlng).strip('[]') #轉成str

         #爬網的租金
         rent=5#測試用
         # rent=get_rent(user)
         if (rent==None):#這邊要改成get_rent
            return jsonify({'error' : '查無租金 data!'})
         else:
            new_array.append(rent)

         school=10
         hospital=5
         bus_station=10
         subway_station=12
         parking=5
         movie_theater=3
         
         #抓附近設施
         # hospital = get_nearby_places(newlatlng,'hospital', '',0)
         # bus_station = get_nearby_places(newlatlng,'bus_station', '',0)
         # school = get_nearby_places(newlatlng,'school', '',0)
         # subway_station = get_nearby_places(newlatlng,'subway_station', '',0)
         # parking = get_nearby_places(newlatlng,'parking', '',0)
         # movie_theater = get_nearby_places(newlatlng,'movie_theater', '',0)
         #並放入array
         new_array.append(bus_station)
         new_array.append(school)
         new_array.append(hospital)
         new_array.append(subway_station)
         new_array.append(parking)
         new_array.append(movie_theater)
         print(new_array)
         #用dataframe存放抓回來的資料，並將data放入predict
         # data=pd.DataFrame(columns=['bus_station','school','hospital','subway_station','parking','movie_theater','price'])
         # data.loc['1']=new_array
         # #載訓練好的模型
         # with open('save/clf.pickle','rb') as f:
         #    clf2 = pickle.load(f)
         #    test_y_predicted=clf2.predict(data)
         #    print(test_y_predicted)
         # #test_y_predicted = forest.predict(X_test)
         
         #  return json.dumps({'status':'OK','user':user})
         return jsonify({'user':user})
         # return render_template('result.html',x=user)
      except :
         return jsonify({'error' : 'Missing data1!'})
   else:
      return jsonify({'error' : 'Missing data!'})


   
  
   
   

if __name__ == "__main__":
    app.run(
      #任何ip都可以訪問
            port=7777,#端口
            debug=True
    )