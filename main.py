import jwt


def create_token(data, secret):
    """
    Creates a json web token using algorithm HS256
    :param data: A dictionary, information that should be deciphered.
    :param secret: Secret key used to generate and verify the signature for the token.
    :return: A token that stores the data information.
    """
    token = jwt.encode(data, secret, algorithm='HS256')

    return token


def verify_signature(token):
    """

    :param token: Json web token that will decode the data using a secret key.
    :return: Returns the deciphered data or an error if the signature is not valid.
    """
    try:
        message = jwt.decode(token, 'acelera', algorithms=['HS256'])
    except jwt.exceptions.DecodeError:
        return {"error": 2}
    else:
        return message


