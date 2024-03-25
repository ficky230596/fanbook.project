from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://Basilius:mario@cluster01.biqbzlj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01')
db = client.dbficky

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    try:
        bucket_receive = request.form['bucket_give']
        count = db.bucket.count_documents({})
        num = count + 1
        doc = {
            'num': num,
            'bucket': bucket_receive,
            'done': 0
        }
        db.bucket.insert_one(doc)
        return jsonify({'msg': 'Data Saved!'})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    try:
        num_receive = request.form['num_give']
        db.bucket.update_one(
            {'num': int(num_receive)},
            {'$set': {'done': 1}}
        )
        return jsonify({'msg': 'Update Done!'})
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route("/bucket", methods=["GET"])
def bucket_get():
    try:
        buckets_list = list(db.bucket.find({}, {'_id': False}))
        return jsonify({'buckets': buckets_list})
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route("/delete", methods=["POST"])
def delete_bucket():
    try:
        num = int(request.form['num']) # Ambil nilai num dari muatan data POST
        db.bucket.delete_one({'num': num}) # Hapus ember dengan num yang sesuai dari database
        return jsonify({'msg': 'Item deleted successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
