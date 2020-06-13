from flask_restplus import Namespace, Resource
api = Namespace(name='', description='API namespace.')


@api.route('/model')
class HousePricePredictionResource(Resource):
    @api.doc('House Price Prediction baseline')
    @api.response(400, 'Error')
    def post(self):
        return "Hello"
