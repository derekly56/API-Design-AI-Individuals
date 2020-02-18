from flask_restful import Resource, reqparse 
from ai_individuals import AI_individuals
import random

class Information(Resource):
    def __init__(self):
        random.seed()
        self.next_available_id = len(AI_individuals) + 1

    def get(self, name = ""):

        SUCCESS = 200
        FAILURE = 404

        if name == "":
            return random.choice(AI_individuals), SUCCESS
        
        for individual in AI_individuals:
            if (individual['name'] == name):
                return individual, SUCCESS
        
        return "Information of individual not found", FAILURE
    
    def post(self):

        SUCCESS = 201
        FAILURE = 400

        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("summary", type=str, required=True)
        parser.add_argument("quotes", type=list, required=True)
        params = parser.parse_args()

        for individual in AI_individuals:
            if (params['name'] == individual['name']):
                return "{0} already exists".format(params['name']), FAILURE
        
        individual = {
            'id': self.next_available_id,
            'name': params['name'],
            'summary': params['summary'],
            'quotes': params['quotes']
        }

        self.next_available_id += 1
        AI_individuals.append(individual)

        return individual, SUCCESS
    
    def put(self):

        SUCCESS_PUT = 200
        SUCCESS_CREATE = 201

        parser = reqparse.RequestParser()
        parser.add_argument("curr-name", type=str, required=True)
        parser.add_argument("revised-name", type=str, required=True)
        parser.add_argument("change-name", type=bool, required=True)
        parser.add_argument("summary", type=str, required=False)
        parser.add_argument("quotes", type=list, required=False)
        params = parser.parse_args()

        for individual in AI_individuals:
            if (params['curr-name'] == individual['name']):
                if params['change-name']:
                    individual['name'] = individual['revised-name']

                individual['summary'] = params['summary']
                individual['quotes'] = params['quotes']

                return individual, SUCCESS_PUT
        
        individual = {
            'id': self.next_available_id,
            'name': params['curr-name'],
            'summary': params['summary'],
            'quotes': params['quotes']
        }

        self.next_available_id += 1
        AI_individuals.append(individual)
        
        return individual, SUCCESS_CREATE
    
    def delete(self, name):

        SUCCESS_DELETE = 200
        FAILURE = 404

        for index, individual in enumerate(AI_individuals):
            if (name == individual['name']):
                del AI_individuals[index]
                self.next_available_id -= 1

                return "{0} is deleted from list.".format(name), SUCCESS_DELETE
        
        return "{0} does not exist!".format(name), FAILURE