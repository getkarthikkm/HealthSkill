"""
Helper module for customerResource operations.
"""
import logging
from httplib import OK, BAD_REQUEST, UNPROCESSABLE_ENTITY, CREATED, INTERNAL_SERVER_ERROR

from Model import db, Customer, CustomerSchema

customers_schema = CustomerSchema(many=True)
customer_schema = CustomerSchema()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')


def generate_success_response(status, data):
    """
    Generate success response with the status code and data.
    :param status: enum
    :param data: dict
    :return: tuple
    """
    logging.info("Sending success response with status : {}".format(status))
    return {"status": 'success', 'skill': data}, status


def generate_failure_response(status, message):
    """
    Generate failure response with the status code and error messsage.
    :param status: enum
    :param message: str
    :return: tuple
    """
    logging.info("Generating failure response with status : {}".format(status))
    return {"status": 'fail', 'message': message}, status


def read_items(args):
    """
    Read items from the database based on input. Reads all the items if no argument provided.
    Read items based on name / category when name / category is provided.
    :param args: dict
    :return: tuple
    """

    def filter_by_inputs(input_param):
        """
        Read items from database based on input provided as argument.
        :param input_param: string
        :return: tuple
        """
        customer = Customer.query.filter_by(name=args[input_param].strip()).first()
        if not customer:
            return generate_failure_response(BAD_REQUEST, 'Customer does not exist')
        else:
            result = customer_schema.dump(customer).data
            return generate_success_response(OK, result)
    try:
        logging.info("get request received with arguments : {}".format(args))

        if len(args) > 0:
            if 'name' in args:
                return filter_by_inputs('name')
            else:
                return generate_failure_response(BAD_REQUEST, 'Invalid data provided')
        else:
            customers = Customer.query.all()
            customers = customers_schema.dump(customers).data
            return generate_success_response(OK, customers)
    except Exception as e:
        return generate_failure_response(INTERNAL_SERVER_ERROR, str(e))


def skill_assessment(data):
    skill = ""
    if not data['has_provider']:
        skill = "S001"
    elif 2000 <= int(data['postcode']) <= 4999:
        if data['cover_type'] == "combined":
            skill = "S002"
        elif data['marital_status'] != "single" and data['has_children']:
            skill = "S001"
        else:
            skill = "S004"
    elif data['marital_status'] == "single" and data['has_children']:
        skill = "S003"
    else:
        skill = "S004"
    return skill


def create_item(json_data):
    """
    Create new item if the item does not exist in the database.
    :param json_data: dict
    :return: tuple
    """
    try:
        if not json_data:
            return generate_failure_response(BAD_REQUEST, 'No input data provided')
        # Validate and deserialize input
        data, errors = customer_schema.load(json_data['customer'])
        if errors:
            return errors, UNPROCESSABLE_ENTITY
        # Check if the item already exists.
        customer = Customer.query.filter_by(name=data['name']).first()

        if customer:
            return generate_failure_response(BAD_REQUEST, 'customer already exists')
        skill = skill_assessment(data)
        customer = Customer(name=data['name'],
                            postcode=data['postcode'],
                            age=data['age'],
                            gender=data['gender'],
                            has_provider=data['has_provider'],
                            has_children=data['has_children'],
                            marital_status=data['marital_status'],
                            cover_type=data['cover_type'],)
        customer.skill = skill
        db.session.add(customer)
        db.session.commit()
        result = customer_schema.dump(customer).data
        return generate_success_response(CREATED, skill)
    except Exception as e:
        return generate_failure_response(INTERNAL_SERVER_ERROR, str(e))



