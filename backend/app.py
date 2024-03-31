# from flask import Flask


# app= Flask(__name__)

# @app.route('/members')
# def member():
#     return{"members":["mem1", "mem2" , "mem444"]}



# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

print("leh")

@app.route('/bags')
def get_bags():
    print("hi")
    conn = sqlite3.connect('bags.db')
    print("hiii")
    cur = conn.cursor()
    print("hellloo")
    cur.execute("SELECT * FROM bags")
    print("yes")
    bags = cur.fetchall()
    print("no")
    conn.close()
    print(bags)
    return jsonify(bags)
    



if __name__ == '__main__':
    app.run(debug=True)



