# how to handle exception messages?

# initially,the exception can be of with 3 major types,

# 400 - BadRequest(requesting non validated data, duplicate ids)
# 404 - NotFound(user requested data is not in the database)
# 403 - Forbidden(when we are trying to access a non authorised data)

# API_SPEC
{
"responses": {
    "400": {
        "schema": {
            "type": "object",
            "properties": {
                "response": {
                    "type": "string"
                },
                "https_status_code": {
                    "type": "string"
                },
                "res_string": {
                    "type": "string",
                    "enum": [
                            "INVALID_ITEM_ID",
                            "INVALID_FORM_IDS",
                            "DUPLICATE_ITEM_IDS"
                        ]
                }
            }
        }
    }
}
}

# for suppose we get 400 error so we write in the custom_expections

INVALID_FORM_ID_EXCEPTION = (
    "given form id is invalid", "INVALID_FORM_ID"
)

# in presenter we generally raise with custom exceptions

class PresenterImplementation:

    def get_invalid_form_failure_response(self):
        from django.http import HttpResponse
        import json
        from custom_expections import INVALID_FORM_ID_EXCEPTION
        response = INVALID_FORM_ID_EXCEPTION[0]
        https_status_code = 400
        res_string = INVALID_FORM_ID_EXCEPTION[1]
        data = {
            "response": response,
            "https_status_code": https_status_code,
            "res_string": res_string
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, status_code=400)