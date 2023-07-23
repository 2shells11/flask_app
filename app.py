from flask import Flask, request, jsonify
import json
app = Flask(__name__)
book_list = [
    {
        "id": 0,
        "author": "author1",
        "language": "english",
        "title": "title1",
    },
    {
        "id": 1,
        "author": "author2",
        "language": "english",
        "title": "title2"
    }

]

@app.route('/books',methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(book_list)>0:
            return jsonify(book_list)
        else:
            'Nothing found', 404

    if request.method == 'POST':
        # new_author = request.form['author']
        # new_lang = request.form['language']
        # new_title = request.form['title']
        # #new_author = {'new_author': request.json['author']}

       
        iD = book_list[-1]['id']+1
    

        new_obj = {
            "id": iD,
            "author": "author1",
            "language": "english",
            "title": "title1"
        }
     

        book_list.append(new_obj)
    return jsonify(book_list), 201


@app.route('/book/<int:id>', methods= ['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in book_list:
            if book['id'] == id:
                return jsonify(book)
            pass

    if request.method == 'PUT':
        
        for book in book_list:
            if book['id'] == id:
                # book['author'] = request.form['author']
                # book['language'] = request.form['language']
                # book['title'] = request.form['title']
                # updated_book = {
                #     'id': id,
                #     'author': book['author'],
                #     'language': book['language'],
                #     'title': book['title']
                # }
                updated_book = {
                    'id': id,
                    'author': 'updated_author',
                    'language': 'updated_lang',
                    'title': 'updated_title'
                }
                return jsonify(updated_book)
            pass
    if request.method == 'DELETE':
        for index, book in enumerate(book_list):
            if book['id'] == id:
                book_list.pop(index)
                return jsonify(book_list)
        



if __name__ == '__main__':
    app.run()