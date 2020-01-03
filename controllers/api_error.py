from controllers.type_result import Error


def unknownError(err):
    return Error(10001,"Unknown error",err)

def invalidParamError(field,condition,err):
    return Error(10007, "Invalid field(%s: %s)"%(field, condition), err)

def parameterParsingError(err):
    return Error(10008, "Parameter parsing error", err)

def missRequiredParamError(v):
    return Error(10009,"'%s' is required parameter" % (v), None)

def notFoundError():
    return Error(10010, "Resource is not found", None)

def notAuthorizedError():
	return Error(10011, "Resource is not authorized", None)

def notAuthorizedActionError():
	return Error(10012, "Action is not authorized", None)

def statusError(v):
	return Error(10013, "'%s', Status not Allowed"%  (v), None)

def notUpdatedError():
	return Error(10014, "Resource is not updated", None)

def notDeletedError():
	return Error(10015, "Resource is not deleted", None)

def notCreatedError():
	return Error(10016, "Resource is not created", None)

def invalidFieldError(field):
	return Error(10018, "Invalid fields [ %v ]" % field, None)


# print(statusError(111).code)