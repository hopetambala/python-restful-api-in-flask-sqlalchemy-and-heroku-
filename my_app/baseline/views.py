import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.baseline.models import BasePerson
 
baseline = Blueprint('baseline', __name__)

#Decorators to Route..stuff 
@baseline.route('/')
@baseline.route('/home')
def home():
    return "Welcome to the Baseline Home."
 
 
class BasePersonView(MethodView):
    def get(self, id=None, page=1):
        #calls first API Rule for GET
        #returns currently existing records
        if not id:
            persons = BasePerson.query.paginate(page, 10).items
            #dictionary created to hold queried points
            res = {}
            for person in persons:
                res[person.id] = {
                    'First Name': person.fname,
                    'Last Name': person.lname,
                }
        #calls second API Rule for GET
        else:
            person = BasePerson.query.filter_by(id=id).first()
            if not person:
                abort(404)
            res = {
                'First Name': person.fname,
                'Last Name': person.lname,
            }
        return jsonify(res)
 
    def post(self):
        #creates record
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        person = BasePerson(fname, lname)
        db.session.add(person)
        db.session.commit()
        
        return jsonify({person.id: {
            'First Name': str(person.fname),
            'Last Name': str(person.lname),
        }})
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        person = BasePerson.query.filter_by(id=id).delete()
        db.session.commit()
        return
 
 
person_view =  BasePersonView.as_view('person_view')

#Rules that allow us to call the URLS
#First URL Rule allows us to get all current data and
#create a person
app.add_url_rule(
    '/person/', view_func=person_view, methods=['GET', 'POST']
)

#Second URL rule allows us to get a specific ID for a person
app.add_url_rule(
    '/person/<int:id>', view_func=person_view, methods=['GET','DELETE']
)